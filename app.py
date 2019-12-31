import requests
from bs4 import BeautifulSoup

URL="https://www.apple.com/au/shop/buy-mac/macbook-pro/13-inch"
TAG_NAME = "span"
QUERY = {"class":"as-price-currentprice"}

response = requests.get(URL)
content = response = response.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()

print(string_price)