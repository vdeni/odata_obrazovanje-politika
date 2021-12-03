# skripta za scrape podataka sa stranica MZOS o odgojno-obrazovnim ustanovama
# unutar hrvatske
import os
import re

import pandas
import popis_mzos_helpers

# >>>>> setup
data_path = os.path.join('data',
                         'obrazovne-ustanove_popis_scrape')

# >>>>> linkovi
base_url = 'http://mzos.hr/dbApp/pregled.aspx?appName=OS'

offset_list = list(range(30, 900, 30))

offset_url = [f'http://mzos.hr/dbApp/pregled.aspx?offset={off}&appName=OS'
              for off in offset_list]

urls = [base_url] + offset_url

# >>>>> pandas
df = pandas.DataFrame(columns=['naziv',
                               'opis',
                               'tip_ustanove',
                               'maticna_skola',
                               'sifra',
                               'podsifra',
                               'zupanija',
                               'adresa',
                               'mjesto',
                               'lokacija',
                               'ravnatelj',
                               'telefon',
                               'faks',
                               'e_mail',
                               'web',
                               'podrucni_objekti'])

# >>>>> scrape
re_id = re.compile('detalji\\.aspx\\?appName=OS&amp;id=\\d+')

df = popis_mzos_helpers.scrape_mzos(urls,
                                    df,
                                    re_id)

# >>>>> output
df.to_csv(os.path.join(data_path,
                       'popis_osnovne-skole_scrape.csv'),
          sep=';',
          index=False,
          encoding='utf-8',
          na_rep='NA')
