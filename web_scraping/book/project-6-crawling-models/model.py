import requests
from bs4 import BeautifulSoup

class Content:
  def __init__(self, url, title, body):
    self.url = url
    self.title = title
    self.body = body

def get_page(url):
  req = requests.get(url)
  # print(req)
  return BeautifulSoup(req.text, 'html.parser')

def scrape_nytimes(url):
  bs = get_page(url)
  title = bs.find('h1').text
  lines = bs.find_all('p', {'class': 'story-content'})
  body = '\n'.join([line.text for line in lines])
  return Content(url, title, body)

def scrape_brookings(url):
  bs = get_page(url)
  title = bs.find('h1').text
  lines = bs.find_all('div', {'class': 'post-body'})
  body = '\n'.join([line.text for line in lines])
  return Content(url, title, body)

# url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'
# content = scrape_nytimes(url)

url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'
content = scrape_brookings(url)

print('Title:\n{}\nURL:\n{}\nBody:\n{}'.format(content.title, content.url, content.body))
