from source.cpf import Cpf
from source.dimension import Dimension
from source.freight import Freight
from source.item import Item

def test_deve_calcular_o_valor_do_frete():
    dimension = Dimension(100,30,10,3)
    item = Item(100, 1, "caneca", dimension)
    freight = Freight.calculate(item)    
    assert freight == 30

def test_deve_calcular_com_o_frete_minimo():
    dimension = Dimension(10,10,10,0.5)
    item = Item(100, 1, "caneca", dimension)
    freight = Freight.calculate(item)    
    assert freight == 10