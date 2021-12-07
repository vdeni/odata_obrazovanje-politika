import re
from classla import Pipeline


def apply_nlp_pipeline(data: list[str],
                       pipeline: Pipeline) -> list[str]:
    """
    Primijeni CLASSLA nlp pipeline na listu stringova. Vraca listu stringova u
    kojoj se nalaze samo oni unosi iz izvorne liste koji su prepoznati kao
    'PER'. Ulazi u svaki 'PER' unos i pregledava tagove elemenata. Ako svi nisu
    '*-PER', zanemaruje cijeli unos.
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


def filter_entries(data: list[str],
                   inflectional_set: set,
                   names_set: set,
                   lastnames_set: set) -> list[str]:
    """
    Filtriranje unosa u popisu djelatnika tako da se izbace pogresno
    prepoznati entiteti. Izbacuje unose koji sadrze samo jednu rijec. Izbacuje
    unose dulje od sest rijeci. Za ostale provjerava nalazi li se bilo koji od
    elemenata unosa u infleksijskoj bazi ili u popisu imena DZS. Ako se niti
    jedan element ne nalazi u tim bazama, unos se izbacuje.
    """
    data_elems = [elem.split() for elem in data
                  if len(elem.split()) > 1 and len(elem.split()) <= 5]

    for entry_idx, entry in enumerate(data_elems):
        entry_set = set(entry)

        if not set(entry_set).intersection(inflectional_set) or\
                not set(entry_set).intersection(names_set) or\
                not set(entry_set).intersection(lastnames_set):
            data_elems.pop(entry_idx)
        else:
            data_elems[entry_idx] = ' '.join(entry)

    return data_elems
