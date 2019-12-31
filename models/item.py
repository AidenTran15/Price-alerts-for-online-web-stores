import re
import requests
from bs4 import BeautifulSoup


class Item:
    def __init__(self, url, tag_name, query):
        self.url = "https://www.apple.com/au/shop/buy-mac/macbook-pro/13-inch"
        self.tag_name = tag_name
        self.query = query
        self.price = None

    def loan_price(self):
        response = requests.get(self.url)
        content = response = response.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d*\.\d\d)") 
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)
            return self.price