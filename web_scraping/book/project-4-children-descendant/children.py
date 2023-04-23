from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

print('==Children==')
for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)

print('==Descendant==')
for child in bs.find('table', {'id': 'giftList'}).descendants:
    print(child)

print('==Siblings==')
for child in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(child)
