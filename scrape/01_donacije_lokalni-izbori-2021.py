# import time

# import bs4
# import html5lib

from selenium import webdriver

# URL aplikacije za dohvacanje financijskih izvjestaja
base_url = 'https://www.izbori.hr/lokalni2021/financ/1/'

# postavi selenium webdriver
driver = webdriver.Firefox()

driver.get(base_url)

elem_zupanije = driver.\
    find_elements(by='xpath',
                  value='//select[@ng-model="zupanija"]/option[@label]')

for zup in elem_zupanije[0:3]:
    print(f'\n======>> Prikupljam podatke za: {zup.text}\n')

    # time.sleep(5)

    zup.click()

    # odabir gradova i opcina
    elem_grop = driver.\
        find_elements(by='xpath',
                      value='//select[@ng-model="grop"]/option[@label]')

    for grop in elem_grop:
        print(f'\n@@@@@@@@@@>> Prikupljam podatke za: {grop.text}')

        grop.click()

        # odabir vrste izbora
        elem_izbori = driver.\
            find_elements(by='xpath',
                          value='''//select[@ng-model="vrstaIzbora"]/
                                   option[@label]''')

        for izbori in elem_izbori:
            print(f'\t============>> Prikupljame podatke za: {izbori.text}')

            izbori.click()

            # odabir obveznika
            elem_obveznici = driver.\
                find_elements(by='xpath',
                              value='''//select[@ng-model="obveznik"]/
                                       option[@label]''')

            for obveznik in elem_obveznici:
                print(f'\t\t>>>>>>>>>> Prikupljam podatke za: {obveznik.text}')

                obveznik.click()
