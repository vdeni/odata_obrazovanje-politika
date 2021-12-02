import scrapy


def unlist_singleton(singleton_list):
    """
    Helper za prebacivanje singleton liste u sam element.
    """
    return singleton_list[0]


class SkoleHrItem(scrapy.Item):
    skola_url = scrapy.Field(output_processor=unlist_singleton)
    skola_naziv = scrapy.Field(output_processor=unlist_singleton)
    skola_zupanija = scrapy.Field(output_processor=unlist_singleton)
    skola_mjesto = scrapy.Field(output_processor=unlist_singleton)
    tekst = scrapy.Field()
