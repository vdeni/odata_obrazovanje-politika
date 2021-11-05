# skripta za scrape podataka sa stranica MZOS o odgojno-obrazovnim ustanovama
# unutar hrvatske
import re
import time

import bs4
import html5lib
import requests

import pandas

# >>>>> setup
def_sleep = 1.5

# >>>>> linkovi
base_url = 'http://mzos.hr/dbApp/pregled.aspx?appName=Vrtici'

offset_list = list(range(30, 871, 30))

offset_url = [f'http://mzos.hr/dbApp/pregled.aspx?offset={off}&appName=Vrtici'
              for off in offset_list]

urls = [base_url] + offset_url

url_stem = 'http://mzos.hr/dbApp/'

# >>>>> regex
# link na unos ustanove u bazi
re_id = re.compile('detalji\\.aspx\\?appName=Vrtici&amp;id=\\d+')

# >>>>> pandas
d_out = pandas.DataFrame(columns=['naziv',
                                  'osnivac',
                                  'zupanija',
                                  'adresa',
                                  'mjesto',
                                  'telefon',
                                  'e_mail',
                                  'podrucni_objekti'])

# >>>>> scrape
for url in urls:
    site = bs4.BeautifulSoup(requests.get(url).text,
                             'html5lib')

    # nadji unose u tablici
    elem_tr = site.find_all('tr',
                            onclick=True)

    for entry_idx, entry in enumerate(elem_tr):
        entry_loc = re_id.search(str(entry))[0]

        entry_loc = re.sub('&amp;',
                           '&',
                           url_stem + entry_loc)

        db_entry = bs4.BeautifulSoup(requests.get(entry_loc).text,
                                     'html5lib')

        elem_db_tr = db_entry.find_all('tr')

        df_input = [elem.findChildren()[1].text for elem in elem_db_tr]

        d_out.loc[entry_idx] = df_input

    time.sleep(def_sleep)
