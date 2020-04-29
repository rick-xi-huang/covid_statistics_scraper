# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CovidWorldSpider(CrawlSpider):
    name = 'covid_world'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/80.0.3987.163 Safari/537.36 '

    def parse(self, response):
        rows = response.xpath("//a[@class='mt_a']/parent::node()/parent::node()")
        for row in rows:
            country = row.xpath(".//td[1]/a/text()").get()
            total_cases = row.xpath(".//td[2]/text()").get()
            total_deaths = row.xpath(".//td[4]/text()").get()
            total_recovered = row.xpath(".//td[6]/text()").get()
            active_cases = row.xpath(".//td[7]/text()").get()
            serious_critical = row.xpath(".//td[7]/text()").get()
            yield {
                'country': country,
                'total_cases': total_cases,
                'total_deaths': total_deaths,
                'total_recovered': total_recovered,
                'active_cases': active_cases,
                'serious_critical': serious_critical,
            }
