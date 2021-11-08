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
base_url = 'http://mzos.hr/dbApp/pregled.aspx?appName=Vrtici'

offset_list = list(range(30, 871, 30))

offset_url = [f'http://mzos.hr/dbApp/pregled.aspx?offset={off}&appName=Vrtici'
              for off in offset_list]

urls = [base_url] + offset_url

# >>>>> pandas
df = pandas.DataFrame(columns=['naziv',
                               'osnivac',
                               'zupanija',
                               'adresa',
                               'mjesto',
                               'telefon',
                               'e_mail',
                               'podrucni_objekti'])

# >>>>> scrape
re_id = re.compile('detalji\\.aspx\\?appName=Vrtici&amp;id=\\d+')

df = _scrape_mzos_funs.scrape_mzos(urls,
                                   df,
                                   re_id)

# >>>>> output
df.to_csv(os.path.join(data_path,
                       'popis_vrtici_scrape.csv'),
          sep=';',
          index=False,
          encoding='utf-8',
          na_rep='NA')
