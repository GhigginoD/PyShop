from .item import Item
class OrderItem():
    def __init__(self, id_item:int, price:float, quantity:int):
        if quantity <= 0: raise Exception("negative quantity")
        self.id_item = id_item
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity