import enb.plugins


class KakaduPluginHT(enb.plugins.Plugin):
    name = "kakadu"
    label = "Wrappers for Kakadu JPEG 2000 High Througput"
    contrib_authors = ["Kakadu Software Pty. Ltd."]
    contrib_reference_urls = ["https://kakadusoftware.com"]
    tags = {"data compression", "image", "codec", "privative"}
    tested_on = {"linux"}
