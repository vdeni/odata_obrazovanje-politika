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

#####
t = d.scrape_tekst[1]
doc = nlp(t[10])

_ = doc.get('ner', from_token=True)
[e.find('PER') for e in _]
#####

# napravi NER na unosima preuzetima s weba
d['tekst_ner'] = d.get('scrape_tekst').apply(helpers.apply_nlp_pipeline,
                                             pipeline=nlp)

# normaliziraj unose
d['tekst_ner'] = d.get('tekst_ner').map(helpers.normalize_inputs)

# TODO: filtriranje unosa u djelatnicima tako da se izbace pogresno
# prepoznati entiteti
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

imena_db = imena_db.dropna()

imena_db['Ime'] = imena_db.get('Ime').map(lambda x: x.title())
# imena_db['Ime'] = imena_db.loc[:, 'Ime'].map(lambda x: x.title())

prezimena_db =\
    pandas.read_excel(os.path.join('data',
                                   '2011-popis_agregati-imena-prezimena',
                                   '2011-popis_agregati-imena-prezimena.xls'),
                      sheet_name='AgregatPrezime')

prezimena_db = prezimena_db.dropna()

prezimena_db['Prezime'] = prezimena_db.loc[:, 'Prezime'].\
    map(lambda x: x.title())

d.tekst_ner.apply(helpers.filter_entries,
                  inflectional_set=set(inflex_db.lema.values),
                  names_set=set(imena_db.Ime.values),
                  lastnames_set=set(prezimena_db.Prezime.values))
