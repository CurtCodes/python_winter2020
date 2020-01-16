import requests # makes you get the http/https requests
import html5lib # small parser package for html-5
from bs4 import BeautifulSoup

amazon_url="https://www.amazon.com/HP-Touchscreen-Computer-Quard-Core-802-11ac/dp/B082PZVZB7/ref=sr_1_1_sspa?keywords=laptop&qid=1579030356&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFUTTJWQlcwU1hIQzImZW5jcnlwdGVkSWQ9QTA5MTY3MTVVUTRDVlVQNlFXQUsmZW5jcnlwdGVkQWRJZD1BMDUwMDEwMDFGQzJaRkwzSVYzOE0md2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"

# NOTE
# A dictionary has a key and a value.
# "Key":"Value"

agent_header={
    "User-Agent": agent
}
amazon_page = requests.get(amazon_url, headers=agent_header)

# print(type(amazon_page))
soup = BeautifulSoup(amazon_page.content, "html5lib")
# print(soup.prettify())

# search for a specific ID in the soup
price_span=str(soup.find(id="priceblock_ourprice"))
print(price_span)

price=''
for char in price_span:
    if char.isdigit() is True:
        price+=char
    if char=='.':
        price+=char

print(price)
price =float(price)
max_price=800

if price<=max_price:
    print("yo buy it now")
else:
    print("Make more money")