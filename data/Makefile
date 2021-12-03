# >>>>> varijable
DIR_OB_USTANOVE_DATAGOV=obrazovne-ustanove_popis_datagov
DIR_OB_USTANOVE_MZOS=obrazovne-ustanove_popis_mzos
DIR_OB_USTANOVE_SCRAPE=obrazovne-ustanove_popis_scrape
DIR_KANDIDATURE=2021-lokalni-izbori_kandidature
DIR_DONACIJE=2021-lokalni-izbori_donacije
DIR_IMENA=infleksijska-baza

.PHONY:\
	all\
	obrazovne_ustanove_datagov\
	obrazovne_ustanove_mzos\
	obrazovne_ustanove_scrape\
	kandidature_lokalni\
	donacije_lokalni\
	infleksijska_baza

# >>>>> recepti
## >>>>> apstraktni
all:\
	obrazovne_ustanove_datagov\
	obrazovne_ustanove_mzos\
	obrazovne_ustanove_scrape\
	kandidature_lokalni\
	donacije_lokalni\
	infleksijska_baza

obrazovne_ustanove_datagov:\
	$(DIR_OB_USTANOVE_DATAGOV)/popis_vrtici.csv\
	$(DIR_OB_USTANOVE_DATAGOV)/popis_osnovne-skole.csv\
	$(DIR_OB_USTANOVE_DATAGOV)/popis_srednje-skole.csv\
	$(DIR_OB_USTANOVE_DATAGOV)/popis_visoko-obrazovanje.csv\
	$(DIR_OB_USTANOVE_DATAGOV)/popis_znanost.csv

obrazovne_ustanove_mzos:\
	$(DIR_OB_USTANOVE_MZOS)/popis_vrtici.xlsx\
	$(DIR_OB_USTANOVE_MZOS)/popis_osnovne-skole.xlsx\
	$(DIR_OB_USTANOVE_MZOS)/popis_srednje-skole.xlsx\
	$(DIR_OB_USTANOVE_MZOS)/popis_umjetnicke-skole.xlsx\
	$(DIR_OB_USTANOVE_MZOS)/popis_visoko-obrazovanje.xlsx\
	$(DIR_OB_USTANOVE_MZOS)/popis_znanost.xlsx

obrazovne_ustanove_scrape:\
	$(DIR_OB_USTANOVE_SCRAPE)/popis_vrtici_scrape.csv\
	$(DIR_OB_USTANOVE_SCRAPE)/popis_osnovne-skole_scrape.csv\
	$(DIR_OB_USTANOVE_SCRAPE)/popis_srednje-skole_scrape.csv\
	$(DIR_OB_USTANOVE_SCRAPE)/popis_umjetnicke-skole_scrape.csv\
	$(DIR_OB_USTANOVE_SCRAPE)/popis_visoko-obrazovanje_scrape.csv\
	$(DIR_OB_USTANOVE_SCRAPE)/popis_znanost_scrape.csv

kandidature_lokalni:\
	$(DIR_KANDIDATURE)/kandidature_zamjenici.csv\
	$(DIR_KANDIDATURE)/kandidature_skupstine.csv\
	$(DIR_KANDIDATURE)/kandidature_nacelnici.csv

donacije_lokalni:\
	$(DIR_DONACIJE)/donacije_lokalni.csv

infleksijska_baza:\
	$(DIR_IMENA)/infleksijska-baza.csv

## >>>>> obrazovne ustanove s datagov
$(DIR_OB_USTANOVE_DATAGOV)/popis_vrtici.csv:
	wget http://52.178.158.152/api/file/vrtici.csv
	mkdir -p $(DIR_OB_USTANOVE_DATAGOV)
	mv vrtici.csv $@

$(DIR_OB_USTANOVE_DATAGOV)/popis_osnovne-skole.csv:
	wget http://52.178.158.152/api/file/skole_os.csv
	mkdir -p $(DIR_OB_USTANOVE_DATAGOV)
	mv skole_os.csv $@

$(DIR_OB_USTANOVE_DATAGOV)/popis_srednje-skole.csv:
	wget http://52.178.158.152/api/file/srednje--skole.csv
	mkdir -p $(DIR_OB_USTANOVE_DATAGOV)
	mv srednje--skole.csv $@

$(DIR_OB_USTANOVE_DATAGOV)/popis_visoko-obrazovanje.csv:
	wget http://52.178.158.152/api/file/ustanove_vu.csv
	mkdir -p $(DIR_OB_USTANOVE_DATAGOV)
	mv ustanove_vu.csv $@

$(DIR_OB_USTANOVE_DATAGOV)/popis_znanost.csv:
	wget http://52.178.158.152/api/file/ustanove_z.csv
	mkdir -p $(DIR_OB_USTANOVE_DATAGOV)
	mv ustanove_z.csv $@

## >>>>> obrazovne ustanove s MZOS
$(DIR_OB_USTANOVE_MZOS)/popis_vrtici.xlsx:
	mkdir -p $(DIR_OB_USTANOVE_MZOS)
	wget http://mzos.hr/dbApp/DownloadExcel.ashx?appName=Vrtici \
		-O $@

$(DIR_OB_USTANOVE_MZOS)/popis_osnovne-skole.xlsx:
	mkdir -p $(DIR_OB_USTANOVE_MZOS)
	wget http://mzos.hr/dbApp/DownloadExcel.ashx?appName=OS \
		-O $@

$(DIR_OB_USTANOVE_MZOS)/popis_umjetnicke-skole.xlsx:
	mkdir -p $(DIR_OB_USTANOVE_MZOS)
	wget http://mzos.hr/dbApp/DownloadExcel.ashx?appName=UMJ \
		-O $@

