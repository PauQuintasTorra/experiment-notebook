#!/usr/bin/env python3
"""Entropy plugin to get a dataset entropy
"""
__author__ = "Xavier Fernández-Mellado"
__since__ = "2021/06/01"

import os
import math
import json
import shutil
from enb import icompression


class Entropy(icompression.LosslessCodec):
    """Entropy plugin to get a dataset entropy
    """

    def __init__(self):
        super().__init__()

    def compress(self, original_path, compressed_path, original_file_info):
            size_bytes = original_file_info['size_bytes']
            bytes_per_sample = original_file_info['bytes_per_sample']

            assert bytes_per_sample in [1,2], "Entropy is only computed for 1 or 2 bps"

            if bytes_per_sample == 1:
                compressed_size = int(math.ceil(size_bytes * (original_file_info['entropy_1B_bps'] / 8)))
            else:
                compressed_size = int(math.ceil(size_bytes * (original_file_info['entropy_2B_bps'] / 16)))

            with open(compressed_path, 'wb') as f:
                f.write(b'\x00' * compressed_size)


            meta_path = compressed_path + '.meta.json'
            metadata = {
                'original_path': original_path,
            }
            with open(meta_path, 'w') as mf:
                json.dump(metadata, mf, indent=2)


    def decompress(self, compressed_path, reconstructed_path, original_file_info=None):
        meta_path = compressed_path + '.meta.json'

        if not os.path.exists(meta_path):
            raise FileNotFoundError(f"Metadata file not found: {compressed_path}")
        
        with open(meta_path, 'r') as mf:
            meta = json.load(mf)

        original_path = meta['original_path']
        
        if not os.path.exists(original_path):
            raise FileNotFoundError(f"Original file not found: {original_path}")

        shutil.copyfile(original_path, reconstructed_path)

        if os.path.exists(meta_path):
            os.remove(meta_path)

    @property
    def label(self):
        return "Entropy"
