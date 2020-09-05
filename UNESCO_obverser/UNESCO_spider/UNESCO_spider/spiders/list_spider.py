import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from urllib.parse import urljoin
from ..items import UnescoSpiderItem, UnescocountryspiderItem

class ListSpiderSpider(scrapy.Spider):
    name = 'list_spider'
    allowed_domains = ['whc.unesco.org']
    start_urls = ['http://whc.unesco.org/zh/list']

    #获取所有世界遗产国家及链接
    def parse(self, response):
        selector = Selector(text=response.text)
        country_list = selector.xpath('//div[@id="main"]/div[@class="content"]/h4/a/text()').extract()
        # for country in country_list:
            # item = UnescocountryspiderItem()
            #国家名称
            # item["country_name"] = country
            # yield item
        country_link = selector.xpath('//div[@class="content"]/h4/a/@href')
        # for url in country_link.extract():
        #     yield Request(urljoin(response.url, url),  callback=self.list_parse)

    #获取各个国家世界遗产名录，及详情链接
    def list_parse(self, response):
        selector = Selector(text=response.text)
        # #国家名称
        # countryofwh = selector.xpath('//div[@class="content"]/h4/a/text()').extract()
        # #对应国家世界遗产列表
        # wh_name_list = selector.xpath('//div[@class="content"]/ul/li[@*]/a[@href]/text()').extract()
        list_link = selector.xpath('//div[@class="content"]/ul/li[@*]/a/@href')
        for url in list_link.extract():
            yield Request(urljoin(response.url, url), callback=self.detail_parse)

    #获取世界遗产详情
    def detail_parse(self, response):
        selector = Selector(text=response.text)
        wh_country = selector.xpath('//div[@class="alternate"]/div[1]/a/text()')[1].extract().strip(' ')
        # print(wh_country)
        wh_name = selector.xpath('//div[@class="content"]/div[@class="content"]/h1/text()').extract()[0].strip()
        # print(wh_name)
        wh_detail = selector.xpath('//div[@class="readable"]/p/text()').extract()
        # print(wh_detail)
        wh_time = selector.xpath('//div[@class="alternate"]/div/strong[text()="注册时间"]/../text()').extract()[1].strip().strip(':')
        # print(wh_time)
        wh_img_href = selector.xpath('//div[@class="icaption bordered"]/a[@href]/img/@src')
        src_list = []
        for src in wh_img_href.extract():
            src_list.append(urljoin('http://whc.unesco.org/', src))
        # print(src_list)
        item = UnescoSpiderItem()
        item["name"] = wh_name
        if wh_detail != []:
            item["detail"] = wh_detail[0]
        else:
            item["detail"] = ''
        item["img_src"] = src_list
        item["time"] = wh_time
        item["country_name"] = wh_country
        yield item

