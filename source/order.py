import datetime
from typing import Union
from source.cpf import Cpf
from source.item import Item
from source.coupon import Coupon
from .orderItem import OrderItem
class Order():
    coupon: Union[Coupon, None] = None

    def __init__(self, cpf:Cpf, date=datetime.datetime.now()):
        self.cpf = cpf
        self.order_items: list[OrderItem] = []
        self.date_created = date.strftime('%Y-%m-%dT%H:%M:%S')

    def add_item(self, item: Item, quantity:int) -> None:
        order_item = OrderItem(item.id_item, item.price, quantity)
        if item.id_item in self.get_items_in_order(): 
            return self.update_quantity_item(item, quantity)
        self.order_items.append(order_item)
    
    def add_coupon(self, new_coupon: Coupon) -> None:
        if self.coupon: raise Exception("there is coupon in order")
        if new_coupon.is_expired(self.date_created): raise Exception("coupon invalid")
        self.coupon = new_coupon

    def update_quantity_item(self, item: Item, quantity: int) -> None:
        self.order_items[self.get_items_in_order().index(item.id_item)].quantity += quantity

    def get_quantity_items(self) -> int:
        return len(self.order_items)
    
    def get_items_in_order(self) -> list:
        return [order_item.id_item for order_item in self.order_items]
    
    def get_total(self) -> float:
        return sum(order_item.get_total() for order_item in self.order_items)
