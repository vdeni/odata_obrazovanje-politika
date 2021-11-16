import os

import pandas
import scrapy


class OsnovneSkoleSpider(scrapy.Spider):
    """
    Klasa za scrape informacija o djelatnicima osnovnih skola sa stranica pod
    domenom skole.hr
    """

    name = 'spider_os_skole-hr'

    allowed_domains = 'www.skole.hr'

    custom_settings = {
        'LOG_FILE': 'log_spider_os_skole-hr.txt'
    }

    def __init__(self):
        _ = pandas.read_csv(os.path.join('skole_hr',
                                         'skole_osnovne_url.csv'),
                            delimiter=';')

        self.start_urls = list(_['url'])[0:25]

        self.start_urls = [url.strip() for url in self.start_urls]

        self.start_urls = [url if url.startswith('http')
                           else 'http://' + url
                           for url in self.start_urls]

    def parse(self,
              response):
        self.logger.info(f'>>> Parsing: {response.url}')
