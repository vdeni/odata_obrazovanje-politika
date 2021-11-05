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
base_url = 'http://mzos.hr/dbApp/pregled.aspx?appName=ustanove_Z'

offset_list = list(range(30, 150, 30))

offset_url = [f'http://mzos.hr/dbApp/pregled.aspx?offset={off}&appName=ustanove_Z'
              for off in offset_list]

urls = [base_url] + offset_url

# >>>>> pandas
df = pandas.DataFrame(columns=['naziv',
                               'nadredjena_ustanova',
                               'vrsta_ustanove',
                               'upisnik',
                               'adresa',
                               'mjesto',
                               'telefon',
                               'faks',
                               'e_mail',
                               'web',
                               'celnik'])

# >>>>> scrape
re_id = re.compile('detalji\\.aspx\\?appName=ustanove_Z&amp;id=\\d+')

df = _scrape_mzos_funs.scrape_mzos(urls,
                                   df,
                                   re_id)

# >>>>> output
df.to_csv(os.path.join(data_path,
                       'popis_znanost_scrape.csv'),
          sep=';',
          index=False,
          encoding='utf-8',
          na_rep='NA')
