class Dish():
    def __init__(self, name, price):
        if type(name) != str:
            raise Exception("name should be a string")
        elif type(price) != float:
            raise Exception("price should be a float")
        self.name = name
        self.price = price
    