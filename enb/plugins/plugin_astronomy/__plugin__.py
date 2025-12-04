import enb.plugins


class AstronomyPlugin(enb.plugins.PluginMake):
    name = "astronomy"
    label = "Wrapper for a astronomy compressor implementation"
    tags = {"data compression", "image", "codec"}
    contrib_authors = ["Pau Quintas-Torra", "Xavier Fernandez-Mellado"]
    contrib_download_url_name = [
        ("https://github.com/PauQuintasTorra/experiment-notebook/blob/master/contrib/Astronomy-Compressor.zip?raw=true",
         "Astronomy-Compressor.zip")]

    tested_on = {"macos","linux"}