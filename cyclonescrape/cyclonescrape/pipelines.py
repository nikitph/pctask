# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2


class CyclonescrapePipeline(object):
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'cycloneuser'
        password = 'abc'  # your password
        database = 'cyclonedata'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO cyclone(storm_identifier, track_history, forecast_history) VALUES (%s,%s, %s);",
                         (item['storm_identifier'], item['track_history'], item['forecast_history']))
        self.connection.commit()
        return item
