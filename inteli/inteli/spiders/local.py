# -*- coding: utf-8 -*-
import scrapy


class LocalSpider(scrapy.Spider):
    name = "local"
    allowed_domains = ['localhost']
    start_urls = (
            'http://localhost:8765',
    )

    def parse(self, response):
        import ipdb; ipdb.set_trace()
