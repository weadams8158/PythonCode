import urllib.request, urllib.parse, urllib.error
import json

url = input ('Enter Url - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_40195.json"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
js = json.loads(data)
print('User count:', len(js))
tot=0
i=0
while i < len(js["comments"]) :
  tot = tot + js["comments"][i]["count"]
  i = i+1
print (tot)
