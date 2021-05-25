import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
total = 0
spans = soup('span')
for span in spans:
    num = int(span.contents[0])
    count = count + 1
    total = total + num

print('Count', count)
print('Sum', total)
