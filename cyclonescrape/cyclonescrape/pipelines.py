# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
from .items import CycloneTrackHistoryItem, CycloneForecastHistoryItem
import os


class CyclonescrapePipeline(object):
    def open_spider(self, spider):
        hostname = os.getenv('DB_HOST')
        username = 'postgres'
        password = 'abc'  # your password
        database = 'cyclonedata'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.connection.autocommit = True
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        print(str(type(item)))
        if isinstance(item, CycloneTrackHistoryItem):
            self.cur.execute("INSERT INTO cyclone_info(storm_identifier, storm_name)"
                             " VALUES (%s,%s) ON CONFLICT (storm_identifier) DO NOTHING;",
                             (item['storm_identifier'], item['storm_name']))
            self.connection.commit()

        if isinstance(item, CycloneForecastHistoryItem):
            self.cur.execute("INSERT INTO cyclone_forecast_history(storm_identifier, time_of_forecast, forecast_hour,"
                             "latitude, longitude, intensity) VALUES (%s,%s, %s, %s, %s, %s);",
                             (item['storm_identifier'], item['time_of_forecast'], item['forecast_hour'],
                              item['latitude'],
                              item['longitude'], item['intensity']))
            self.connection.commit()

        else:
            self.cur.execute("INSERT INTO cyclone_track_history(storm_identifier, synoptic_time,"
                             "latitude, longitude, intensity) VALUES (%s, %s, %s, %s, %s);",
                             (item['storm_identifier'], item['synoptic_time'],
                              item['latitude'], item['longitude'], item['intensity']))
            self.connection.commit()

        self.connection.commit()
        return item
