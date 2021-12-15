library(here)
library(dplyr)
library(magrittr)
library(readr)

set.seed(1)

d_osnovne <- readr::read_csv2(here::here('data',
                                         'obrazovne-ustanove_popis_scrape',
                                         'popis_osnovne-skole_scrape.csv')) %>%
    dplyr::select(.,
                  naziv,
                  mjesto,
                  zupanija,
                  web) %>%
    sample_n(.,
             100)

readr::write_csv2(d_osnovne,
                  here('stats',
                       'obrazovne-ustanove_popis_sample.csv'))
