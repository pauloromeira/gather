# from scrapy.exceptions import NotConfigured
from inteli.tools import BulkRequest, BulkResponse
from twisted.internet import defer


class GatherMiddleware(object):

    def __init__(self, crawler):
        # if not settings.getbool('GATHER_ENABLED'):
        #     raise NotConfigured
        self.crawler = crawler

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler)
        # crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        # crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
        return o


    @defer.inlineCallbacks
    def process_request(self, request, spider):
        if isinstance(request, BulkRequest):
            deferreds = [self.crawler.engine.download(req, spider)
                            for req in request.requests]
            responses = yield defer.gatherResults(deferreds)
            defer.returnValue(BulkResponse(request, responses))


    # def process_response(self, request, response, spider):
    #     return response


    # def process_exception(self, request, exception, spider):
    #     pass
