import scrapy


class SkoleHrItem(scrapy.Item):
    skola_url = scrapy.Field()
    tekst = scrapy.Field()
