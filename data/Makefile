# >>>>> varijable
DIR_OB_USTANOVE=obrazovne-ustanove_popis
DIR_KANDIDATURE=2021-lokalni-izbori_kandidature

# >>>>> recepti
obrazovne_ustanove: dir_obrazovne\
	popis_vrtici.csv\
	popis_osnovne-skole.csv\
	popis_srednje-skole.csv\
	popis_visoko-obrazovanje.csv\
	popis_znanost.csv

kandidature_lokalni: dir_kandidature\
	kandidature_zamjenici.csv\
	kandidature_skusptine.csv\
	kandidature_nacelnici.csv

.PHONY: obrazovne_ustanove\
	kandidature_lokalni

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

dir_obrazovne:
	if [[ ! -d $(DIR_OB_USTANOVE) ]];\
		printf '\n\n>>>>> CREATING DIRECTORY\n\n';\
		then mkdir $(DIR_OB_USTANOVE);\
	fi

# >>>>> kandidature na lokalnim izborima
kandidature_nacelnici.csv: dir_kandidature
	wget https://www.izbori.hr/site/UserDocsImages/2021/Lokalni%20izbori%202021/KANDIDATURE/Kandidatura_Otvoreni%20podaci_ZS_GSGZ_GV_OV_03%2005%202021.xlsx
	mv 'Kandidatura_Otvoreni podaci_ZS_GSGZ_GV_OV_03 05 2021.xlsx'\
		$(DIR_KANDIDATURE)/$(basename $@).xlsx
	# convert to semicolon delimited csv
	libreoffice --convert-to csv:"Text - txt - csv (StarCalc)":59,34,33,1,1\
		--outdir $(DIR_KANDIDATURE)\
		$(DIR_KANDIDATURE)/$(basename $@).xlsx
	rm $(DIR_KANDIDATURE)/$(basename $@).xlsx
	# convert to utf-8 encoding from WIN-1250
	enconv -L hr -x utf-8 $(DIR_KANDIDATURE)/$@
	# squash repeating whitespace, strip whitespace from ends
	sed -E -i -e 's/\s{2,}/ /g' $(DIR_KANDIDATURE)/$@

dir_kandidature:
	if [[ ! -d $(DIR_KANDIDATURE) ]];\
		printf '\n\n>>>>> CREATING DIRECTORY\n\n';\
		then mkdir $(DIR_KANDIDATURE);\
	fi
