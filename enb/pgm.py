#!/usr/bin/env python3
"""Module to handle PGM (P5), PPM (P6) and PAM (P7) images
"""
__author__ = "Miguel Hernández-Cabronero"
__since__ = "2020/04/08"

import os
import sys
import re
import tempfile

import numpy as np

import enb
import enb.isets


class PAMWrapperCodec(enb.icompression.WrapperCodec):
    """Raw images are coded into PAM before compression with the wrapper,
    and PAM is decoded to raw after decompression.
    """

    # pylint: disable=abstract-method

    def compress(self, original_path: str, compressed_path: str, original_file_info=None):
        assert original_file_info["bytes_per_sample"] in [1, 2], \
            "PAM only supported for 8 or 16 bit images"
        assert original_file_info["big_endian"], \
            f"Only big-endian samples are supported by {self.__class__.__name__}"
        img = enb.isets.load_array_bsq(
            file_or_path=original_path, image_properties_row=original_file_info)


        with tempfile.NamedTemporaryFile(suffix=".pam", mode="wb") as tmp_file:

            write_pam(img, original_file_info["bytes_per_sample"], tmp_file.name)

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
        with tempfile.NamedTemporaryFile(suffix=".pam") as tmp_file:
            decompression_results = super().decompress(
                compressed_path=compressed_path,
                reconstructed_path=tmp_file.name)
            
            img = read_pam(tmp_file.name)
            enb.isets.dump_array_bsq(img, file_or_path=reconstructed_path)

            drs = self.decompression_results_from_paths(
                compressed_path=compressed_path,
                reconstructed_path=reconstructed_path)
            drs.decompression_time_seconds = \
                decompression_results.decompression_time_seconds

class PGMCurationTable(enb.png.PNGCurationTable):
    """Given a directory tree containing PGM images, copy those images into
    a new directory tree in raw BSQ format adding geometry information tags to
    the output names recognized by `enb.isets.load_array_bsq`.
    """
    dataset_files_extension = "pgm"


def read_pgm(input_path, byteorder='>'):
    """Return image data from a raw PGM file as numpy array.
    Format specification: http://netpbm.sourceforge.net/doc/pgm.html

    (From answer:
    https://stackoverflow.com/questions/7368739/numpy-and-16-bit-pgm)
    """
    with open(input_path, 'rb') as input_file:
        buffer = input_file.read()
    try:
        header, width, height, maxval = re.search(
            br"(^P5\s(?:\s*#.*[\r\n])*"
            br"(\d+)\s(?:\s*#.*[\r\n])*"
            br"(\d+)\s(?:\s*#.*[\r\n])*"
            br"(\d+)\s)", buffer).groups()
    except AttributeError as ex:
        raise ValueError(f"Not a raw PGM file: '{input_path}'") from ex

    return np.frombuffer(
        buffer,
        dtype='u1' if int(maxval) < 256 else byteorder + 'u2',
        count=int(width) * int(height),
        offset=len(header)).reshape((int(width), int(height)), order="F")


def write_pgm(array, bytes_per_sample, output_path, byteorder=">"):
    """Write a 2D array indexed with [x,y] into output_path with PGM format.
    """
    array = np.squeeze(array)
    assert bytes_per_sample in [1, 2], \
        f"bytes_per_sample={bytes_per_sample} not supported"
    assert len(array.shape) == 2, "Only 2D arrays can be output as PGM"
    assert (array.astype(int) - array < 2 * sys.float_info.epsilon).all(), \
        "Only integer values can be stored in PGM"
    assert array.min() >= 0, "Only positive values can be stored in PGM"
    assert array.max() <= 2 ** (8 * bytes_per_sample) - 1, \
        f"All values should be representable in {bytes_per_sample} bytes " \
        f"(max is {array.max()}, bytes_per_sample={bytes_per_sample})"
    width, height = array.shape
    with open(output_path, "wb") as output_file:
        output_file.write(
            f"P5\n{width}\n{height}\n"
            f"{(2 ** (8 * bytes_per_sample)) - 1}\n".encode("utf-8"))
        array.swapaxes(0, 1).astype(f"{byteorder}u{bytes_per_sample}").tofile(
            output_file)


def read_ppm(input_path, byteorder='>'):
    """Return image data from a raw PGM file as numpy array.
    Format specification: http://netpbm.sourceforge.net/doc/pgm.html

    (From answer:
    https://stackoverflow.com/questions/7368739/numpy-and-16-bit-pgm)
    """
    with open(input_path, 'rb') as input_file:
        buffer = input_file.read()
    try:
        header, width, height, maxval = re.search(
            rb"(^P6\s(?:\s*#.*[\r\n])*"
            rb"(\d+)\s(?:\s*#.*[\r\n])*"
            rb"(\d+)\s(?:\s*#.*[\r\n])*"
            rb"(\d+)\s)", buffer).groups()
    except AttributeError as ex:
        raise ValueError(f"Not a raw PGM file: '{input_path}'") from ex

    return np.frombuffer(
        buffer,
        dtype='u1' if int(maxval) < 256 else byteorder + 'u2',
        count=int(width) * int(height) * 3,
        offset=len(header)).reshape((3, int(width), int(height)),
                                    order="F").swapaxes(0, 2).swapaxes(0, 1)


