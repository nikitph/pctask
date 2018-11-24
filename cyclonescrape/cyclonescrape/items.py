# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CycloneTrackHistoryItem(scrapy.Item):
    # define the fields for your item here like:
    storm_identifier = scrapy.Field()
    storm_name = scrapy.Field()
    synoptic_time = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    intensity = scrapy.Field()


class CycloneForecastHistoryItem(scrapy.Item):
    # define the fields for your item here like:
    storm_identifier = scrapy.Field()
    time_of_forecast = scrapy.Field()
    forecast_hour = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    intensity = scrapy.Field()
