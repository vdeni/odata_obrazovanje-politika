import re

from classla import Pipeline


def apply_nlp_pipeline(data: list[str],
                       pipeline: Pipeline) -> list[str]:
    """
    Primijeni CLASSLA nlp pipeline na listu stringova. Vraca listu stringova u
    kojoj se nalaze samo oni unosi iz izvorne liste koji su prepoznati kao
    'PER'. Ulazi u svaki unos i vadi sukcesivne B-PER i I-PER tagove.
    """
    out_list = []

    for entry_idx, entry in enumerate(data):
        try:
            doc = pipeline(entry)

            elems = doc.get(['text', 'ner'],
                            from_token=True)

            for elem_idx, elem in enumerate(elems):
                if elem[1] == 'B-PER':
                    out_line = elem[0]
                elif elem[1] == 'I-PER':
                    out_line = ' '.join([out_line, elem[0]])

                    if elem_idx + 1 == len(elems):
                        out_list.append(out_line)

                        del(out_line)
                elif elem[1] not in ['B-PER', 'I-PER']\
                        and 'out_line' in locals():
                    out_list.append(out_line)

                    del(out_line)
                elif elem[1] not in ['B-PER', 'I-PER']\
                        and 'out_line' not in locals():
                    continue

        except IndexError:
            continue

    return out_list


def dash_handler(data: list[str]) -> list[str]:
    """
    Ukloni razmake oko crtica; npr. ako je napisano 'Ivan Horvat - Vuk',
    rezultat treba biti 'Ivan Horvat-Vuk'. Osim toga, zamjenjuje en i em dash
    s obicnom crticom (CLSSLA NER moze raditi s em dashom, ali ne i s en).
    Ovo olaskava izvlacenje imena u appl_nlp_pipleine().
    """
    re_dashes = re.compile('\\s*[\u002d\u2010\u2011\u2012\u2013\u2014]\\s*')

    out_list = [re_dashes.sub(string=entry,
                              repl='-') for entry in data]

    return out_list


def normalize_inputs(data: list[str]) -> list[str]:
    """
    Ukloni interpunkciju iz unosa, ukloni vise uzastopnih razmaka, ukloni
    razmake na pocetku i na kraju unosa.
    """
    re_punctuation = re.compile(
        '[\'\'!\"#\\$%&\'()*+,-./:;<=>\\?@\\[\\]^_`{|}~]')

    data = [re_punctuation.sub(repl=' ',
                               string=elem) for elem in data]

    data = [elem.strip() for elem in data]

    data = [re.sub(pattern='\\s{2,}',
                   repl=' ',
                   string=elem) for elem in data]

    data = [elem.title() for elem in data]

    return data


def filter_entries(data: list[str]) -> list[str]:
    """
    Filtriranje unosa u popisu djelatnika. Izbacuje unose koji sadrze samo
    jednu rijec.
    """
    data_elems = [elem for elem in data if len(elem.split()) > 1]

    return data_elems
