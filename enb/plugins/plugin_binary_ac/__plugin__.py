import enb.plugins


class BinaryACPlguin(enb.plugins.PluginMake):
    name = "binary_ac"
    label = "Wrapper for a Binary ArithmeticCoder implementation"
    tags = {"data compression", "image", "codec"}
    contrib_authors = ["Pau Quintas-Torra", "Xavier Fernandez-Mellado"]
    contrib_download_url_name = [
        ("https://github.com/PauQuintasTorra/experiment-notebook/blob/master/contrib/binary-entropy-coder.zip?raw=true",
         "binary-entropy-coder.zip")]

    tested_on = {"macos","linux"}