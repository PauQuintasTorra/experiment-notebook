import enb.plugins


class HDF5Plugin(enb.plugins.PluginMake):
    name = "hdf5"
    label = "Wrapper for a reference hdf5 implementation"
    tags = {"data compression", "image", "codec"}
    contrib_authors = ["HDF Group"]
    contrib_reference_urls = ["https://www.hdfgroup.org/download-hdf5/"]
    contrib_download_url_name = [
        ("https://github.com/PauQuintasTorra/experiment-notebook/blob/master/contrib/hdf5-1.14.6.zip?raw=true",
         "hdf5-1.14.6.zip")]

    tested_on = {"linux"}