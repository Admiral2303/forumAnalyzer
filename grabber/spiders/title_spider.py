import scrapy
import math

from ..items import TitleItem


class TitleSpider(scrapy.Spider):
    name = "titles"

    def start_requests(self):
        # urls = ['http://replace.org.ua/forum/6/page/1/']
        urls = ['https://www.youth4work.com/Talent/C-Language/Forum?page=1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # for title in response.css("div.main-item"):
        for title in response.css("li.tForum"):
            item = TitleItem()
            item['name'] = str(title.css("a::text").extract_first()).strip()
            item['url'] = "https://www.youth4work.com/" + str(title.css("a::attr(href)").extract_first()).strip()
            posts = title.css("ul.list-inline li:nth-of-type(5)::text").extract_first()
            pages = math.ceil(int(posts.replace(" Answers", "")) / 20)
            item["page_count"] = pages
            yield item

        next_page_url = response.css("a.Next::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
