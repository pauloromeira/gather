from scrapy.http import Request, Response


class BulkRequest(Request):
    def __init__(self, requests, callback):
        super(BulkRequest, self).__init__(url=requests[0].url,
                                          dont_filter=True,
                                          callback=callback)
        self.requests = requests


class BulkResponse(Response):
    def __init__(self, bulk_request, responses):
        super(BulkResponse, self).__init__(url=bulk_request.requests[0].url)
        self.bulk_request = bulk_request
        self.responses = responses
