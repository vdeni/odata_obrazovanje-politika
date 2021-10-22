import os
import json
import time

import requests

from selenium import webdriver

# postavi path za spremanje podataka
data_path = os.path.join('data',
                         '2021-lokalni-izbori_donacije')

# URL aplikacije za dohvacanje financijskih izvjestaja
base_url = 'https://www.izbori.hr/lokalni2021/financ/1/'

# postavi selenium webdriver
driver = webdriver.Firefox()

driver.get(base_url)

elem_zupanije = driver.\
    find_elements(by='xpath',
                  value='//select[@ng-model="zupanija"]/option[@label]')

# izvuci imena zupanija i napravi dict s kodovima
_ = [zup.text for zup in elem_zupanije]

kodovi_zupanije = zip(_,
                      [f'{x:02}' for x in range(1, len(_) + 1)])

kodovi_zupanije = dict(list(kodovi_zupanije))

with open(os.path.join(data_path,
                       'zupanije_kodovi.json'),
          'w+',
          encoding='utf-8') as outfile:
    json.dump(kodovi_zupanije,
              outfile)

# scrape
for zup in elem_zupanije[0:3]:
    print(f'\n======>> Prikupljam podatke za: {zup.text}\n')

    zup.click()

    time.sleep(2)

    # odabir gradova i opcina
    elem_grop = driver.\
        find_elements(by='xpath',
                      value='//select[@ng-model="grop"]/option[@label]')

    for grop in elem_grop:
        print(f'\n@@@@@@@@@@>> Prikupljam podatke za: {grop.text}')

        grop.click()

        time.sleep(2)

        # odabir vrste izbora
        elem_izbori = driver.\
            find_elements(by='xpath',
                          value='''//select[@ng-model="vrstaIzbora"]/
                                   option[@label]''')

        for izbori in elem_izbori:
            print(f'\t======>> Prikupljam podatke za: {izbori.text}')

            izbori.click()

            time.sleep(2)

            # odabir obveznika
            elem_obveznici = driver.\
                find_elements(by='xpath',
                              value='''//select[@ng-model="obveznik"]/
                                       option[@label]''')

            for obveznik in elem_obveznici:
                print(f'\t\t>>> Prikupljam podatke za: {obveznik.text}')

                obveznik.click()

                time.sleep(2)

                # nadji JSON
                donacije_json = driver.\
                    find_element(by='xpath',
                                 value='''//div[contains(text(),
                                       "IZ-D-IP")]/a[contains(text(),
                                       "json")]''').\
                    get_attribute('href')

                donacije_json = requests.get(donacije_json).text
