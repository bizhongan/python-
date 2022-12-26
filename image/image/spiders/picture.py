import scrapy
from ..items import ImageItem

class PictureSpider(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['iw233.cn']
    start_urls = ['https://iw233.cn/API/Random.php']
    count = 0
    Max = 200
    def parse(self, response):
        src = response.request.url
        item = ImageItem()
        item['src'] = [src]
        yield item

        self.count += 1

        if self.count <= self.Max:
            newurl = "https://iw233.cn/API/Random.php"
            yield scrapy.Request(url=newurl, dont_filter = True)
