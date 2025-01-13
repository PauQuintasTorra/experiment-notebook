import enb.plugins


class LZ4Plugin(enb.plugins.PluginMake):
    name = "lz4"
    label = "Wrapper for a LZ4 codec"
    tags = {"data compression", "codec"}
    contrib_authors = ["Yann Collet"]
    contrib_reference_urls = ["https://lz4.github.io/lz4/"]
    contrib_download_url_name = [
        ("https://github.com/PauQuintasTorra/experiment-notebook/blob/master/contrib/lz4-1.10.0.zip?raw=true",
         "lz4-1.10.0.zip")]
    tested_on = {"linux"}
