from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('http://www.nationaljournal.com/politics?rss=1')

xml = BeautifulSoup(req, 'xml')

for item in xml.findAll('link')[3:]:
    url = item.text
    news = urllib.request.urlopen(url).read()
    print(news)
    print(20*"#")
