
import os
from enb import icompression
from enb.config import get_options

options = get_options()

class HEVC_H265_lossless(icompression.WrapperCodec, icompression.LosslessCodec):
    def __init__(self, config_path, geometry=400):
        icompression.WrapperCodec.__init__(
            self,
            compressor_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "TAppEncoderStatic"),
            decompressor_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "TAppDecoderStatic"),
            param_dict=None, output_invocation_dir=None)
        self.config_path = config_path
        self.param_dict['geometry'] = geometry

    def get_compression_params(self, original_path, compressed_path, original_file_info):
        return f"-i {original_path} -c {self.config_path} -b {compressed_path} -wdt {original_file_info['width']} " \
               f"-hgt {original_file_info['height']} -f {original_file_info['component_count']} " \
               f"-cf {self.param_dict['geometry']} --InputChromaFormat={self.param_dict['geometry']} " \
               f"--InputBitDepth={8*original_file_info['bytes_per_sample']} -fr 1"

    def get_decompression_params(self, compressed_path, reconstructed_path, original_file_info):
        return f"-b {compressed_path} -o {reconstructed_path} -d {8*original_file_info['bytes_per_sample']}"

    @property
    def label(self):
        return "HEVC H265 lossless"


class HEVC_H265_lossy(icompression.WrapperCodec, icompression.LossyCodec):
    def __init__(self, config_path, geometry=400):
        icompression.WrapperCodec.__init__(
            self,
            compressor_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "TAppEncoderStatic"),
            decompressor_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "TAppDecoderStatic"),
            param_dict=None, output_invocation_dir=None)
        self.config_path = config_path
        self.param_dict['geometry'] = geometry

    def get_compression_params(self, original_path, compressed_path, original_file_info):
        return f"-i {original_path} -c {self.config_path} -b {compressed_path} -wdt {original_file_info['width']} " \
               f"-hgt {original_file_info['height']} -f {original_file_info['component_count']} " \
               f"-cf {self.param_dict['geometry']} --InputChromaFormat={self.param_dict['geometry']} " \
               f"--InputBitDepth={8*original_file_info['bytes_per_sample']} -fr 1" \
               f"--InternalBitDepth={8*original_file_info['bytes_per_sample']}"

    def get_decompression_params(self, compressed_path, reconstructed_path, original_file_info):
        return f"-b {compressed_path} -o {reconstructed_path} -d {8*original_file_info['bytes_per_sample']}"

    @property
    def label(self):
        return "HEVC H265 lossy"
