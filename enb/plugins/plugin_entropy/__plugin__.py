import enb.plugins


class EntropyPlugin(enb.plugins.Plugin):
    name = "entropy"
    label = "Entropy Plugin (8 and 16 bits)"
    tags = {"data compression", "codec"}
    tested_on = {"linux"}
