
import scrapy

class Movies(scrapy.Item):
    name        = scrapy.Field()
    imdb        = scrapy.Field()
    duration        = scrapy.Field()
    country        = scrapy.Field()
    date        = scrapy.Field()
    genres        = scrapy.Field()

# line_number = 34
class LinksSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['https://hdtoday.tv/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]

    except:
        start_urls = []

    def parse(self, response):
        p = Movies()

        p['name'] = response.xpath('//h2[@class="heading-name"]//text()').getall()
        p['imdb'] = response.xpath('//span[@class="item mr-2"]//text()').getall()
        p['duration'] = response.xpath('//*[@id="main-wrapper"]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[4]/div/div[2]/div[1]/text()').getall()
        p['date'] = response.xpath('//*[@id="main-wrapper"]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[4]/div/div[1]/div[1]/text()').getall()
        p['country'] = response.xpath('//*[@id="main-wrapper"]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/a//text()').getall()
        p['genres'] = response.xpath('//*[@id="main-wrapper"]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[4]/div/div[1]/div[2]/a//text()').getall()
        yield p
