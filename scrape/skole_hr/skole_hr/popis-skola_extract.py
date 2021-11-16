import os
import re

import pandas

# otvori popis osnovnih skola
skole_os = pandas.read_csv(os.path.join('data',
                                        'obrazovne-ustanove_popis_scrape',
                                        'popis_osnovne-skole_scrape.csv'),
                           delimiter=';')

# odaberi samo relevantne stupce
skole_os = skole_os[['naziv',
                     'opis',
                     'sifra',
                     'podsifra',
                     'zupanija',
                     'mjesto',
                     'e_mail',
                     'web']]

# izvuci url iz 'web' stupca ako unutra postoji unos; ako ne, probaj ga izvuci
# iz 'e_mail'; u protivnom stavi NA
skole_os['url'] = pandas.NA

re_domain = re.compile(r'(^|\s+|\w+)(@)(os[-\w\.]+)')

for row_idx, row in skole_os.iterrows():
    if not pandas.isna(row.web):
        row.url = row.web
    elif not pandas.isna(row.e_mail):
        out_url = re_domain.search(row.e_mail)
        if out_url is not None:
            row.url = 'www.' + out_url.group(3)
        else:
            row.url = pandas.NA
    else:
        row.url = pandas.NA
    skole_os.loc[row_idx] = row

skole_os.to_csv(os.path.join('scrape',
                             'skole_hr',
                             'skole_hr',
                             'skole_osnovne_url.csv'),
                sep=';',
                index=False,
                encoding='utf-8',
                na_rep='NA')
