from scrapy import Spider 

class SeiyuuSpider(Spider):
    allowed_domains = ['myanimelist.net']
    name = "seiyuu"
    start_urls = [
        # 'file:///C:/Users/dell/Desktop/mal_people.html'
        'https://myanimelist.net/people.php?letter=A'
    ]
    def parse(self, response):
        for tr in response.css("#content>table>tr"):
            name = tr.css('td.borderClass>a').extract_first()
            yield {
                'name':name
                }

        # next_page = response.css("#content>div.borderClass>div.spaceit>span.bgColor1>a::attr(href)").extract_first()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)