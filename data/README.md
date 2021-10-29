# Podaci

U folderu se nalazi `Makefile` koji služi za generiranje podataka.
Mogućnosti su:
- `make obrazovne_ustanove` za dohvaćanje popisa odgojno obrazovnih ustanova s
data.gov.hr u CSV formatu. linkovi:
    - popis_vrtici.csv: http://52.178.158.152/api/file/vrtici.csv
    - popis_osnovne-skole.csv: http://52.178.158.152/api/file/skole_os.csv
    - popis_srednje-skole.csv: http://52.178.158.152/api/file/srednje--skole.csv
    - popis_visoko-obrazovanje.csv: http://52.178.158.152/api/file/ustanove_vu.csv
    - popis_znanost.csv: http://52.178.158.152/api/file/ustanove_z.csv
- `make kandidature_lokalni` za dohvaćanje popisa kandidata na lokalnim izborima 2021.
linkovi:
    - kandidature_skupstine.csv: https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZS_GSGZ_GV_OV_03%2005%202021.xlsx
    - kandidature_nacelnici.csv: https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZN_GNGZ_GN_ON_03%2005%202021.xlsx
    - kandidature_zamjenici.csv: https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZZN_ZGN_ZON_03%2005%202021.xlsx
