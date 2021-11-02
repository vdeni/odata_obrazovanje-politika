import os
import json

import pandas

# >>>>> setup
_append_colnames = ["rb", "nazivDonatora", "oib", "adresaDonatora",
                    "datumDonacije", "iznos", "trzisnaVrijednost", "ukupno"]

data_path = os.path.join('data',
                         '2021-lokalni-izbori_donacije')

data_folders = [filename for filename in os.listdir(data_path)
                if os.path.isdir(os.path.join(data_path,
                                              filename))]

data_files = os.listdir(os.path.join(data_path,
                                     data_folders[0]))

data_files = [os.path.abspath(os.path.join(data_path,
                                           data_folders[0],
                                           filename))
              for filename in data_files]

# >>>>> join
d_out = pandas.DataFrame()

for filename in data_files[0:1]:
    with open(filename, 'r') as infile:
        d_json = json.load(infile)

    d = pandas.json_normalize(d_json)

    d = d.explode('data')

    d_append = pandas.DataFrame(columns=_append_colnames)

    if not d.data.isna():
        for row in range(0, d.shape[0]):
            _ = pandas.DataFrame(d.data.iloc[row],
                                 index=[0])

            d_append = pandas.concat([d_append,
                                      _])

    d = d.drop(columns='data')

    d = pandas.concat([d,
                       d_append],
                      axis=1)

    d_out = pandas.concat([d_out,
                           d])
