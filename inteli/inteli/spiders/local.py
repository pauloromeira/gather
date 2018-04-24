# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from inteli.tools import BulkRequest


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
        requests = []
        for link in links:
            requests.append(Request(response.urljoin(link),
                                    callback=self.other_pages))

        yield BulkRequest(requests, callback=self.other_pages)


    def other_pages(self, response):
        for response in response.responses:
            print('******** ' + response.xpath('//title/text()').extract_first())
