import scrapy

from ..items import MessageItem
from ..database.messageDB import ForumDatabase


class MessSpider(scrapy.Spider):
    name = "messages"

    def start_requests(self):
        db = ForumDatabase()

        urls = []
        for title in db.get_titles():
            for i in range(1, int(title["page_count"])):
                urls.insert(len(urls), title['url'] + "?page=" + str(i))
            # urls.insert(len(urls), title['url'] )
        db.close()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # title = response.css("span.crumblast a::text").extract_first()
        # for message in response.css("div.post"):
        title = response.css("div.item-box h1::text").extract_first()
        for message in response.css("li.tForum"):
            item = MessageItem()
            item['text'] = message.css("p::text").extract_first()
            item['author'] = message.css("li.pull-right span::text").extract_first()
            item['date'] = message.css("ul.list-inline:nth-of-type(2) li:nth-of-type(7)::text").extract_first()

            # item['text'] = message.css("div.entry-content p::text").extract_first()
            # item['author'] = message.css("em a::text").extract_first()
            # item['date'] = message.css("span.post-link a::text").extract_first()
            item['title_name'] = title
            yield item

        next_page_url = response.css("a.Next::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
