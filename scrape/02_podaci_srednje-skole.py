# skripta za scrape podataka sa stranica MZOS o odgojno-obrazovnim ustanovama
# unutar hrvatske
import os
import re

import pandas
import _scrape_mzos_funs

# >>>>> setup
data_path = os.path.join('data',
                         'scrape_obrazovne-ustanove_popis')

# >>>>> linkovi
base_url = 'http://mzos.hr/dbApp/pregled.aspx?appName=SS'

offset_list = list(range(30, 420, 30))

offset_url = [f'http://mzos.hr/dbApp/pregled.aspx?offset={off}&appName=SS'
              for off in offset_list]

urls = [base_url] + offset_url

# >>>>> pandas
df = pandas.DataFrame(columns=['naziv',
                               'opis',
                               'sifra',
                               'zupanija',
                               'adresa',
                               'mjesto',
                               'lokacija',
                               'ravnatelj',
                               'telefon',
                               'faks',
                               'e_mail',
                               'web'])

# >>>>> scrape
re_id = re.compile('detalji\\.aspx\\?appName=SS&amp;id=\\d+')

df = _scrape_mzos_funs.scrape_mzos(urls,
                                   df,
                                   re_id)

# >>>>> output
df.to_csv(os.path.join(data_path,
                       'popis_srednje-skole_scrape.csv'),
          sep=';',
          index=False,
          encoding='utf-8',
          na_rep='NA')
