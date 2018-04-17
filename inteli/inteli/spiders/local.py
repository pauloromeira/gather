# -*- coding: utf-8 -*-
import scrapy


class LocalSpider(scrapy.Spider):
    name = "local"
    allowed_domains = ["localhost"]
    start_urls = (
        'http://www.localhost/',
    )

    def parse(self, response):
        pass
