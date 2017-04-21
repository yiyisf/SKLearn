import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"

    def start_requests(self):
        urls = [
            'http://news.baidu.com/',
            'http://baijia.baidu.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('//')[1].split('.')[0]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)