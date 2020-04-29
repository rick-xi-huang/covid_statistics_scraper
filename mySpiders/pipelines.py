# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import sqlite3


class SQLlitePipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect("covid_world.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE covid_world(
                    country TEXT,
                    total_cases INTEGER ,
                    total_deaths INTEGER ,
                    total_recovered INTEGER ,
                    active_cases INTEGER ,
                    serious_critical INTEGER 
                )

            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO covid_world (country,total_cases,total_deaths,total_recovered,active_cases,serious_critical) VALUES(?,?,?,?,?,?)

        ''', (
            item.get('country'),
            item.get('total_cases'),
            item.get('total_deaths'),
            item.get('total_recovered'),
            item.get('active_cases'),
            item.get('serious_critical')
        ))
        self.connection.commit()
        return item

class CovidWorldPipeline(object):
    def process_item(self, item, spider):
        return item
