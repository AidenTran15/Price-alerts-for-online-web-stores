from typing import Dict
import re
import requests
import uuid
from dataclasses import dataclass, field
from bs4 import BeautifulSoup
from models.model import Model
from common.database import Database

@dataclass(eq=Fasle)
class Item(Model):
    collection = str = field(init=False, default="items")
    url: str
    tag_name: str
    query: Dict
    price: float = field(default=None)
    _id: str = field(default_factory=lambda: uuid.uuid4())

    def load_price(self) -> float:
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d*\.\d\d)") 
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)
        return self.price

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "price": self.price,
            "query": self.query
        }


    def save_to_mongo(self):
        Database.insert(self.collection, self.json())

    @classmethod
    def get_by_id(cls, _id: str) -> "Item":
        item_json = Database.find_one("items", {"_id": _id})
        return cls(**item_json)

