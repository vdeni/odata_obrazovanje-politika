# Podaci

## Licence

Na datoteke u ovom direktoriju primjenjuje se
[CC0 licenca](http://creativecommons.org/publicdomain/zero/1.0/).

**Iznimke su**:
- *Imena i prezimena u Republici Hrvatskoj*: nisam dobio informaciju o
konkretnoj licenci, ali uputa je: "dostavljene podatke možete koristiti prema
svojim potrebama. Prilikom korištenja podataka obavezno je potrebno navesti
izvor podataka."
- *Leksička flektivna baza podataka hrvatskih imena i prezimena* podijeljena
je pod
[CC-BY-SA licencom](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
(vidi [izvor](http://meta-share.ffzg.hr/repository/browse/lexical-inflectional-database-of-croatian-first-and-last-names/11e503cc3d3f11e38a985ef2e4e6c59eaeb2fa3a711d40e7b740b9be76e2964c/)).

## Podaci

Linkovi na datoteke koje su dostupne drugdje mogu se naći u sekciji
[Makefile](##Makefile).

- `2011-popis_agregati-imena-prezimena/`
    - `2011-popis_agregati-imena-prezimena.xls`: popis učestalosti imena,
    prezimena, i parova (ime, prezime) iz popisa stanovništva 2011. Državni
    zavod za statistiku (2011). *Imena i prezimena u Republici Hrvatskoj*.
    Ovo su podaci u podlozi [ove](https://www.dzs.hr/app/imena/) aplikacije.
- `2021-lokalni-izbori_donacije/`
    - `donacije_lokalni.csv`: datoteka koja sadrži pojedinačne donacije
    kandidatima na lokalnim izborima 2021. godine. Delimiter je `;`. Svaki
    unos predstavlja jednu donaciju. Informacije o donatorima sadržane su
    u varijablama koje završavaju na `Indiv`; ostali podaci se odnose na
    kandidate. Ako kandidat nije primio niti jednu donaciju, varijable pod
    `Indiv` sadrže oznaku `NA`. Budući da ovaj objedinjeni CSV **nije
    službena baza** DIP-a, preporučujem da se koristi orijentacijski i
    da se unosi dodatno provjere u
    [službenim podacima](https://www.izbori.hr/lokalni2021/financ/1/).
    - `zupanije_kodovi.json`: datoteka s numeričkim kodovima županija. Kodovi
    su korišteni pri imenovanju datoteka s pojedinim izvještajima o donacijama.
    - [`bjelovarsko-bilogorska_županija/`,
    `brodsko-posavska_županija/`,
    `dubrovačko-neretvanska_županija/`,
    `grad_zagreb/`,
    `istarska_županija/`,
    `karlovačka_županija/`,
    `koprivničko-križevačka_županija/`,
    `krapinsko-zagorska_županija/`,
    `ličko-senjska_županija/`,
    `međimurska_županija/`,
    `osječko-baranjska_županija/`,
    `požeško-slavonska_županija/`,
    `primorsko-goranska_županija/`,
    `šibensko-kninska_županija/`,
    `sisačko-moslavačka_županija/`,
    `splitsko-dalmatinska_županija/`,
    `varaždinska_županija/`,
    `virovitičko-podravska_županija/`,
    `vukovarsko-srijemska_županija/`,
    `zadarska_županija/`,
    `zagrebačka_županija/`]
        - ovi folderi sadrže pojedine izvještaje o donacijama u JSON formatu.
        Podijeljeno po županijama. Imena JSON datoteka sadrže ime općine ili
        grada za koji su podaci preuzeti, te vrstu izbora
        (`gradona` = gradonačelnici i općinski načelnici, `gradsko` =
        gradska i općinska vijeća, `zamjeni` = zamjenici načelnika i župana,
        `župan` = župan, `županij` = županijska skupština). Sami kandidati
        kodirani su tek kroz numeričke oznake, ali za njih ne postoji
        datoteka s kodovima.
- `2021-lokalni-izbori_kandidature/`
    - popisi kandidata na lokalnim izborima preuzeti sa stranica Državnog
    izbornog povjerenstva. Delimiter je `;`.
    - `kandidature_nacelnici.csv`: kandidature za gradonačelnike, općinske
    načelnike i župane.
    - `kandidature_skupstine.csv`: kandidature za članove općinskih, gradskih
    i županijskih skupština.
    - `kandidature_zamjenici.csv`: kandidature za zamjenike gradonačelnika,
    općinskih načelnika i župana.
- `infleksijska-baza/`
    - `infleksijska-baza.csv`: Damir Boras, Nives Mikelić, Davor Lauc (2003).
    *Leksička flektivna baza podataka hrvatskih imena i prezimena*,
    pp. 219--236.
- `obrazovne-ustanove_popis_datagov/`
    - popisi odgojno-obrazovnih i znanstvenih ustanova u Republici Hrvatskoj
    preuzeti s data.gov.hr. Delimiter je `;` u CSV datotekama, i `\t` (tab) u
    TSV datotekama.
    - `popis_vrtici.csv`: popis vrtića
    - `popis_osnovne-skole.csv`: popis osnovnih škola
    - `popis_srednje-skole.csv`: popis srednjih škola
    - `popis_visoko-obrazovanje.csv`: popis ustanova iz sustava visokog
    obrazovanja
    - `popis_znanost.csv`: popis znanstvenih ustanova
    - `popis_osnovne-skole_kod-spolova.tsv`: tablice u kojima su kodirani
    spolovi rukovodećih osoba u osnovnim školama
    - `popis_srednje-skole_kod-spolova.tsv`: tablice u kojima su kodirani
    spolovi rukovodećih osoba u srednjim školama
- `obrazovne-ustanove_popis_mzos/`
    - popisi odgojno-obrazovnih i znanstvenih ustanova u Republici Hrvatskoj
    preuzeti sa stranica Ministarstva znanosti i obrazovanja.
    - `popis_vrtici.xlsx`: popis vrtića
    - `popis_osnovne-skole.xlsx`: popis osnovnih škola
    - `popis_srednje-skole.xlsx`: popis srednjih škola
    - `popis_umjetnicke-skole.xlsx`: popis umjetničkih škola
    - `popis_visoko-obrazovanje.xlsx`: popis ustanova iz sustava visokog
    obrazovanja
    - `popis_znanost.xlsx`: popis znanstvenih ustanova
- `obrazovne-ustanove_popis_scrape/`
    - popisi odgojno-obrazovnih ustanova u Republici Hrvatskoj scrapeani
    iz aplikacije na stranici Ministarstva znanosti i obrazovanja. Delimiter
    je `;`.
    - `popis_vrtici_scrape.csv`: popis vrtića
    - `popis_osnovne-skole_scrape.csv`: popis osnovnih škola
    - `popis_srednje-skole_scrape.csv`: popis srednjih škola
    - `popis_umjetnicke-skole_scrape.csv`: popis umjetničkih škola
    - `popis_visoko-obrazovanje_scrape.csv`: popis ustanova iz sustava visokog
    obrazovanja
    - `popis_znanost_scrape.csv`: popis znanstvenih ustanova

## Makefile

U folderu se nalazi `Makefile` koji služi za generiranje podataka.
Mogućnosti su:
- `make` za prikupljanje svih setova podataka (traje neko vrijeme jer se dio
podataka scrapea)

- `make obrazovne_ustanove_datagov`: za dohvaćanje popisa odgojno obrazovnih
ustanova s data.gov.hr u CSV formatu. linkovi:
    - popis_vrtici.csv: http://52.178.158.152/api/file/vrtici.csv
    - popis_osnovne-skole.csv: http://52.178.158.152/api/file/skole_os.csv
    - popis_srednje-skole.csv: http://52.178.158.152/api/file/srednje--skole.csv
    - popis_visoko-obrazovanje.csv: http://52.178.158.152/api/file/ustanove_vu.csv
    - popis_znanost.csv: http://52.178.158.152/api/file/ustanove_z.csv
- `make obrazovne_ustanove_scrape`: za dohvaćanje podataka na web sučelju za
baze podataka na stranicama Ministarstva znanosti i obrazovanja
(https://mzo.gov.hr/ustanove/103)
- `make obrazovne_ustanove_mzos`: za dohvaćanje XSLX datoteka sa stranica
Ministarstva znanosti i obrazovanja:
    - popis_vrtici.xlsx: http://mzos.hr/dbApp/DownloadExcel.ashx?appName=Vrtici
    - popis_osnovne-skole.xlsx: http://mzos.hr/dbApp/DownloadExcel.ashx?appName=OS
    - popis_umjetnicke-skole.xlsx: http://mzos.hr/dbApp/DownloadExcel.ashx?appName=UMJ
    - popis_visoko-obrazovanje.xlsx: http://mzos.hr/dbApp/DownloadExcel.ashx?appName=ustanove_VU
    - popis_znanost.xlsx: http://mzos.hr/dbApp/DownloadExcel.ashx?appName=ustanove_Z

- `make kandidature_lokalni`: za dohvaćanje popisa kandidata na lokalnim
izborima 2021.
linkovi:
    - kandidature_skupstine.csv: https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZS_GSGZ_GV_OV_03%2005%202021.xlsx
    - kandidature_nacelnici.csv: https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZN_GNGZ_GN_ON_03%2005%202021.xlsx
    - kandidature_zamjenici.csv: https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZZN_ZGN_ZON_03%2005%202021.xlsx

- `make donacije_lokalni`: za scrape JSON izvještaja o donacijama kandidatima
na lokalnim izborima 2021. sa stranica Državnog izbornog povjerenstva
(https://www.izbori.hr/lokalni2021/financ/1/). Oslanja se na dvije Python
skripte s potrebnim paketima popisanima u `/Pipfile`.
Skripte izbacuju CSV datoteku (`;` kao delimiter), u kojoj svaki red
predstavlja jednu donaciju za jednog kandidata. Pritom, i kandidati
koji nisu imali niti jednu donaciju imaju unos.
Varijable čija imena završavaju na `Indiv` sadrže podatke o donatorima i
donacijama. Ostale varijable se odnose na primatelje donacija. Dakle,
ako neki kandidat nije primio niti jednu donaciju, imat će unose u
varijablama koje ne završavaju na `Indiv`, a u varijablama koje završavaju
na `Indiv` (koje se, dakle, odnose na donatore) imat će vrijednost `NA`.

- `make infleksijska-baza`: za pretvaranje infleksijske baze u CSV datoteku.
Prethodno je potrebno preuzeti infleksijsku bazu [odavde](http://meta-share.ffzg.hr/repository/browse/lexical-inflectional-database-of-croatian-first-and-last-names/11e503cc3d3f11e38a985ef2e4e6c59eaeb2fa3a711d40e7b740b9be76e2964c/).
Izvorna baza ima neke trailing tabove, zbog čega sam imao problema s
učitavanjem baze. Zbog toga sam je pretvorio u CSV i uklonio trailing
tabove.

## Druge datoteke
- `lokalni-izbori_kandidature_process-xlsx.sh`: pomoćna skripta korištena pri preuzimanju
datoteka s kandidaturama
- `Makefile`: `make` naredbe za dohvaćanje ili izradu podataka

## Struktura direktorija

```
.
├── lokalni-izbori_kandidature_process-xlsx.sh
├── 2011-popis_agregati-imena-prezimena
│   └── 2011-popis_agregati-imena-prezimena.xls
├── 2021-lokalni-izbori_donacije
│   ├── bjelovarsko-bilogorska_županija
│   │   ├── 07_berek_gradona_0.json
│   │   ├── ...
│   │   └── 07_zrinski_topolovac_gradsko_2.json
│   ├── brodsko-posavska_županija
│   │   ├── 12_bebrina_gradona_0.json
│   │   ├── ...
│   │   └── 12_vrpolje_gradsko_2.json
│   ├── donacije_lokalni.csv
│   ├── dubrovačko-neretvanska_županija
│   │   ├── 19_blato_gradona_0.json
│   │   ├── ...
│   │   └── 19_župa_dubrovačka_gradsko_5.json
│   ├── grad_zagreb
│   │   ├── 21_grad_zagreb_gradona_0.json
│   │   ├── ...
│   │   └── 21_grad_zagreb_gradska_9.json
│   ├── istarska_županija
│   │   ├── 18_bale_-_valle_gradona_0.json
│   │   ├── ...
│   │   └── 18_žminj_gradsko_5.json
│   ├── karlovačka_županija
│   │   ├── 04_barilović_gradona_0.json
│   │   ├── ...
│   │   └── 04_žakanje_gradsko_2.json
│   ├── koprivničko-križevačka_županija
│   │   ├── 06_đelekovec_gradona_0.json
│   │   ├── ...
│   │   └── 06_virje_gradsko_3.json
│   ├── krapinsko-zagorska_županija
│   │   ├── 02_bedekovčina_gradona_0.json
│   │   ├── ...
│   │   └── 02_zlatar_gradsko_3.json
│   ├── ličko-senjska_županija
│   │   ├── 09_brinje_gradona_0.json
│   │   ├── ...
│   │   └── 09_vrhovine_gradsko_3.json
│   ├── međimurska_županija
│   │   ├── 20_belica_gradona_0.json
│   │   ├── ...
│   │   └── 20_vratišinec_gradsko_2.json
│   ├── osječko-baranjska_županija
│   │   ├── 14_antunovac_gradona_0.json
│   │   ├── ...
│   │   └── 14_vuka_gradsko_0.json
│   ├── požeško-slavonska_županija
│   │   ├── 11_brestovac_gradona_0.json
│   │   ├── ...
│   │   └── 11_velika_gradsko_4.json
│   ├── primorsko-goranska_županija
│   │   ├── 08_bakar_gradona_0.json
│   │   ├── ...
│   │   └── 08_vrbovsko_zamjeni_1.json
│   ├── šibensko-kninska_županija
│   │   ├── 15_bilice_gradona_0.json
│   │   ├── ...
│   │   └── 15_vodice_gradsko_4.json
│   ├── sisačko-moslavačka_županija
│   │   ├── 03_donji_kukuruzari_gradona_0.json
│   │   ├── ...
│   │   └── 03_velika_ludina_gradsko_4.json
│   ├── splitsko-dalmatinska_županija
│   │   ├── 17_baška_voda_gradona_0.json
│   │   ├── ...
│   │   └── 17_zmijavci_gradsko_4.json
│   ├── varaždinska_županija
│   │   ├── 05_bednja_gradona_0.json
│   │   ├── ...
│   │   └── 05_visoko_gradsko_1.json
│   ├── virovitičko-podravska_županija
│   │   ├── 10_čačinci_gradona_0.json
│   │   ├── ...
│   │   └── 10_zdenci_gradsko_3.json
│   ├── vukovarsko-srijemska_županija
│   │   ├── 16_andrijaševci_gradona_0.json
│   │   ├── ...
│   │   └── 16_županja_gradsko_6.json
│   ├── zadarska_županija
│   │   ├── 13_benkovac_gradona_0.json
│   │   ├── ...
│   │   └── 13_zemunik_donji_gradsko_1.json
│   ├── zagrebačka_županija
│   │   ├── 01_bedenica_gradona_0.json
│   │   ├── ...
│   │   └── 01_žumberak_gradsko_1.json
│   └── zupanije_kodovi.json
├── 2021-lokalni-izbori_kandidature
│   ├── kandidature_nacelnici.csv
│   ├── kandidature_skupstine.csv
│   └── kandidature_zamjenici.csv
├── infleksijska-baza
│   └── infleksijska-baza.csv
├── Makefile
├── obrazovne-ustanove_popis_datagov
│   ├── popis_osnovne-skole.csv
│   ├── popis_osnovne-skole_kod-spolova.tsv
│   ├── popis_srednje-skole.csv
│   ├── popis_srednje-skole_kod-spolova.tsv
│   ├── popis_visoko-obrazovanje.csv
│   ├── popis_vrtici.csv
│   └── popis_znanost.csv
├── obrazovne-ustanove_popis_mzos
│   ├── popis_osnovne-skole.xlsx
│   ├── popis_srednje-skole.xlsx
│   ├── popis_umjetnicke-skole.xlsx
│   ├── popis_visoko-obrazovanje.xlsx
│   ├── popis_vrtici.xlsx
│   └── popis_znanost.xlsx
├── obrazovne-ustanove_popis_scrape
│   ├── popis_osnovne-skole_scrape.csv
│   ├── popis_srednje-skole_scrape.csv
│   ├── popis_umjetnicke-skole_scrape.csv
│   ├── popis_visoko-obrazovanje_scrape.csv
│   ├── popis_vrtici_scrape.csv
│   └── popis_znanost_scrape.csv
└── README.md
```
