import scrapy


class SkoleHrItem(scrapy.Item):
    skola_url = scrapy.Field()
    skola_naziv = scrapy.Field()
    skola_zupanija = scrapy.Field()
    skola_mjesto = scrapy.Field()
    tekst = scrapy.Field()
