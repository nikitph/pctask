# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CyclonescrapeItem(scrapy.Item):
    # define the fields for your item here like:
    storm_identifier = scrapy.Field()
    track_history = scrapy.Field()
    forecast_history = scrapy.Field()


class CyclonescrapeForecastItem(scrapy.Item):
    # define the fields for your item here like:
    storm_identifier = scrapy.Field()
    forecast_history = scrapy.Field()
    track_history = scrapy.Field()
