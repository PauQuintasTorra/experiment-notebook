#!/usr/bin/env python3
"""Codec wrapper for the HDF5 lossless image coder
"""
__author__ = "Òscar Maireles and Miguel Hernández-Cabronero"
__since__ = "2021/08/01"

import numpy as np
import enb
import h5py
import hdf5plugin
import tables
import blosc2
import blosc2_grok


class AbstractHdf5Codec(enb.icompression.LosslessCodec):
    NOSHUFFLE = 0
    BYTESHUFFLE = 1
    BITSHUFFLE = 2

    def __init__(self, shuffle=NOSHUFFLE, param_dict=None):
        assert self.NOSHUFFLE <= shuffle <= self.BITSHUFFLE

        param_dict = dict() if param_dict is None else param_dict
        param_dict["shuffle"] = shuffle
        super().__init__(param_dict=param_dict)

    def _compression(self, hdf5_file, dataset_name, image):
        raise NotImplementedError("Abstract method not implemented")

    def compress(self, original_path, compressed_path, original_file_info):
        with h5py.File(compressed_path, "w") as compressed_file:
            array = enb.isets.load_array_bsq(
                file_or_path=original_path, image_properties_row=original_file_info)
            
            self._compression(compressed_file, "dataset_1", array)

    def decompress(self, compressed_path, reconstructed_path, original_file_info=None):
        with h5py.File(f'{compressed_path}', 'r') as compressed_file, open(reconstructed_path,
                                                                            "wb") as reconstructed_file:
            compressed_file = compressed_file.get('dataset_1')
            compressed_file = np.array(compressed_file)

            enb.isets.dump_array_bsq(array=compressed_file, file_or_path=reconstructed_file)

class HDF5_GZIP(AbstractHdf5Codec):
    """Apply the Gzip algorithm and Huffman coding to the file using HDF5.
    """

    MIN_COMPRESSION_LEVEL = 1
    MAX_COMPRESSION_LEVEL = 9
    DEFAULT_COMPRESSION_LEVEL = 5

    def __init__(self, compression_level=DEFAULT_COMPRESSION_LEVEL, shuffle=0, param_dict=None):
        assert self.MIN_COMPRESSION_LEVEL <= compression_level <= self.MAX_COMPRESSION_LEVEL
        assert self.BITSHUFFLE != shuffle, "GZIP doesn't accept bitshuffle"
        
        param_dict = dict() if param_dict is None else param_dict
        param_dict["compression_level"] = compression_level
        super().__init__(shuffle=shuffle, param_dict=param_dict)

    def _compression(self, hdf5_file, dataset_name, image):
        hdf5_file.create_dataset(dataset_name, data=image, compression="gzip", compression_opts=self.param_dict["compression_level"], shuffle=self.param_dict["shuffle"])

    @property
    def label(self):
        return f"HDF5_GZIP"


class HDF5_LZF(AbstractHdf5Codec):
    """Apply the LZF algorithm using HDF5.
    """

    def __init__(self, shuffle=0, param_dict=None):
        assert self.BITSHUFFLE != shuffle, "LZF doesn't accept bitshuffle"

        super().__init__(shuffle=shuffle, param_dict=param_dict)

    def _compression(self, hdf5_file, dataset_name, image):
        hdf5_file.create_dataset(dataset_name, data=image, compression="lzf", shuffle=self.param_dict["shuffle"])

    @property
    def label(self):
        return f"HDF5_LZF"

class HDF5_ZSTD(AbstractHdf5Codec):
    """Apply the ZSTD algorithm using HDF5.
    """

    MIN_COMPRESSION_LEVEL = 1
    MAX_COMPRESSION_LEVEL = 22
    DEFAULT_COMPRESSION_LEVEL = 3

    def __init__(self, compression_level=DEFAULT_COMPRESSION_LEVEL, param_dict=None):
        assert self.MIN_COMPRESSION_LEVEL <= compression_level <= self.MAX_COMPRESSION_LEVEL
        
        param_dict = dict() if param_dict is None else param_dict
        param_dict["compression_level"] = compression_level
        super().__init__(param_dict=param_dict)

        self.param_dict["shuffle"] = None

    def _compression(self, hdf5_file, dataset_name, image):
        hdf5_file.create_dataset(dataset_name, data=image, compression=hdf5plugin.Zstd(clevel=self.param_dict["compression_level"]))

    @property
    def label(self):
        return f"HDF5_ZSTD"


