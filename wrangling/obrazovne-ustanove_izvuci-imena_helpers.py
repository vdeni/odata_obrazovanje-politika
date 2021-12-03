def apply_nlp_pipeline(data,
                       pipeline):
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
