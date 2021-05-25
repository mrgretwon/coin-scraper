import scrapy


class CMCSpider(scrapy.Spider):
    name = 'coinmarketcap'
    start_urls = [
        'https://coinmarketcap.com/new/',
    ]

    def parse(self, response):
        for coin in response.xpath('(//table[contains(@class, "cmc-table")]/tbody/tr/td)[3]'):
            yield {
                'name': coin.xpath('(//p[text()])[1]').get(),
                'ticker': coin.xpath('(//p[text()])[1]').get(),
                'link': coin.css('a::attr("href")').get(),
            }