import scrapy
from demo.items import DouBanItem
from scrapy.loader import ItemLoader

class DoubanSpiderSpider(scrapy.Spider):
    name = "douban_spider"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "https://movie.douban.com/top250"
        ]
    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
            "referrer":'https://movie.douban.com/'
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse,headers=headers)
    def parse(self, response):
        # print(response.text)
        # for movie in response.css('div.item'):
        #     yield {
        #         'title': movie.css('span.title::text').get(),
        #         'rating': movie.css('span.rating_num::text').get(),
        #         'quote': movie.css('p.quote span::text').get(),
        #     }
        # # 处理分页
        # next_page = response.css('span.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
        
        movies = response.css('.item')
        for movie in movies:
            loader = ItemLoader(item=DouBanItem(), selector=movie)
            
            # 使用ItemLoader填充字段
            loader.add_css('rating', 'span.rating_num::text')
            loader.add_css('quote', 'p.quote span::text')
            loader.add_css('title', 'span.title:nth-child(1)::text')

            
            yield loader.load_item()
