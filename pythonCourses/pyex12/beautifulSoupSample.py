import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input ('Enter - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_40192.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
num = 0
tags = soup('span')
for tag in tags:
    val = re.findall('[0-9]+',tag.decode())
    num = num + int(val[0])
print(num)
