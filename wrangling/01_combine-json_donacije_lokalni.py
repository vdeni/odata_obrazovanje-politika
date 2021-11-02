import os
import json

import pandas

# >>>>> setup
# imena stupaca za podatke vezane uz pojedine donatore
_append_colnames = ["rbIndiv",
                    "nazivDonatoraIndiv",
                    "oibIndiv",
                    "adresaDonatoraIndiv",
                    "datumDonacijeIndiv",
                    "iznosIndiv",
                    "trzisnaVrijednostIndiv",
                    "ukupnoIndiv"]

data_path = os.path.join('data',
                         '2021-lokalni-izbori_donacije')

data_folders = [filename for filename in os.listdir(data_path)
                if os.path.isdir(os.path.join(data_path,
                                              filename))]

data_files = []

for folder in data_folders:
    _ = os.listdir(os.path.join(data_path,
                                folder))

    data_files += [os.path.abspath(os.path.join(data_path,
                                                folder,
                                                filename))
                   for filename in _]

# >>>>> join
d_out = pandas.DataFrame()

for filename in data_files:
    with open(filename, 'r') as infile:
        d_json = json.load(infile)

    d = pandas.json_normalize(d_json)

    d = d.explode('data')

    if pandas.isna(d.data).all():
        d_append = pandas.DataFrame(columns=_append_colnames)

    elif not pandas.isna(d.data).all():
        d_append = pandas.DataFrame()

        for row in range(0, d.shape[0]):
            _ = pandas.DataFrame(d.data.iloc[row],
                                 index=[0])

            d_append = pandas.concat([d_append,
                                      _])

        d_append = d_append.rename(lambda x: x + 'Indiv',
                                   axis=1)

    d = d.drop(columns='data')

    d = pandas.concat([d,
                       d_append],
                      axis=1)

    d_out = pandas.concat([d_out,
                           d])

d_out.reset_index(inplace=True,
                  drop=True)

d_out.to_csv(os.path.join(data_path,
                          'donacije_lokalni.csv'),
             sep=';',
             index=False,
             encoding='utf-8',
             na_rep='NA')
