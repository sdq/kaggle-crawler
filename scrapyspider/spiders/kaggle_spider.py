from scrapy.spiders import Spider
import scrapy
import json

class CompetitionsSpider(Spider):
    name = "competitions"

    def start_requests(self):
        yield scrapy.Request('https://www.kaggle.com/competitions?sortBy=prize&group=active&page=1&segment=inClass', self.parse_kaggle)

    def parse_kaggle(self, response):
        doc = response.xpath("//script").extract()[9]
        doc = doc[85:-110]
        # print(doc)
        jsondoc = json.loads(doc)
        print(jsondoc)

class DatasetsSpider(Spider):
    name = "datasets"

    def start_requests(self):
        yield scrapy.Request('https://www.kaggle.com/datasets', self.parse_kaggle)

    def parse_kaggle(self, response):
        doc = response.xpath("//script").extract()[10]
        doc = doc[85:-107]
        # print(doc)
        jsondoc = json.loads(doc)
        print(jsondoc)

class KernelsSpider(Spider):
    name = "kernels"

    def start_requests(self):
        yield scrapy.Request('https://www.kaggle.com/kernels', self.parse_kaggle)

    def parse_kaggle(self, response):
        doc = response.xpath("//script").extract()[9]
        doc = doc[85:-101]
        # print(doc)
        jsondoc = json.loads(doc)
        print(jsondoc)

# https://www.kaggle.com/topics.json

class DiscussionSpider(Spider):
    name = "discussion"

    def start_requests(self):
        yield scrapy.Request('https://www.kaggle.com/discussion', self.parse_kaggle)

    def parse_kaggle(self, response):
        doc = response.xpath("//script").extract()[9]
        doc = doc[85:-101]
        # print(doc)
        jsondoc = json.loads(doc)
        print(jsondoc)