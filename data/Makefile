# >>>>> varijable
DIR_OB_USTANOVE=obrazovne-ustanove_popis
DIR_KANDIDATURE=2021-lokalni-izbori_kandidature

.PHONY: obrazovne_ustanove\
	kandidature_lokalni\
	dir_obrazovne\
	dir_kandidature

# >>>>> recepti
obrazovne_ustanove:\
	popis_vrtici.csv\
	popis_osnovne-skole.csv\
	popis_srednje-skole.csv\
	popis_visoko-obrazovanje.csv\
	popis_znanost.csv

kandidature_lokalni:\
	$(DIR_KANDIDATURE)/kandidature_zamjenici.csv\
	$(DIR_KANDIDATURE)/kandidature_skupstine.csv\
	$(DIR_KANDIDATURE)/kandidature_nacelnici.csv

# >>>>> obrazovne ustanove
popis_vrtici.csv: dir_obrazovne
	wget http://52.178.158.152/api/file/vrtici.csv
	mv vrtici.csv $(DIR_OB_USTANOVE)/$@

popis_osnovne-skole.csv: dir_obrazovne
	wget http://52.178.158.152/api/file/skole_os.csv
	mv skole_os.csv $(DIR_OB_USTANOVE)/$@

popis_srednje-skole.csv: dir_obrazovne
	wget http://52.178.158.152/api/file/srednje--skole.csv
	mv srednje--skole.csv $(DIR_OB_USTANOVE)/$@

popis_visoko-obrazovanje.csv: dir_obrazovne
	wget http://52.178.158.152/api/file/ustanove_vu.csv
	mv ustanove_vu.csv $(DIR_OB_USTANOVE)/$@

popis_znanost.csv: dir_obrazovne
	wget http://52.178.158.152/api/file/ustanove_z.csv
	mv ustanove_z.csv $(DIR_OB_USTANOVE)/$@

# >>>>> kandidature na lokalnim izborima
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
