import os
import re
import json
import string

from itemadapter import ItemAdapter


class SkoleHrPipeline:
    # regex za filtriranje polja koja su samo whitespace
    re_only_whitespace = re.compile(f'^[{string.whitespace}]+$')

    # regex za skresati whitespace oko teksta
    re_rm_whitespace = re.compile(f'({string.whitespace}|\xa0)+')

    def open_spider(self, spider):
        os.makedirs('data',
                    exist_ok=True)

        self.file = open(os.path.join('data',
                                      'osnovne_skole.jl'),
                         'w+')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # filtriraj HTML elemente koji sadrze samo praznine
        adapter['tekst'] = [elem for elem in adapter.get('tekst')
                            if not self.re_only_whitespace.search(elem)]

        # zamijeni razni whitespace obicnim razmakom \s
        adapter['tekst'] = [self.re_rm_whitespace.sub(string=elem,
                                                      repl=' ')
                            for elem in adapter.get('tekst')]

        line_out = json.dumps(adapter.asdict()) + '\n'

        self.file.write(line_out)

        return item
