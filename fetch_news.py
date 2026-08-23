import urllib.request
import json
import xml.etree.ElementTree as ET

urls = [
    "https://news.google.com/rss/search?q=Vaca+Muerta+Argentina",
    "https://news.google.com/rss/search?q=Litio+Argentina",
    "https://news.google.com/rss/search?q=Cobre+RIGI+Argentina",
    "https://news.google.com/rss/search?q=Corredor+Bioceanico+Argentina"
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read()
        root = ET.fromstring(html)
        print("--- " + url + " ---")
        for item in root.findall('./channel/item')[:3]:
            print(item.find('title').text)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
