# -*- coding: utf-8 -*-
import scrapy


class LocalSpider(scrapy.Spider):
    name = "local"
    allowed_domains = ['localhost']
    start_urls = (
            'http://localhost:8000',
    )

    def parse(self, response):
        pass
