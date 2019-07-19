from bs4 import BeautifulSoup
import urllib.request
import time

req = urllib.request.urlopen('http://www.nationaljournal.com/politics?rss=1')

xml = BeautifulSoup(req, 'xml')

for item in xml.findAll('link')[3:]:
    url = item.text
    news = urllib.request.urlopen(url).read()
    
    page = BeautifulSoup(news)

    for p in page.findAll('p'):
        print(p.text)

    time.sleep(10)
    

