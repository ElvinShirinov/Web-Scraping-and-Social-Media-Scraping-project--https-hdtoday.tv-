import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'link_lists'
    allowed_domains = ['https://hdtoday.tv/']
    start_urls = ['https://hdtoday.tv/home']

    def parse(self, response):
        xpath = '//h3[@class="film-name"]//@href'

        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://hdtoday.tv/' + s.get()
            yield l