class HDF5_LZ4(AbstractHdf5Codec):
    """Apply the LZ4 algorithm using HDF5.
    """

    MIN_N_BYTES = 0
    MAX_N_BYTES = 2113929216
    DEFAULT_N_BYTES = 0

    def __init__(self, nbytes=DEFAULT_N_BYTES, shuffle=0, param_dict=None):
        assert self.MIN_N_BYTES <= nbytes <= self.MAX_N_BYTES
        
        param_dict = dict() if param_dict is None else param_dict
        param_dict["n_bytes"] = nbytes
        super().__init__(shuffle=shuffle, param_dict=param_dict)


    def _compression(self, hdf5_file, dataset_name, image):
        hdf5_file.create_dataset(dataset_name, data=image, compression=hdf5plugin.LZ4(nbytes = self.param_dict["n_bytes"]))

    @property
    def label(self):
        return f"HDF5_LZ4"


class HDF5_SZIP(AbstractHdf5Codec):
    """Apply the SZIP algorithm using HDF5.
    """

    def _compression(self, hdf5_file, dataset_name, image):
        hdf5_file.create_dataset(dataset_name, data=image, compression="szip")

    @property
    def label(self):
        return f"HDF5_SZIP"

class HDF5_BLOSC(AbstractHdf5Codec):
    """Apply the BLOSC algorithm using HDF5.
    """
    MIN_COMPRESSION_LEVEL = 1
    MAX_COMPRESSION_LEVEL = 9
    DEFAULT_COMPRESSION_LEVEL = 5
    
    def __init__(self, cname, shuffle, compression_level=DEFAULT_COMPRESSION_LEVEL, param_dict=None):
        assert self.MIN_COMPRESSION_LEVEL <= compression_level <= self.MAX_COMPRESSION_LEVEL
        assert cname in ["blosclz", "lz4", "lz4hc", "zlib", "zstd"]

        param_dict = dict() if param_dict is None else param_dict
        param_dict["compression_level"] = compression_level
        param_dict["cname"] = cname
        super().__init__(shuffle=shuffle, param_dict=param_dict)
    
    def _compression(self, hdf5_file, dataset_name, image):
        hdf5_file.create_dataset(dataset_name, data=image, compression=hdf5plugin.Blosc(cname=self.param_dict["cname"], 
                                    clevel=self.param_dict["compression_level"], shuffle=self.param_dict["shuffle"]))

    @property
    def label(self):
        return f"HDF5_BLOSC"

class HDF5_BLOSC2(AbstractHdf5Codec):
    """Apply the BLOSC2 algorithm using HDF5.
    """
    MIN_COMPRESSION_LEVEL = 1
    MAX_COMPRESSION_LEVEL = 9
    DEFAULT_COMPRESSION_LEVEL = 5

    def __init__(self, cname, shuffle, compression_level=DEFAULT_COMPRESSION_LEVEL, param_dict=None):
        assert self.MIN_COMPRESSION_LEVEL <= compression_level <= self.MAX_COMPRESSION_LEVEL
        assert cname in ["blosclz", "lz4", "lz4hc", "zlib", "zstd", "grok"]

        param_dict = dict() if param_dict is None else param_dict
        param_dict["compression_level"] = compression_level
        param_dict["cname"] = cname
        super().__init__(shuffle=shuffle, param_dict=param_dict)
    
    def _compression(self, hdf5_file, dataset_name, image):
        hdf5_file.create_dataset(dataset_name, data=image, compression=hdf5plugin.Blosc2(cname=self.param_dict["cname"], 
                                    clevel=self.param_dict["compression_level"], shuffle=self.param_dict["shuffle"]))

    @property
    def label(self):
        return f"HDF5_BLOSC2"

