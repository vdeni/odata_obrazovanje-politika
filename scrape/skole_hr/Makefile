# >>>>> varijable
COMMON_DEPS_SKOLE=skole_hr/items.py skole_hr/pipelines.py skole_hr/settings.py

.PHONY:\
	all

# >>>>> recepti
## >>>>> apstraktni
all:\
	data/osnovne_skole.jl

## >>>>> konkretni
data/osnovne_skole.jl: skole_hr/spiders/skole.py\
	$(COMMON_DEPS_SKOLE)
	pipenv run scrapy crawl spider_skole-hr\
		-s LOG_FILE=log_spider_os_skole-hr.txt\
		-a link_db_path=skole_hr/skole_osnovne_url.csv\
		-a data_path=data/osnovne_skole.jl\
		-a path_404=data/osnovne_list_404.txt
