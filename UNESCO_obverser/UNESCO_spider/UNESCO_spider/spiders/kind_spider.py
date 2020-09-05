import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from urllib.parse import urljoin
from ..items import UnescokindspiderItem


class KindSpiderSpider(scrapy.Spider):
    name = 'kind_spider'
    allowed_domains = ['yichan.cnair.com']
    start_urls = ['http://yichan.cnair.com/wenhua/',
                  'http://yichan.cnair.com/ziran/',
                  'http://yichan.cnair.com/koushu/',
                  'http://yichan.cnair.com/shuangchong/',
                  'http://yichan.cnair.com/jingguan/',
                  'http://yichan.cnair.com/guojia/']

    def parse(self, response):
        selector = Selector(text=response.text)
        item = UnescokindspiderItem()
        kind = selector.xpath('//div[@id="ConBodyLeft"]/div[@id="theCurrent"]/a[3]/text()').extract()
        print(kind)
        ki = 0
        if kind == []:
            ki = 0
        elif kind[0] == "世界文化遗产":
            ki = 1
        elif kind[0] == "世界自然遗产":
            ki = 2
        elif kind[0] == "世界非物质文化遗产":
            ki = 3
        elif kind[0] == "文化和自然双重遗产":
            ki = 4
        elif kind[0] == "文化景观":
            ki = 5
        elif kind[0] == "国家级文化遗产":
            ki = 6
        listofUNESCO = selector.xpath('//div[@id="ConBodyLeft"]/div[@id="theContent"]/div[@class="mainListNewsInfo"]/div/span/a/text()').extract()
        for UNESCO in listofUNESCO:
            item = UnescokindspiderItem()
            item["kind"] = ki
            item["name"] = UNESCO
            yield item
        # UNESCO_link = selector.xpath('/div[@id="ConBodyLeft"]/div[@id="theContent"]/div[@class="mainListNewsInfo"]/div/span/a/@href').extract()
        # for url in UNESCO_link:
        #     yield Request(url, callback=self.detail_parse)
        next_index_list = selector.xpath('//div[@id="ConBodyLeft"]/div[@id="thePage"]/a/@href').extract()
        print(next_index_list)
        for url in next_index_list:
            yield Request(urljoin(response.url, url))

