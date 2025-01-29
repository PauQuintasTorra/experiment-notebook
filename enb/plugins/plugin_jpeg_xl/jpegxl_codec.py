#!/usr/bin/env python3
"""Wrapper for the JPEG-XL reference implementation
"""
__author__ = "Ashwin Kumar Gururajan <ashwin.gururajan@uab.cat>"
__since__ = "2021/02/15"

import os
import shutil
import enb
from enb import icompression
import numpy as np
from imagecodecs import jpegxl_encode, jpegxl_decode

class JPEG_XL(icompression.LosslessCodec, icompression.LossyCodec):
    def __init__(self, quality_0_to_100=100, compression_level=7,
                 lossless=True,
                 compressor_path=os.path.join(os.path.dirname(__file__), "cjxl"),
                 decompressor_path=os.path.join(os.path.dirname(__file__), "djxl")):
        """
        :param quality_0_to_100: Quality setting. Range: -inf .. 100.
        100 = mathematically lossless. Default for already-lossy input (JPEG/GIF).
        Positive quality values roughly match libjpeg quality.
        Uses jpeg_xl parameter -q and was chosen over -d maxError
        (defined by butteraugli distance) becuase of slightly better throughput
        (approx 1.2 Mp/s) under lossless mode
        :param compression_level: higher values mean slower compression
        :param lossless: if True, the modular mode of JPEG-XL is employed (in this case quality 100 is required)
        """
        assert 3 <= compression_level <= 9
        assert 0 <= quality_0_to_100 <= 100
        assert (not lossless) or quality_0_to_100 == 100, f"Lossless mode can only be employed with quality 100"

        super().__init__(param_dict=dict(cl=compression_level, quality=quality_0_to_100))


    def compress(self, original_path, compressed_path, original_file_info):
        assert original_file_info["bytes_per_sample"] in [1, 2], \
            "JPEG XL only supported for 8 or 16 bit images"
        img = enb.isets.load_array_bsq(
            file_or_path=original_path, image_properties_row=original_file_info)
        img = np.moveaxis(img, 0, -1).byteswap().newbyteorder('<')
        encoded = jpegxl_encode(img, level=self.param_dict["quality"], effort=self.param_dict["cl"])
        with open(compressed_path, 'wb') as f:
            f.write(encoded)

    def decompress(self, compressed_path, reconstructed_path, original_file_info=None):
        with open(compressed_path, 'rb') as f:
            encoded = f.read()
        img = jpegxl_decode(encoded)
        img = np.moveaxis(img, -1, 0).byteswap().newbyteorder(">" if original_file_info["big_endian"] else "<")
        enb.isets.dump_array_bsq(img, reconstructed_path)

    @property
    def label(self):
        return f"JPEG XL"
