import scrapy
from scrapy.selector import Selector
from ..items import UnesconewsItem
import MySQLdb
from scrapy.http import Request
from urllib.parse import urljoin


class PreliminaryListSpider(scrapy.Spider):
    name = 'preliminary_list'
    allowed_domains = ['whc.unesco.org']
    start_urls = ['http://whc.unesco.org/en/news/mode=list&date=2015-12-01&calendarmode=year&maxrows=198',
                  'http://whc.unesco.org/en/news/mode=list&date=2016-12-01&calendarmode=year&maxrows=183',
                  'http://whc.unesco.org/en/news/mode=list&date=2017-12-01&calendarmode=year&maxrows=137',
                  'http://whc.unesco.org/en/news/mode=list&date=2018-12-01&calendarmode=year&maxrows=141',
                  'http://whc.unesco.org/en/news/mode=list&date=2020-12-01&calendarmode=year&maxrows=75']

    def parse(self, response):
        selector = Selector(text=response.text)
        name = selector.xpath(
            '//div[@class="box "]/div[@class="box-header box-padding-m"]/h5/a/descendant-or-self::text()').extract()
        time = selector.xpath('//div[@class="box "]/div[@class="box-header box-padding-m"]/h5/span/text()').extract()
        src = selector.xpath('//div[@class="box "]/div[@class="box-header box-padding-m"]/a/img/@src').extract()
        img_src = []
        for i in src:
            i = urljoin('http://whc.unesco.org/', i)
            img_src.append(i)
        detail_src = selector.xpath('//div[@class="box "]/div[@class="box-header box-padding-m"]/a/@href').extract()
        detail = selector.xpath('//div[@class="ym-gbox-right"]/div/div[@class="box "]/text()').extract()
        Detail = []
        for d in detail:
            D = d.strip()
            if D != '':
                Detail.append(D)
        L = len(img_src)
        i =0
        print(response.url)
        while i < L:
            item = UnesconewsItem()
            if '2015' in response.url:
                item["year"] = 2015
            elif '2016' in response.url:
                item["year"] = 2016
            elif '2017' in response.url:
                item["year"] = 2017
            elif '2018' in response.url:
                item["year"] = 2018
            elif '2019' in response.url:
                item["year"] = 2019
            elif '2019' in response.url:
                item["year"] = 2020
            else:
                item["year"] = 2020
            item["name"] = name[i]
            item["time"] = time[i]
            item["img_src"] = img_src[i]
            # item["detail"] = detail[i]
            item["sdetail"] = Detail[i]
            yield Request(urljoin(response.url, detail_src[i]), callback=self.detail_process, meta={"item": item})
            i = i + 1


    def detail_process(self,response):
        selector = Selector(text=response.text)
        item = response.meta['item']
        d = selector.xpath('//div[@class="content-full-body text-align-normal nopadding-top"]/div[@class="readable article-body"]/descendant-or-self::text()').extract()
        detail = ''
        for i in d:
            j = i.strip()
            if j != '':
                detail = detail + j
        src = []
        img_src = selector.xpath('//div[@class="bordered icaption "]/a/img/@data-src').extract()
        for i in img_src:
            j = 'http://whc.unesco.org' + i
            src.append(j)
        item["Detail"] = detail
        item["dsrc"] = src
        yield item