from models.item import Item

url = "https://www.apple.com/au/shop/buy-mac/macbook-pro/13-inch"
tag_name = "span"
query = {"class": "as-price-currentprice"}

ipad = Item(url, tag_name, query)
ipad.save_to_mongo()

# items_loaded = Item.all()
# print(items_loaded)
# print(items_loaded[0].load_price())


# import requests
# from bs4 import BeautifulSoup
# import re

# URL="https://www.apple.com/au/shop/buy-mac/macbook-pro/13-inch"
# TAG_NAME = "span"
# QUERY = {"class":"as-price-currentprice"}

# response = requests.get(URL)
# content = response = response.content
# soup = BeautifulSoup(content, "html.parser")
# element = soup.find(TAG_NAME, QUERY)
# string_price = element.text.strip()

# pattern = re.compile(r"(\d+,?\d*\.\d\d)") 
# match = pattern.search(string_price)
# found_price = match.group(1)
# without_commas = found_price.replace(",", "")
# price = float(without_commas)

# print(price)