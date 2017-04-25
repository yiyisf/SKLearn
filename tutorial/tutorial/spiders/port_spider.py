import scrapy
import MySQLdb


# db = MySQLdb.connect(host='192.168.1.200:3305', user='root', passwd='slysSE4RFV', db='data_explorer')
#
# print()

# 抓取海关信息
class PortSpider(scrapy.Spider):
    name = 'port'

    def start_requests(self):
        urls = [
            'http://www.customs.gov.cn/publish/portal0/tab3795/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('tables have:' + str(len(response.xpath('//table'))))
        # print(response.xpath('//table[@class="datagrid-main"]/tr').extract())
        # print(response.xpath('//table[@class="datagrid-main"]/tr'))
        # print(response.xpath('//table').extract())

        ports = response.xpath('//table[@class="datagrid-main"]/tr')
        for i, port in enumerate(ports):
            print('index '+ str(i) , port.xpath('td/text()').extract())

