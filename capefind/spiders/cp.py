import scrapy


class CpSpider(scrapy.Spider):
    name = "cp"
    # allowed_domains = ["www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br"]
    start_urls = ["https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php"]

    def parse(self, response, **kwargs):
        pass
