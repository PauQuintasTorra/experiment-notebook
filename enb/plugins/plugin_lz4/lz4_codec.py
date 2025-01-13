#!/usr/bin/env python3
"""Codec wrapper for the LZ4 lossless image coder
"""
__author__ = "Òscar Maireles and Miguel Hernández-Cabronero"
__since__ = "2021/06/01"

import os
import enb.icompression


class Lz4(enb.icompression.LosslessCodec, enb.icompression.NearLosslessCodec, enb.icompression.WrapperCodec):
    """Wrapper for the LZ4 codec
    All data types integer and float 16, 32, 64 can be compressed 
    """

    def __init__(self, lz4_binary=os.path.join(os.path.dirname(__file__), "lz4"), compression_level: int = 1, threads: int = 1):
        """
        :param compression_level: 1-12, being 1 the fastest execution and 12 the slowest one.
        :param threads: 1-N, being N the maximum system threads
        """
        assert (compression_level >= 1) and (compression_level <= 12), \
            f"The compression level must be an integer value between [1 and 12]"
        assert (threads >= 1) \
            f"Threads must be minimum 1"
        super().__init__(compressor_path=lz4_binary,
                         decompressor_path=lz4_binary,
                         param_dict=dict(compression_level=compression_level, threads=threads))

    @property
    def label(self):
        return f"LZ4 level {self.param_dict['compression_level']} threads {self.param_dict['threads']}"

    def get_compression_params(self, original_path, compressed_path, original_file_info):
        assert original_file_info["big_endian"] and not original_file_info["float"], \
            f"Only big-endian integer samples are currently supported by {self.__class__.__name__}"
        return f"-{self.param_dict['compression_level']} -T{self.param_dict['threads']} {original_path}  {compressed_path}"

    def get_decompression_params(self, compressed_path, reconstructed_path, original_file_info):
        return f"-d -{self.param_dict['compression_level']} -T{self.param_dict['threads']} {compressed_path} {reconstructed_path} "
