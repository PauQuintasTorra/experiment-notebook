#!/usr/bin/env python3
"""Codec wrapper for the Astronomy image coder
"""
__author__ = "Pau Quintas-Torra, Xavier Fernandez-Mellado"
__since__ = "2025/04/12"

import numpy as np
import enb
import os

class Astronomy(enb.icompression.LosslessCodec):

    def __init__(self, binary=os.path.join(os.path.dirname(__file__), "compressor"), cm=4, weights=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,333,333,0,0,0,0,0,334]):
        assert 0 <= cm <= 4
        assert len(weights) == 32
        assert sum(weights) == 1000

        param_dict = dict() if param_dict is None else param_dict
        param_dict["cm"] = cm
        param_dict["w"] = weights
        super().__init__(compressor_path=binary, decompressor_path=binary, param_dict=param_dict)

    @property
    def label(self):
        return ("Astronomy"
                + (" no context" if self.param_dict['cm'] == 0 else "")
                + (" H context" if self.param_dict['cm'] == 1 else "")
                + (" V context" if self.param_dict['cm'] == 2 else "")
                + (" HVD context" if self.param_dict['cm'] == 3 else "")
                + (" WEIGHTS " + str(self.param_dict["w"])))

    def get_compression_params(self, original_path, compressed_path, original_file_info):
        return f"cmp {original_path} {compressed_path} {self.param_dict['cm']} {','.join(map(str, lst))} "

    def get_decompression_params(self, compressed_path, reconstructed_path, original_file_info):
        return f"dec {compressed_path} {reconstructed_path} {self.param_dict['cm']} {','.join(map(str, lst))} "

