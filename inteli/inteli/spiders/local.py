# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from inteli.tools import BulkRequest

from inline_requests import inline_requests


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


    @inline_requests
    def page1(self, response):
        print('******** ' + response.xpath('//title/text()').extract_first())

        links = response.xpath('//a/@href').extract()
        # links.append('http://localhost:9999')
        requests = [Request(response.urljoin(link)) for link in links]

        bulk_response = yield BulkRequest(requests)
        for response in bulk_response.responses:
            print('******** ' + response.xpath('//title/text()').extract_first())
