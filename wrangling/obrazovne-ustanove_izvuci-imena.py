import os

import pandas
import classla

from importlib import import_module

helpers = import_module('wrangling.obrazovne-ustanove_izvuci-imena_helpers')

# ucitaj podatke
data_path = os.path.join('scrape',
                         'skole_hr',
                         'data',
                         'osnovne_skole.jl')

d = pandas.read_json(data_path,
                     lines=True)

# postavi NLP pipeline
nlp = classla.Pipeline('hr',
                       type='standard',
                       processors='tokenize,ner')

# standardiziraj crtice u tekstovima
d['tekst_dash_cleaned'] = d.get('scrape_tekst').map(helpers.dash_handler)

# napravi NER na unosima preuzetima s weba
d['tekst_ner'] = d.get('tekst_dash_cleaned').apply(helpers.apply_nlp_pipeline,
                                                   pipeline=nlp)

# filtriraj unose koji imaju samo jednu rijec
d['tekst_ner'] = d.get('tekst_ner').map(helpers.filter_entries)
