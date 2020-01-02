from typing import List
from abc import ABCMeta, abstractmethod
from common.database import Database


class Model(metaclass=ABCMeta):
    colletion = "models"

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def json(self):
        raise NotImplementedError

    @classmethod
    def all(cls) -> List:
        elements_from_db = Database.find(cls.collection, {})
        return [cls(**elem) for elem in elements_from_db]
        


