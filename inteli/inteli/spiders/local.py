# -*- coding: utf-8 -*-
import scrapy


class LocalSpider(scrapy.Spider):
    name = "local"
    allowed_domains = ['httbin.org']
    start_urls = (
        'https://httpbin.org/ip',
    )

    def parse(self, response):
        pass
