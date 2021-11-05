import re
import time

import bs4
import html5lib
import requests

import pandas


def scrape_mzos(urls: str,
                d_out: pandas.DataFrame,
                url_stem: str = 'http://mzos.hr/dbApp/',
                def_sleep: float = 1.5) -> pandas.DataFrame:
    re_id = re.compile('detalji\\.aspx\\?appName=Vrtici&amp;id=\\d+')

    for url_idx, url in enumerate(urls):
        print(f'{url_idx + 1} / {len(urls)}')

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

    d_out = d_out.replace('',
                          pandas.NA)

    return d_out
