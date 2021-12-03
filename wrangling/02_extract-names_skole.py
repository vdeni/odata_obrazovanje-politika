import os
import re

import pandas
import classla

# ucitaj podatke
data_path = os.path.join('scrape',
                         'skole_hr',
                         'data',
                         'osnovne_skole.jl')

d = pandas.read_json(data_path,
                     lines=True)

t = d.at[1, 'tekst']

# postavi NLP pipeline
nlp = classla.Pipeline('hr',
                       processors='tokenize,ner')

# inicijaliziraj series za spremanje podataka
djelatnici = pandas.Series(name='djelatnici',
                           dtype='string')

# iteriraj kroz unose za svaku skolu i izvuci samo one koji su prepoznati kao
# PERSON u CLASSLA NER
for entry_idx, entry in enumerate(t):
    try:
        doc = nlp(entry)

        for ent in doc.entities:
            if ent.type == 'PER':
                djelatnici.loc[entry_idx] = ent.text
    except IndexError:
        continue

djelatnici = djelatnici.reset_index(drop=True)

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
# prepoznati entiteti. izbacuje unose koji sadrze samo jednu rijec. izbacuje
# unose dulje od sest rijeci. za ostale provjerava nalazi li se bilo koji od
# elemenata unosa u infleksijskoj bazi ili u popisu imena DZS
