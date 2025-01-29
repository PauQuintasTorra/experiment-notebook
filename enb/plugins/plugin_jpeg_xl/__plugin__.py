import enb.plugins

class JPEGXLPlugin(enb.plugins.Plugin):
    name = "jpegxl"
    label = "Wrapper for a reference JPEG-XL implementation"
    tags = {"data compression", "image", "codec"}
    contrib_authors = ["See https://gitlab.com/wg1/jpeg-xl/-/blob/main/CONTRIBUTORS"]
    contrib_reference_urls = ["https://gitlab.com/wg1/jpeg-xl.git"]
    tested_on = {"linux"}
