from scrapy.item import Item, Field
from scrapy.http import FormRequest
from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser


class pubSpider(Spider):
    name = "pubSpider"
    allowed_domains = ["9292.nl"]
    start_urls = ["http://9292.nl"]

    def parse(self, response):
        formdata={'fromText': 'Rotterdam Centraal', 'toText': 'Amsterdam Centraal', 'dateTime.date':'2015-11-29','dateTime.time':'00:35','searchType':'aankomst'}
        yield FormRequest.from_response(response,
                                        formdata=formdata,
                                        callback=self.parse1)

    def parse1(self, response):
        open_in_browser(response)