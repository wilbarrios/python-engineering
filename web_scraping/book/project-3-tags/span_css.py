from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')

print(html)

name_list = bs.findAll('span', {'class': 'green'})
for name in name_list:
    print(name.get_text())
