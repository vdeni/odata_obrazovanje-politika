import os
import json
import time

import requests

from selenium import webdriver

# >>>>> setup
# postavi path za spremanje podataka
data_path = os.path.join('data',
                         '2021-lokalni-izbori_donacije')

# default sleep
def_sleep = 1.5

# URL aplikacije za dohvacanje financijskih izvjestaja
base_url = 'https://www.izbori.hr/lokalni2021/financ/1/'

# postavi selenium webdriver
driver = webdriver.Firefox()

driver.get(base_url)

elem_zupanije = driver.\
    find_elements(by='xpath',
                  value='//select[@ng-model="zupanija"]/option[@label]')

# ucitaj kodove zupanija
with open(os.path.join(data_path,
                       'zupanije_kodovi.json'),
          'r') as infile:
    kodovi_zupanije = json.load(infile)

counter_zupanije = dict()

# >>>>> scrape
for zup_id, zup in enumerate(elem_zupanije[0:1]):
    print(f'\n===>> {zup_id} / 21 _ Prikupljam podatke za: {zup.text}\n')

    zup.click()

    time.sleep(def_sleep)

    # napravi folder za spremanje datoteka
    folder_name = zup.text.lower().replace(' ',
                                           '_')

    os.makedirs(os.path.join(data_path,
                             folder_name),
                exist_ok=True)

    # odabir gradova i opcina
    elem_grop = driver.\
        find_elements(by='xpath',
                      value='//select[@ng-model="grop"]/option[@label]')

    for grop_id, grop in enumerate(elem_grop):
        print(f'\n======>> Prikupljam podatke za: {grop.text}')

        grop.click()

        time.sleep(def_sleep)

        # odabir vrste izbora
        elem_izbori = driver.\
            find_elements(by='xpath',
                          value='//select[@ng-model="vrstaIzbora"]/\
                                 option[@label]')

        for izbori in elem_izbori:
            print(f'\t>>> Prikupljam podatke za: {izbori.text}')

            if izbori.text.startswith('ŽUPAN'):
                if zup.text in counter_zupanije and\
                        izbori.text in counter_zupanije[zup.text]:
                    print('\nPreskačem.\n')
                    continue
                elif zup.text in counter_zupanije and\
                        izbori.text not in counter_zupanije[zup.text]:
                    counter_zupanije[zup.text] += [izbori.text]
                elif zup.text not in counter_zupanije:
                    counter_zupanije[zup.text] = [izbori.text]

            izbori.click()

            time.sleep(def_sleep)

            # odabir obveznika
            elem_obveznici = driver.\
                find_elements(by='xpath',
                              value='//select[@ng-model="obveznik"]/\
                                     option[@label]')

            for obveznik_id, obveznik in enumerate(elem_obveznici):
                print(f'\t\t>>> Prikupljam podatke za: {obveznik.text}')

                obveznik.click()

                time.sleep(def_sleep)

                # nadji JSON
                donacije_json = driver.\
                    find_element(by='xpath',
                                 value='//div[contains(text(),\
                                        "IZ-D-IP")]/a[contains(text(),\
                                        "json")]').\
                    get_attribute('href')

                donacije_json = requests.get(donacije_json).json()

                donacije_json.update([('izbori', izbori.text),
                                      ('mjesto', grop.text),
                                      ('zupanija', zup.text)])

                file_name = '_'.join([kodovi_zupanije[zup.text],
                                      grop.text.lower().replace(' ',
                                                                '_'),
                                      izbori.text.lower()[0:7],
                                      str(obveznik_id)]) + '.json'

                with open(os.path.join(data_path,
                                       folder_name,
                                       file_name),
                          'w+') as outfile:
                    json.dump(donacije_json,
                              outfile)
