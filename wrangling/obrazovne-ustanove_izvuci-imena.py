import os
import re

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

inflex_db = pandas.read_csv(os.path.join('data',
                                         'infleksijska-baza',
                                         'infleksijska-baza.csv'),
                            header=0,
                            names=['forma', 'lema', 'tag'])

imena_db =\
    pandas.read_excel(os.path.join('data',
                                   '2011-popis_agregati-imena-prezimena',
                                   '2011-popis_agregati-imena-prezimena.xls'),
                      sheet_name='AgregatIme')

# postavi NLP pipeline
nlp = classla.Pipeline('hr',
                       type='standard',
                       processors='tokenize,ner')

# napravi NER na unosima preuzetima s weba
d['tekst_ner'] = d.get('tekst').apply(helpers.apply_nlp_pipeline,
                                      pipeline=nlp)

# normaliziraj unose
# ukloni interpunkciju
re_punctuation = re.compile('[\'\'!\"#\\$%&\'()*+,-./:;<=>\\?@\\[\\]^_`{|}~]')

djelatnici = djelatnici.map(lambda x: re_punctuation.sub(repl=' ',
                                                         string=x))

# ukloni ponavljajuce razmake i razmake s pocetka i kraja
djelatnici = djelatnici.map(lambda x: x.strip())

djelatnici = djelatnici.map(lambda x: re.sub(pattern='\\s{2,}',
                                             repl=' ',
                                             string=x))

# TODO: filtriranje unosa u djelatnicima tako da se izbace pogresno
# prepoznati entiteti