def write_ppm(array, bytes_per_sample, output_path):
    """Write a 3-component 3D array indexed with [x,y,z] into output_path
    with PPM format.
    """
    assert bytes_per_sample in [1], \
        f"bytes_per_sample={bytes_per_sample} not supported"
    assert len(array.shape) == 3, \
        f"Only 3D arrays can be output as PPM ({array.shape=})"
    assert (array.astype(int) - array < 2 * sys.float_info.epsilon).all(), \
        "Only integer values can be stored in PPM"
    assert array.min() >= 0, "Only positive values can be stored in PPM"
    assert array.max() <= 2 ** (8 * bytes_per_sample) - 1, \
        f"All values should be representable in {bytes_per_sample} bytes " \
        f"(max is {array.max()}, bytes_per_sample={bytes_per_sample})"
    width, height, component_count = array.shape
    assert component_count == 3, \
        f"Only 3D arrays can be output as PPM ({array.shape=})"

    with open(output_path, "wb") as output_file:
        output_file.write(
            f"P6\n{width}\n{height}\n"
            f"{(2 ** (8 * bytes_per_sample)) - 1}\n".encode("utf-8"))
        enb.isets.dump_array_bip(
            array=array, file_or_path=output_file, dtype=np.uint8)
        

def read_pam(input_path, byteorder='>'):
    """Return image data from a raw PAM file as a numpy array."""
    with open(input_path, 'rb') as input_file:
        buffer = input_file.read()

    try:
        match = re.search(
            rb"^P7\s+"
            rb"(WIDTH\s+(\d+)\s*)" 
            rb"(HEIGHT\s+(\d+)\s*)"
            rb"(DEPTH\s+(\d+)\s*)" 
            rb"(MAXVAL\s+(\d+)\s*)"
            rb"(TUPLTYPE\s+\w+\s*)"
            rb"ENDHDR\s",
            buffer
        )

        if not match:
            raise ValueError(f"Not a valid PAM file: '{input_path}'")

        width = int(match.group(2))
        height = int(match.group(4))
        depth = int(match.group(6))
        maxval = int(match.group(8))

    except AttributeError as ex:
        raise ValueError(f"Invalid PAM header in '{input_path}'") from ex

    dtype = 'u1' if maxval < 256 else byteorder + 'u2'
    
    offset = match.end()

    img =  np.frombuffer(
        buffer,
        dtype=dtype,
        count=width * height * depth,
        offset=offset
    )
    
    if depth == 1:
        return img.reshape((int(height), int(width)),
                  order="C")

    return img.reshape((int(depth), int(height), int(width)),
              order="F").swapaxes(0, 2).swapaxes(0, 1)

def write_pam(array, bytes_per_sample, output_path, byteorder=">"):
    """
    Write a 3D array indexed with [height, width, channels] into output_path with PAM format.
    Supports up to 4 channels (Grayscale, RGB, RGBA).
    """
    array = np.squeeze(array)
    assert bytes_per_sample in [1, 2], f"bytes_per_sample={bytes_per_sample} not supported"
    assert len(array.shape) <= 4, "Only 3D arrays can be output as PAM (grayscale, alpha, RGB or RBGA)"
    assert (array.astype(int) - array < 2 * sys.float_info.epsilon).all(), "Only integer values can be stored in PAM"
    assert array.min() >= 0, "Only positive values can be stored in PAM"
    assert array.max() <= 2 ** (8 * bytes_per_sample) - 1, (
        f"All values should be representable in {bytes_per_sample} bytes "
        f"(max is {array.max()}, bytes_per_sample={bytes_per_sample})"
    )
    
    height, width = array.shape[:2]
    depth = 1 if len(array.shape) == 2 else array.shape[2]
    maxval = (2 ** (8 * bytes_per_sample)) - 1

    tupltype = {1: "GRAYSCALE", 2: "GRAYSCALE_ALPHA", 3: "RGB", 4: "RGB_ALPHA"}.get(depth, "UNKNOWN")
    
    with open(output_path, "wb") as output_file:
        output_file.write(
            f"P7\nWIDTH {width}\nHEIGHT {height}\nDEPTH {depth}\nMAXVAL {maxval}\nTUPLTYPE {tupltype}\nENDHDR\n".encode("utf-8")
        )
        if depth == 1:
            array.astype(f"{byteorder}u{bytes_per_sample}").tofile(
            output_file)
        else:
            enb.isets.dump_array_bip(
                array=array, file_or_path=output_file, 
                dtype=np.uint8 if bytes_per_sample == 1 else np.uint16)


def pgm_to_raw(input_path, output_path):
    """Read a file in PGM format and write its contents in raw format,
    which does not include any geometry or data type information.
    """
    enb.isets.dump_array_bsq(array=read_pgm(input_path),
                             file_or_path=output_path)

def ppm_to_raw(input_path, output_path):
    """Read a file in PPM format and write its contents in raw format,
    which does not include any geometry or data type information.
    """
    enb.isets.dump_array_bsq(array=read_ppm(input_path),
                             file_or_path=output_path)
