import os
import re

import pandas
import scrapy

from scrapy.loader import ItemLoader
from skole_hr.items import SkoleHrItem


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

        self.start_urls = list(_['url'])[0:5]

        self.start_urls = [url.strip() for url in self.start_urls]

        for url_idx, url in enumerate(self.start_urls):
            _ = re.search(r'((https?://)?(www\.)?)([-\w]*\.skole\.hr)',
                          url)
            if _ is not None:
                self.start_urls[url_idx] = _.group()

        self.start_urls = [url if url.startswith('http')
                           else 'http://' + url
                           for url in self.start_urls]

        self.start_urls = [url + 'skola/djelatnici' if url.endswith('/')
                           else url + '/skola/djelatnici'
                           for url in self.start_urls]

    def parse(self,
              response):
        self.logger.info(f'>>> Parsing: {response.url}')

        loader = ItemLoader(item=SkoleHrItem(),
                            response=response)

        loader.add_xpath('tekst',
                         '//*/text()')
        loader.add_value('skola_url',
                         response.url)

        return loader.load_item()
