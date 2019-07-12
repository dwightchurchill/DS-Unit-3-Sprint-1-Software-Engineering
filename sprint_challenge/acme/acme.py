import random

class Product(object):

    def __init__(self, name: str,
               price: int = 10,
               weight: int = 20,
               flammability: float = 0.5,
               identifier: int = random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        score = self.price / self.weight
        if (score < 0.5):
            return "Not so stealable..."
        elif (score >= 0.5) and (score < 1.0):
            return "Kind stealable..."
        else:
            return "Very stealable!"

    def explode(self):
        score = self.flammability * self.weight
        if (score < 10):
            return "...fizzle"
        elif (score >= 10) and (score < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):

    def __init__(self, name: str,
               price: int = 10,
               weight: int = 10,
               flammability: float = 0.5,
               identifier: int = random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if (self.weight < 5):
            return "That tickles."
        elif (self.weight >= 5) and (self.weight < 15):
            return "Hey that hurt!"
        else:
            return "OUCH!"

