import re
from classla import Pipeline


def apply_nlp_pipeline(data: list[str],
                       pipeline: Pipeline) -> list[str]:
    """
    Primijeni CLASSLA nlp pipeline na listu stringova. Vraca listu stringova u
    kojoj se nalaze samo oni unosi iz izvorne liste koji su prepoznati kao
    PERSON.
    """
    out_list = []

    for entry_idx, entry in enumerate(data):
        try:
            doc = pipeline(entry)

            for entity in doc.entities:
                if entity.type == 'PER':
                    out_list.append(entity.text)
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

# def filter_entries(series: pandas.Series,
#                    inflectional_db: pandas.DataFrame,
#                    names_db: pandas.DataFrame) -> pandas.Series:
#     """
#     Filtriranje unosa u popisu djelatnika tako da se izbace pogresno
#     prepoznati entiteti. Izbacuje unose koji sadrze samo jednu rijec. Izbacuje
#     unose dulje od sest rijeci. Za ostale provjerava nalazi li se bilo koji od
#     elemenata unosa u infleksijskoj bazi ili u popisu imena DZS. Ako se niti
#     jedan element ne nalazi u tim bazama, unos se izbacuje.
#     """
#     pass
