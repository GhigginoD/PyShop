from source.dimension import Dimension
class Item():
    def __init__(self, price:int=0, id_item:int=0, description:str='', dimension:Dimension = Dimension(0,0,0,0)):
        self.price = price
        self.id_item = id_item
        self.description = description
        self.dimension = dimension
    
    def get_volume(self) -> int:
        return self.dimension.get_volume()
    
    def get_density(self) -> int:
        return self.dimension.get_density()