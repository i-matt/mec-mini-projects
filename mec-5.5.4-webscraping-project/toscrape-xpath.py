#scrapy xpath spider
import scrapy

class QuotesXPathSpider(scrapy.Spider):
    name = "toscrape-xpath"
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('.//span/text()').get(),
                'author': quote.xpath('.//small/text()').get(),
                'tags': quote.xpath('.//div/a/text()').getall()
            }
       
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        
