import scrapy


class CMCSpider(scrapy.Spider):
    name = 'coinmarketcap'
    base_url = 'https://coinmarketcap.com'
    start_urls = [
        base_url + '/new',
    ]

    def parse(self, response):
        for coin in response.xpath('//table[contains(@class, "cmc-table")]/tbody/tr'):
            name_row = coin.xpath('(td)[3]')
            yield {
                'name': name_row.css('p::text')[0].get(),
                'ticker': name_row.css('p::text')[1].get(),
                'link': self.base_url + name_row.css('a::attr("href")').get(),
            }
