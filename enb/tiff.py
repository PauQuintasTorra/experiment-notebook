#!/usr/bin/env python3
"""Module to handle TIFF images
"""
__author__ = "Xavier Fernández-Mellado"
__since__ = "2025/03/02"

import os
import sys
import re
import tempfile

import numpy as np
import tifffile

import enb
import enb.isets


class TIFFWrapperCodec(enb.icompression.WrapperCodec):
    """Raw images are coded into TIFF before compression with the wrapper,
    and TIFF is decoded to raw after decompression.
    """

    # pylint: disable=abstract-method

    def compress(self, original_path: str, compressed_path: str, original_file_info=None):
        assert original_file_info["bytes_per_sample"] in [1, 2], \
            "PAM only supported for 8 or 16 bit images"
        assert original_file_info["big_endian"], \
            f"Only big-endian samples are supported by {self.__class__.__name__}"
        img = enb.isets.load_array_bsq(
            file_or_path=original_path, image_properties_row=original_file_info)


        with tempfile.NamedTemporaryFile(suffix=".tiff", mode="wb") as tmp_file:
            tifffile.imwrite(tmp_file.name, img, compression='none')

            compression_results = super().compress(
                original_path=tmp_file.name,
                compressed_path=compressed_path,
                original_file_info=original_file_info)
            crs = self.compression_results_from_paths(
                original_path=original_path, compressed_path=compressed_path)
            crs.compression_time_seconds = max(
                0, compression_results.compression_time_seconds)
            crs.maximum_memory_kb = compression_results.maximum_memory_kb
            return crs

    def decompress(self, compressed_path, reconstructed_path,
                   original_file_info=None):
        with tempfile.NamedTemporaryFile(suffix=".tiff") as tmp_file:
            decompression_results = super().decompress(
                compressed_path=compressed_path,
                reconstructed_path=tmp_file.name)
            
            img = tifffile.imread(tmp_file.name)
            enb.isets.dump_array_bsq(img, file_or_path=reconstructed_path)

            drs = self.decompression_results_from_paths(
                compressed_path=compressed_path,
                reconstructed_path=reconstructed_path)
            drs.decompression_time_seconds = \
                decompression_results.decompression_time_seconds
