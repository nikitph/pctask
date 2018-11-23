# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup


from ..items import CyclonescrapeItem, CyclonescrapeForecastItem


class CycloneSpider(CrawlSpider):
    name = 'cyclone'
    allowed_domains = ['rammb.cira.colostate.edu']
    start_urls = ['http://rammb.cira.colostate.edu/products/tc_realtime/index.asp']

    rules = (
        Rule(LinkExtractor(allow=r'storm\.asp'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'strmfcst\.asp'), callback='parse_item_2', follow=True),
    )

    def parse_item(self, response):
        i = {}
        item = CyclonescrapeItem()
        item['storm_identifier'] = response.url.split('=')[-1]
        print('Parse :' + response.url.split('=')[-1])
        tabl = response.css('body > div > div > div.text_product_wrapper > table').extract()[1]
        table_data = [[cell.text for cell in row("td")]
                      for row in BeautifulSoup(tabl)("tr")]
        item['track_history'] = table_data
        item['forecast_history'] = ''
        print(table_data)
        return item

    def parse_item_2(self, response):
        i = {}
        item = CyclonescrapeForecastItem()
        item['storm_identifier'] = response.url.split('=')[-1]
        print('Parse :' + response.url.split('=')[-1])
        h4d={}
        print(len(response.css('body > div > div > h4::text').extract()))
        for i in range(len(response.css('body > div > div > h4::text').extract())):
            tabl = response.css('body > div > div > table').extract()[i]
            table_data = [[cell.text for cell in row("td")]
                            for row in BeautifulSoup(tabl)("tr")]
            h4d[response.css('body > div > div > h4::text').extract()[i]] = table_data
        item['forecast_history'] = str(h4d)
        item['track_history'] = ''
        return item