#!/usr/bin/env python3
"""Codec wrapper for the Binary AC image coder
"""
__author__ = "Pau Quintas-Torra, Xavier Fernandez-Mellado"
__since__ = "2025/04/12"

import numpy as np
import enb
import os

class BinaryAC(enb.icompression.LosslessCodec, enb.icompression.WrapperCodec):

    def __init__(self, binary=os.path.join(os.path.dirname(__file__), "arithmetic"), cm=4):
        assert 0 <= cm <= 4

        param_dict = dict()
        param_dict["cm"] = cm
        super().__init__(compressor_path=binary, decompressor_path=binary, param_dict=param_dict)

    @property
    def label(self):
        return ("Binary AC"
                + (" no context" if self.param_dict['cm'] == 0 else "")
                + (" H context" if self.param_dict['cm'] == 1 else "")
                + (" V context" if self.param_dict['cm'] == 2 else "")
                + (" HVD context" if self.param_dict['cm'] == 3 else ""))

    def get_compression_params(self, original_path, compressed_path, original_file_info):
        return f"cmp {original_path} {compressed_path} {self.param_dict['cm']}"

    def get_decompression_params(self, compressed_path, reconstructed_path, original_file_info):
        return f"dec {compressed_path} {reconstructed_path} {self.param_dict['cm']}"

