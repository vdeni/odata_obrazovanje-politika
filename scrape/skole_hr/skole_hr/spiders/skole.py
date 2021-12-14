import re
import datetime

import pandas
import scrapy

from scrapy.loader import ItemLoader
from skole_hr.items import SkoleHrItem


# TODO: klasu za pretrazivanje popisa zaposlenika


class OsnovneSkoleSpider(scrapy.Spider):
    """
    Klasa za scrape informacija o djelatnicima osnovnih skola sa stranica pod
    domenom skole.hr
    """

    name = 'spider_skole-hr'

    allowed_domains = 'www.skole.hr'

    handle_httpstatus_list = [404]

    custom_settings = {
        'ITEM_PIPELINES': {
            'skole_hr.pipelines.SkoleHrPipeline': 300,
        }
    }

    def __init__(self,
                 link_db_path,
                 data_path,
                 path_404):
        self.url_db = pandas.read_csv(link_db_path,
                                      delimiter=';')

        self.url_db = self.url_db.dropna(axis=0,
                                         how='any',
                                         subset=['url'])

        self.url_db = self.url_db.reset_index(drop=True)

        self.data_path = data_path

        self.path_404 = path_404

        self.start_urls = self.url_db['url']

        self.start_urls = list(self.start_urls)

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
        print(f'>>> Parsing: {response.url}')

        _url_id = self.start_urls.index(response.url)

        print(f'\t>>> {_url_id} Ime: {self.url_db.loc[_url_id, "naziv"]}')

        if response.status == 404:
            print('\t>>> Added 404 url to list')

            with open(self.path_404,
                      'a') as ofile:
                ofile.write(response.url + '\n')

            return None

        loader = ItemLoader(item=SkoleHrItem(),
                            response=response)

        loader.add_xpath('scrape_tekst',
                         '//*/text()')

        loader.add_value('scrape_time',
                         datetime.datetime.now().astimezone().
                         replace(microsecond=0).isoformat())

        loader.add_value('skola_url',
                         response.url)

        loader.add_value('skola_naziv',
                         self.url_db.loc[_url_id, 'naziv'])

        loader.add_value('skola_zupanija',
                         self.url_db.loc[_url_id, 'zupanija'])

        loader.add_value('skola_mjesto',
                         self.url_db.loc[_url_id, 'mjesto'])

        return loader.load_item()
