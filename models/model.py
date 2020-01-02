from abc import ABCMeta, abstractmethod


class Model(metaclass=ABCMeta):
    @abstractmethod
    def json(self):
        raise NotImplementedError

class MyModel(Model):
    def json(self):
        return {
            "name": "My Model"
        }

model = MyModel()
print(model.json())
