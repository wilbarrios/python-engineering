from scrapy import Spider, Request
# print(dir(scrapy))

class BooksSpider(Spider):
  name = "books" # This has to be unique

  def start_requests(self): # This is overriding Spider method
    return [
      Request(url = "http://books.toscrape.com", callback = self.parse)
    ]
  
  def parse(self, response):
    print(response.body)
