# >>>>> varijable
COMMON_DEPS=skole_hr/items.py skole_hr/pipelines.py skole_hr/settings.py

.PHONY:\
	all

# >>>>> recepti
data/osnovne_skole.jl: skole_hr/spiders/skole.py\
	$(COMMON_DEPS)
	pipenv run scrapy crawl spider_skole-hr\
		-s LOG_FILE=log_spider_os_skole-hr.txt\
		-a link_db_path=skole_hr/skole_osnovne_url.csv\
		-a data_path=data/osnovne_skole.jl\
		-a path_404=data/osnovne_list_404.txt
