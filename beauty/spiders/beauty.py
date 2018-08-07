from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


import scrapy
from ..items import BeautyItem
import proxy



#class BeautySpider(CrawlSpider):
class BeautySpider(scrapy.Spider):
    print('start generate proxy ip')
    proxy.get_proxy()
    
    name = 'siwa'
    allowed_domains = ['www.27270.com']
    start_urls = [
	'http://www.27270.com/tag/384.html',
	'http://www.27270.com/tag/513.html',
    	'http://www.27270.com/tag/782.html',
	'http://www.27270.com/tag/35.html',
	'http://www.27270.com/tag/288.html',
	'http://www.27270.com/tag/441.html',
	]

    num = 1
    items_per_page = 0

    def parse(self, response):
		items = []
        # write the category page data extraction code here
#		global num
#		num += 1

		for li in response.xpath('//ul[@id="Tag_list"]'):
			print(li)
			titles = li.xpath('li/a/@title').extract()
			imgs = li.xpath('li/a/img/@src').extract()
			pages = li.xpath('li/a/@href').extract()
			print(titles,imgs,pages)
		total = len(titles)
		print(total)

		for i in range(total):
			print(titles[i],pages[i])
			yield scrapy.Request(pages[i],callback=self.parse_beauty)
		self.logger.debug('callback "parse": got response %r' % response)

		while total <= 30:   #There is 30 items per page
			next_page = response.xpath('//div[@class="TagPage"]/ul/li/a/@href').extract()[-2]
			url = 'http://www.27270.com' + next_page
			yield scrapy.Request(url, callback=self.parse)


    def parse_beauty(self, response):
	if response.status==200:	
		detail = response.xpath('//div[@id="picBody"]')
		title = detail.xpath('p/a/img/@alt').extract()[0]
		image_url = detail.xpath('p/a/img/@src').extract()[0]
		print(title,image_url)

		beauty = BeautyItem()	
		beauty['title'] = title
		beauty['image_urls'] = [image_url]

		yield beauty
		self.logger.debug('callback "parse": got response %r' % response)
		
		pages = response.xpath('//ul[@class="articleV4Page l"]')
		total_pages = pages.xpath('li[@class="hide"]/@pageinfo').extract()[0]
		next_page = pages.xpath('li[@id="nl"]/a/@href').extract()[0]
		
		#url = request.url
		#next_page_url = '/'.join(url.split('/')[0:-1]) + '/' + next_page
		next_page_url = '/'.join(image_url.split('/')[0:-1]) + '/' + next_page
		print(title,image_url)
		print('scrath for next page', next_page_url)
		#yield scrapy.Request(url, callback=self.parse_beauty)
		yield scrapy.Request(next_page_url, callback=self.parse_beauty)
	else:
		print('request url:',request.url,'returned error')
		scrapy.Request(request.url, callback=self.parse_beauty)
		self.logger.debug('callback "parse": got response %r' % response)