class HDF5_GROK(AbstractHdf5Codec):
    """Apply the GROK algorithm using HDF5.
    """

    blosc2_grok.set_params_defaults(
        cod_format=blosc2_grok.GrkFileFmt.GRK_FMT_JP2
    )


    def __init__(self, param_dict=None):

        super().__init__(param_dict=param_dict)
    
    def _compression(self, hdf5_file, dataset_name, image):
        dataset = group.create_dataset(
            dataset_name,
            shape=image.shape,
            dtype=image.dtype,
            chunks=image.shape,
            allow_unknown_filter=True,
            compression=hdf5plugin.Blosc2(),
        )
        hdf5_file.id.write_direct_chunk((0,0,0),
            blosc2.asarray(
                image,
                chunks=image.shape,
                blocks=(1,) + image.shape[1:],
                cparams={
                    'codec': blosc2.Codec.GROK,
                    'filters': [],
                    'splitmode': blosc2.SplitMode.NEVER_SPLIT,
                },
            ).schunk.to_cframe()
        )
    @property
    def label(self):
        return f"HDF5_GROK"

class HDF5_BZIP2(enb.icompression.LosslessCodec):
    """Apply the BZIP2 algorithm using HDF5.
    """

    NOSHUFFLE = 0
    BYTESHUFFLE = 1

    MIN_COMPRESSION_LEVEL = 1
    MAX_COMPRESSION_LEVEL = 9
    DEFAULT_COMPRESSION_LEVEL = 6

    def __init__(self, compression_level=DEFAULT_COMPRESSION_LEVEL, shuffle=NOSHUFFLE, param_dict=None):
        assert self.NOSHUFFLE <= shuffle <= self.BYTESHUFFLE
        assert self.MIN_COMPRESSION_LEVEL <= compression_level <= self.MAX_COMPRESSION_LEVEL

        param_dict = dict() if param_dict is None else param_dict
        param_dict["shuffle"] = shuffle
        param_dict["clevel"] = compression_level

        super().__init__(param_dict=param_dict)

    def compress(self, original_path, compressed_path, original_file_info):
        with tables.open_file(compressed_path, "w") as compressed_file:
            array = enb.isets.load_array_bsq(
                file_or_path=original_path, image_properties_row=original_file_info)

            filters = tables.Filters(complevel=self.param_dict["clevel"], complib='bzip2', shuffle=self.param_dict["shuffle"])

            atom = tables.Atom.from_dtype(array.dtype)
            ds = compressed_file.create_carray(compressed_file.root, 'dataset_1', atom=atom, shape=array.shape, filters=filters)
            ds[:] = array.view(array.dtype.newbyteorder('='))

    def decompress(self, compressed_path, reconstructed_path, original_file_info=None):
        with tables.open_file(f'{compressed_path}', 'r') as compressed_file, open(reconstructed_path,
                                                                            "wb") as reconstructed_file:
            compressed_file = compressed_file.root.dataset_1[:]
            compressed_file = np.array(compressed_file)

            enb.isets.dump_array_bsq(array=compressed_file, file_or_path=reconstructed_file)
    
    @property
    def label(self):
        return f"HDF5_BZIP2"

class HDF5_BITSHUFFLE(enb.icompression.LosslessCodec):
    """Apply the BITSHUFFLE function using HDF5.
    """


    MIN_COMPRESSION_LEVEL = 1
    MAX_COMPRESSION_LEVEL = 22
    DEFAULT_COMPRESSION_LEVEL = 3

    def __init__(self, cname, compression_level = DEFAULT_COMPRESSION_LEVEL, param_dict=None):
        assert cname in ["lz4", "zstd"]
        assert self.MIN_COMPRESSION_LEVEL <= compression_level <= self.MAX_COMPRESSION_LEVEL

        param_dict = dict() if param_dict is None else param_dict
        param_dict["cname"] = cname
        param_dict["clevel"] = compression_level

        super().__init__(param_dict=param_dict)

    def compress(self, original_path, compressed_path, original_file_info):
        with h5py.File(compressed_path, "w") as compressed_file:
            array = enb.isets.load_array_bsq(
                file_or_path=original_path, image_properties_row=original_file_info)
            
            compressed_file.create_dataset("dataset_1", data=array, compression=hdf5plugin.Bitshuffle(cname=self.param_dict["cname"], clevel=self.param_dict["clevel"]))

    def decompress(self, compressed_path, reconstructed_path, original_file_info=None):
        with h5py.File(f'{compressed_path}', 'r') as compressed_file, open(reconstructed_path,
                                                                            "wb") as reconstructed_file:
            compressed_file = compressed_file.get('dataset_1')
            compressed_file = np.array(compressed_file)

            enb.isets.dump_array_bsq(array=compressed_file, file_or_path=reconstructed_file)
    
    @property
    def label(self):
        return f"HDF5_BITSHUFFLE"