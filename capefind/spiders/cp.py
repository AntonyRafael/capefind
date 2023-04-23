import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from time import sleep


class CpSpider(scrapy.Spider):
    name = "cp"
    # allowed_domains = ["www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br"]
    start_urls = ["https://capes-primo.ezl.periodicos.capes.gov.br/primo-explore/search?vid=CAPES_V3&lang=pt_BR&tab=default_tab&search_scope=default_scope&offset=0"]

    def __init__(self):
        # Configura as opções do Chrome para ser executado em modo headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
    
    def parse(self, response, **kwargs):
        termo_de_busca = getattr(self, 'termo_de_busca', 'python')
        
        # Abre a página usando o Selenium
        self.driver.get(response.url)

        # Espera até que a página seja totalmente carregada
        sleep(5)

        # Obtém o HTML da página usando o Selenium
        html = self.driver.page_source

        # Cria um objeto de resposta do Scrapy a partir do HTML obtido
        response = HtmlResponse(url=response.url, body=html, encoding='utf-8')

        form = response.css('form[name="search-form"]')
        input = form.css('input#searchBar')
        input.attrib['value'] = termo_de_busca
        
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'searchBar': termo_de_busca},
            callback=self.parse_results
        )

    def parse_results(self, response):
        sleep(5)
        # Obtém o HTML da página usando o Selenium
        html = self.driver.page_source
        print(html)
        f = open('arquivo.html', 'w')
        f.write(html)
        f.close()


        # Fecha o navegador
        self.driver.quit()
