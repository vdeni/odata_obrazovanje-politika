import os
import re
import json
import string

from itemadapter import ItemAdapter


class SkoleHrPipeline:
    # regex za filtriranje polja koja su samo whitespace
    re_only_whitespace = re.compile(f'^[{string.whitespace}]+$')

    # regex za skresati whitespace oko teksta
    re_any_whitespace = re.compile(f'[({string.whitespace}\xa0)]+')

    def open_spider(self, spider):
        os.makedirs('data',
                    exist_ok=True)

        self.file = open(spider.data_path,
                         'a')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # filtriraj HTML elemente koji sadrze samo praznine
        adapter['scrape_tekst'] = [elem for elem in adapter.get('scrape_tekst')
                                   if not self.re_only_whitespace.search(elem)]

        # zamijeni razni whitespace obicnim razmakom \s
        adapter['scrape_tekst'] = [self.re_any_whitespace.sub(string=elem,
                                                              repl=' ')
                                   for elem in adapter.get('scrape_tekst')]

        adapter['scrape_tekst'] = [elem.strip()
                                   for elem in adapter.get('scrape_tekst')]

        line_out = json.dumps(adapter.asdict()) + '\n'

        self.file.write(line_out)

        return item
