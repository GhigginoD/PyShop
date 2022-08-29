from source.item import Item

class Freight:
    MIN_FREIGHT = 10
    @classmethod
    def calculate(cls, item: Item) -> float:
        return max(item.get_volume() * 1000 * (item.get_density()/100 ), cls.MIN_FREIGHT)