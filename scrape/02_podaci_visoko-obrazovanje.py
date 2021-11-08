# skripta za scrape podataka sa stranica MZOS o odgojno-obrazovnim ustanovama
# unutar hrvatske
import os
import re

import pandas
import _scrape_mzos_funs

# >>>>> setup
data_path = os.path.join('data',
                         'obrazovne-ustanove_popis_scrape')

# >>>>> linkovi
base_url = 'http://mzos.hr/dbApp/pregled.aspx?appName=ustanove_VU'

offset_list = list(range(30, 100, 30))

offset_url = [f'http://mzos.hr/dbApp/pregled.aspx?offset={off}&appName=ustanove_VU'
              for off in offset_list]

urls = [base_url] + offset_url

# >>>>> pandas
df = pandas.DataFrame(columns=['naziv',
                               'nadredjena_ustanova',
                               'vrsta_ustanove',
                               'tip_financiranja',
                               'upisnik',
                               'adresa',
                               'mjesto',
                               'telefon',
                               'faks',
                               'e_mail',
                               'web',
                               'celnik'])

# >>>>> scrape
re_id = re.compile('detalji\\.aspx\\?appName=ustanove_VU&amp;id=\\d+')

df = _scrape_mzos_funs.scrape_mzos(urls,
                                   df,
                                   re_id)

# >>>>> output
df.to_csv(os.path.join(data_path,
                       'popis_visoko-obrazovanje_scrape.csv'),
          sep=';',
          index=False,
          encoding='utf-8',
          na_rep='NA')
