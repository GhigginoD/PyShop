from .item import Item
class OrderItem():
    def __init__(self, item:Item, quantity:int):
         if quantity <= 0: raise Exception("negative quantity")
         self.item = item
         self.quantity = quantity