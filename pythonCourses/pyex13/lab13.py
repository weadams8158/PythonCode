import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#if api_key is False:
#    api_key = 42
#    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
#else :
#    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_40194.xml'
#uh = urllib.request.urlopen(url, context=ctx)
uh = urllib.request.urlopen(url)
data = uh.read()
# print(data.decode())
totcnt = 0
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for cnt in counts:
#    print('count:', cnt.text)
    totcnt = totcnt + int(cnt.text)
print('totcnt: ',totcnt)
