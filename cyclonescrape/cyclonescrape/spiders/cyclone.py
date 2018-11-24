# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup


from ..items import CycloneTrackHistoryItem, CycloneForecastHistoryItem


class CycloneSpider(CrawlSpider):
    name = 'cyclone'
    allowed_domains = ['rammb.cira.colostate.edu']
    start_urls = ['http://rammb.cira.colostate.edu/products/tc_realtime/index.asp']

    rules = (
        Rule(LinkExtractor(allow=r'storm\.asp'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'strmfcst\.asp'), callback='parse_item_2', follow=True),
    )

    def parse_item(self, response):
        item = CycloneTrackHistoryItem()
        item['storm_identifier'] = response.url.split('=')[-1]
        item['storm_name'] = \
            response.css('body:nth-child(2) div:nth-child(1) > h2:nth-child(2)::text').extract()[0].split('- ')[-1]

        print('Parse :' + response.url.split('=')[-1])
        tabl = response.css('body > div > div > div.text_product_wrapper > table').extract()[1]
        for row in BeautifulSoup(tabl)("tr"):
            if row("td")[0].text == "Synoptic Time":
                continue
            item['synoptic_time'] = row("td")[0].text
            item['latitude'] = row("td")[1].text
            item['longitude'] = row("td")[2].text
            item['intensity'] = row("td")[3].text
            yield item

    def parse_item_2(self, response):
        item = CycloneForecastHistoryItem()
        item['storm_identifier'] = response.url.split('=')[-1]
        print('Parse :' + response.url.split('=')[-1])
        for i in range(len(response.css('body > div > div > h4::text').extract())):
            item['time_of_forecast'] = response.css('body > div > div > h4::text').extract()[i].split(': ')[-1]
            tabl = response.css('body > div > div > table').extract()[i]
            for row in BeautifulSoup(tabl)("tr"):
                if row("td")[0].text == "Forecast Hour":
                    continue
                item['forecast_hour'] = row("td")[0].text
                item['latitude'] = row("td")[1].text
                item['longitude'] = row("td")[2].text
                item['intensity'] = row("td")[3].text
                yield item
