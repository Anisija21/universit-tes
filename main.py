import requests
from bs4 import BeautifulSoup

url = 'http://www.aiknc.lv/lv/list.php'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

a = soup.find_all(href="desc.php?id=1")
for a in a:
  print(a.text)
b = soup.find_all(href="desc.php?id=36")
for b in b:
  print(b.text)
c = soup.find_all(href="desc.php?id=36")
for c in c:
  print(c.text)
d = soup.find_all(href="desc.php?id=15")
for d in d:
  print(d.text)
f = soup.find_all(href="desc.php?id=2")
for f in f:
  print(f.text)
g = soup.find_all(href="desc.php?id=38")
for g in g:
  print(g.text)





