import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.Request("https://www.abuseipdb.com/sitemap?page=1",headers={'User-Agent': 'Mozilla/5.0'})

rawsite = urllib.request.urlopen(req)
content = rawsite.read().decode('utf-8')
soup = BeautifulSoup(content, 'html.parser')

res = soup.find(class_="col-md-4").find_all("a")
filtered = map(lambda ip : ip.contents[0], res )
print(list(filtered))