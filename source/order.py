from source.item import Item
from .orderItem import OrderItem
class Order():
    
    def __init__(self, cpf):
        self.cpf = cpf
        self.total_items = 0
        self.order_items: list[OrderItem] = []

    def add_item(self, item: Item, quantity:int) -> None:
        order_item = OrderItem(item, quantity)
        if item.idItem in self.get_items_in_order(): 
            self.update_quantity_item(item, quantity)
            return 
        self.order_items.append(order_item)
    
    def update_quantity_item(self, item: Item, quantity: int) -> None:
        self.order_items[self.get_items_in_order().index(item.idItem)].quantity += quantity

    def get_quantity_items(self) -> int:
        return len(self.order_items)
    
    def get_items_in_order(self) -> list:
        return [order_item.item.idItem for order_item in self.order_items]
    

