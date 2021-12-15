# >>>>> varijable
COMMON_DEPS=_config.yml _site.yml

.PHONY:\
	web

# >>>>> recepti

## >>>>> apstraktni
web:\
	index.html\
	spol-rukovodeci.html\
	$(COMMON_DEPS)

## >>>>> konkretni
index.html: index.Rmd $(COMMON_DEPS)
	Rscript -e "setwd('..'); renv::activate(); setwd('docs/'); rmarkdown::render('$<')"

spol-rukovodeci.html: spol-rukovodeci.Rmd $(COMMON_DEPS)\
	../data/obrazovne-ustanove_popis_datagov/*
	Rscript -e "setwd('..'); renv::activate(); setwd('docs/'); rmarkdown::render('$<')"
