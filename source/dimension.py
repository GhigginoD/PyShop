class Dimension:
    def __init__(self, height:int, lenght:int, width:int, weight:int):
        self.width = width
        self.weight = weight
        self.lenght = lenght
        self.height = height
        if self.is_invalid_dimension():
            raise Exception("invalid dimensions")
    
    def is_invalid_dimension(self) -> bool:
       return bool((self.weight<0) or (self.width<0) or (self.lenght<0) or (self.height<0))
    
    def get_volume(self) -> int:
        return (self.height * self.lenght * self.width) / 100
    
    def get_density(self) -> int:
        return self.weight / self.get_volume()
        