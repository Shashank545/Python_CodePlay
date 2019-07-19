# to make URL request
import urllib.request
# to take care of browser query encodings
import urllib.parse


values = {'q':'python programming tutorial'}
data = urllib.parse.urlencode(values)
#print(data)
#data = data.encode('utf-8')
#print(data)
url = 'https://www.google.com/search?'+data
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

# It is similar to class (self, *args, **kwargs)
req = urllib.request.Request(url, headers = headers)
#print(type(req))
resp = urllib.request.urlopen(req)
resp_data = resp.read()
print(resp_data)

'''
req = urllib.request.urlopen('https://www.google.com')
print(type(req))
print(req.read())

'''