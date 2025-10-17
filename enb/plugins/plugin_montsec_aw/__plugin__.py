import enb.plugins


class MontsecAWPlugin(enb.plugins.plugin.PluginMake):
    name = "montsecAW"
    label = "Wrapper for the Adaptative Words montsec codec"
    tags = {"data compression", "image", "codec"}
    authors = ["Pau Quintas Torra", "Xavier Fernandez Mellado"]
    contrib_authors = ["Group on Interactive Coding of Images (GICI)"]
    contrib_download_url_name = [
    ("https://github.com/PauQuintasTorra/experiment-notebook/blob/master/contrib/montsecAW.zip?raw=true",
        "montsecAW.zip")]
    tested_on = {"linux", "macos"}