$(DIR_OB_USTANOVE_MZOS)/popis_visoko-obrazovanje.xlsx:
	mkdir -p $(DIR_OB_USTANOVE_MZOS)
	wget http://mzos.hr/dbApp/DownloadExcel.ashx?appName=ustanove_VU \
		-O $@

$(DIR_OB_USTANOVE_MZOS)/popis_znanost.xlsx:
	mkdir -p $(DIR_OB_USTANOVE_MZOS)
	wget http://mzos.hr/dbApp/DownloadExcel.ashx?appName=ustanove_Z \
		-O $@

## >>>>> obrazovne ustanove s MZOS
$(DIR_OB_USTANOVE_MZOS)/popis_srednje-skole.xlsx:
	mkdir -p $(DIR_OB_USTANOVE_MZOS)
	wget http://mzos.hr/dbApp/DownloadExcel.ashx?appName=SS \
		-O $@

## >>>>> scrape za obrazovne ustanove
$(DIR_OB_USTANOVE_SCRAPE)/popis_vrtici_scrape.csv:\
	../scrape/popis_mzos_helpers.py\
	../scrape/popis_vrtici_scrape.py
	mkdir -p $(DIR_OB_USTANOVE_SCRAPE)
	cd ..; pipenv run python scrape/popis_vrtici_scrape.py

$(DIR_OB_USTANOVE_SCRAPE)/popis_osnovne-skole_scrape.csv:\
	../scrape/popis_mzos_helpers.py\
	../scrape/popis_osnovne-skole_scrape.py
	mkdir -p $(DIR_OB_USTANOVE_SCRAPE)
	cd ..; pipenv run python scrape/popis_osnovne-skole_scrape.py

$(DIR_OB_USTANOVE_SCRAPE)/popis_srednje-skole_scrape.csv:\
	../scrape/popis_mzos_helpers.py\
	../scrape/popis_srednje-skole_scrape.py
	mkdir -p $(DIR_OB_USTANOVE_SCRAPE)
	cd ..; pipenv run python scrape/popis_srednje-skole_scrape.py

$(DIR_OB_USTANOVE_SCRAPE)/popis_umjetnicke-skole_scrape.csv:\
	../scrape/popis_mzos_helpers.py\
	../scrape/popis_umjetnicke-skole_scrape.py
	mkdir -p $(DIR_OB_USTANOVE_SCRAPE)
	cd ..; pipenv run python scrape/popis_umjetnicke-skole_scrape.py

$(DIR_OB_USTANOVE_SCRAPE)/popis_visoko-obrazovanje_scrape.csv:\
	../scrape/popis_mzos_helpers.py\
	../scrape/popis_visoko-obrazovanje_scrape.py
	mkdir -p $(DIR_OB_USTANOVE_SCRAPE)
	cd ..; pipenv run python scrape/popis_visoko-obrazovanje_scrape.py

$(DIR_OB_USTANOVE_SCRAPE)/popis_znanost_scrape.csv:\
	../scrape/popis_mzos_helpers.py\
	../scrape/popis_znanost_scrape.py
	mkdir -p $(DIR_OB_USTANOVE_SCRAPE)
	cd ..; pipenv run python scrape/popis_znanost_scrape.py

## >>>>> kandidature na lokalnim izborima
$(DIR_KANDIDATURE)/kandidature_skupstine.csv:\
	lokalni-izbori_kandidature_process-xlsx.sh
	wget https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZS_GSGZ_GV_OV_03%2005%202021.xlsx
	mkdir -p $(DIR_KANDIDATURE)
	mv 'Kandidatura_Otvoreni podaci_ZS_GSGZ_GV_OV_03 05 2021.xlsx'\
		$(@:.csv=.xlsx)
	bash lokalni-izbori_kandidature_process-xlsx.sh $(DIR_KANDIDATURE) $@

$(DIR_KANDIDATURE)/kandidature_nacelnici.csv:\
	lokalni-izbori_kandidature_process-xlsx.sh
	wget https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZN_GNGZ_GN_ON_03%2005%202021.xlsx
	mkdir -p $(DIR_KANDIDATURE)
	mv 'Kandidatura_Otvoreni podaci_ZN_GNGZ_GN_ON_03 05 2021.xlsx'\
		$(@:.csv=.xlsx)
	bash lokalni-izbori_kandidature_process-xlsx.sh $(DIR_KANDIDATURE) $@

$(DIR_KANDIDATURE)/kandidature_zamjenici.csv:\
	lokalni-izbori_kandidature_process-xlsx.sh
	wget https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZZN_ZGN_ZON_03%2005%202021.xlsx
	mkdir -p $(DIR_KANDIDATURE)
	mv 'Kandidatura_Otvoreni podaci_ZZN_ZGN_ZON_03 05 2021.xlsx'\
		$(@:.csv=.xlsx)
	bash lokalni-izbori_kandidature_process-xlsx.sh $(DIR_KANDIDATURE) $@

## >>>>> donacije na lokalnim izborima
$(DIR_DONACIJE)/donacije_lokalni.csv:\
	../scrape/lokalni-izbori-2021_donacije_scrape.py\
	../wrangling/lokalni-izbori_donacije_combine-json.py
	cd ../;\
	pipenv run \
	python scrape/lokalni-izbori-2021_donacije_scrape.py && \
	pipenv run \
	python wrangling/lokalni-izbori_donacije_combine-json.py

## >>>>> infleksijska baza
$(DIR_IMENA)/infleksijska-baza.csv:
	sed -Ee 's/\t|\s/,/g' $(DIR_IMENA)/HML_v50_utf8_Np.txt > \
		$(DIR_IMENA)/infleksijska-baza.csv
	sed -i -e 's/,$$//' $(DIR_IMENA)/infleksijska-baza.csv
	rm $(DIR_IMENA)/HML_v50_utf8_Np.txt
