import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input ('Enter Url - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Isak.html"
position = input ('Enter Position - ')
count = input ('Enter count - ')
print(url)
i = 0
while i < int(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[int(position)-1]
    url = tag.get('href',None)
    print(url)
    i += 1
#    soup = BeautifulSoup(html2, 'html.parser')
#    tag = tags[3]
#    print(tag.decode().strip())
