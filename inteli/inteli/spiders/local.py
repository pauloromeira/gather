# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request


class LocalSpider(scrapy.Spider):
    name = "local"
    allowed_domains = ['localhost']
    start_urls = (
            'http://localhost:8765',
    )

    def parse(self, response):
        print('******** ' + response.xpath('//title/text()').extract_first())

        link = response.xpath('//a/@href').extract_first()
        yield Request(response.urljoin(link), callback=self.page1)

    def page1(self, response):
        print('******** ' + response.xpath('//title/text()').extract_first())

        links = response.xpath('//a/@href').extract()
        for link in links:
            yield Request(response.urljoin(link), callback=self.other_pages)

    def other_pages(self, response):
        print('******** ' + response.xpath('//title/text()').extract_first())
