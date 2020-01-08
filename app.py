import os
from flask import Flask
from views.stores import store_blueprint
from views.alerts import alert_blueprint
from views.users import user_blueprint

app = Flask(__name__)
app.secret_key = os.urandom(64)

app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(user_blueprint, url_prefix="/users")

if __name__ == '__main__':
    app.run(debug=True)




















# from models.item import Item

# url = "https://www.apple.com/au/shop/buy-mac/macbook-pro/13-inch"
# tag_name = "span"
# query = {"class": "as-price-currentprice"}

# ipad = Item(url, tag_name, query)
# ipad.save_to_mongo()

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

