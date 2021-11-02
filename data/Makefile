# >>>>> varijable
DIR_OB_USTANOVE=obrazovne-ustanove_popis
DIR_KANDIDATURE=2021-lokalni-izbori_kandidature
DIR_DONACIJE=2021-lokalni-izbori_donacije
DIR_IMENA=infleksijska-baza

.PHONY:\
	obrazovne_ustanove\
	kandidature_lokalni\
	donacije_lokalni\
	infleksijska_baza

# >>>>> recepti
obrazovne_ustanove:\
	$(DIR_OB_USTANOVE)/popis_vrtici.csv\
	$(DIR_OB_USTANOVE)/popis_osnovne-skole.csv\
	$(DIR_OB_USTANOVE)/popis_srednje-skole.csv\
	$(DIR_OB_USTANOVE)/popis_visoko-obrazovanje.csv\
	$(DIR_OB_USTANOVE)/popis_znanost.csv

kandidature_lokalni:\
	$(DIR_KANDIDATURE)/kandidature_zamjenici.csv\
	$(DIR_KANDIDATURE)/kandidature_skupstine.csv\
	$(DIR_KANDIDATURE)/kandidature_nacelnici.csv

donacije_lokalni:\
	$(DIR_DONACIJE)/donacije_lokalni.csv

infleksijska_baza:\
	$(DIR_IMENA)/infleksijska-baza.csv

## >>>>> obrazovne ustanove
$(DIR_OB_USTANOVE)/popis_vrtici.csv: 
	wget http://52.178.158.152/api/file/vrtici.csv
	mkdir -p $(DIR_OB_USTANOVE)
	mv vrtici.csv $@

$(DIR_OB_USTANOVE)/popis_osnovne-skole.csv: 
	wget http://52.178.158.152/api/file/skole_os.csv
	mkdir -p $(DIR_OB_USTANOVE)
	mv skole_os.csv $@

$(DIR_OB_USTANOVE)/popis_srednje-skole.csv: 
	wget http://52.178.158.152/api/file/srednje--skole.csv
	mkdir -p $(DIR_OB_USTANOVE)
	mv srednje--skole.csv $@

$(DIR_OB_USTANOVE)/popis_visoko-obrazovanje.csv: 
	wget http://52.178.158.152/api/file/ustanove_vu.csv
	mkdir -p $(DIR_OB_USTANOVE)
	mv ustanove_vu.csv $@

$(DIR_OB_USTANOVE)/popis_znanost.csv: 
	wget http://52.178.158.152/api/file/ustanove_z.csv
	mkdir -p $(DIR_OB_USTANOVE)
	mv ustanove_z.csv $@

## >>>>> kandidature na lokalnim izborima
$(DIR_KANDIDATURE)/kandidature_skupstine.csv:
	wget https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZS_GSGZ_GV_OV_03%2005%202021.xlsx
	mkdir -p $(DIR_KANDIDATURE)
	mv 'Kandidatura_Otvoreni podaci_ZS_GSGZ_GV_OV_03 05 2021.xlsx'\
		$(@:.csv=.xlsx)
	bash 01_process-xlsx_kandidature.sh $(DIR_KANDIDATURE) $@

$(DIR_KANDIDATURE)/kandidature_nacelnici.csv:
	wget https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZN_GNGZ_GN_ON_03%2005%202021.xlsx
	mkdir -p $(DIR_KANDIDATURE)
	mv 'Kandidatura_Otvoreni podaci_ZN_GNGZ_GN_ON_03 05 2021.xlsx'\
		$(@:.csv=.xlsx)
	bash 01_process-xlsx_kandidature.sh $(DIR_KANDIDATURE) $@

$(DIR_KANDIDATURE)/kandidature_zamjenici.csv:
	wget https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZZN_ZGN_ZON_03%2005%202021.xlsx
	mkdir -p $(DIR_KANDIDATURE)
	mv 'Kandidatura_Otvoreni podaci_ZZN_ZGN_ZON_03 05 2021.xlsx'\
		$(@:.csv=.xlsx)
	bash 01_process-xlsx_kandidature.sh $(DIR_KANDIDATURE) $@

## >>>>> donacije na lokalnim izborima
$(DIR_DONACIJE)/donacije_lokalni.csv:
	cd ../;\
	pipenv run \
	python scrape/01_donacije_lokalni-izbori-2021.py && \
	pipenv run \
	python wrangling/01_combine-json_donacije_lokalni.py

## >>>>> infleksijska baza
$(DIR_IMENA)/infleksijska-baza.csv:
	sed -Ee 's/\t|\s/,/g' $(DIR_IMENA)/HML_v50_utf8_Np.txt > \
		$(DIR_IMENA)/infleksijska-baza.csv
	sed -i -e 's/,$$//' $(DIR_IMENA)/infleksijska-baza.csv
	rm $(DIR_IMENA)/HML_v50_utf8_Np.txt
