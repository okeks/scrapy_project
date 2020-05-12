import scrapy
from ..items import QuotetutorialItem

class Quote_spider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items = QuotetutorialItem()
        all_quotes = response.css('div.quote')
        for quote in all_quotes:

            title = quote.css('span.text::text').extract()
            author = quote.css('span small.author::text').extract()
            tags = quote.css('div.tags a.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items

