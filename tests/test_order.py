from source.cpf import Cpf
from source.order import Order
from source.item import Item

def test_deve_criar_um_pedido():
    cpf = Cpf("879.444.500-12")
    order = Order(cpf)
    total = order.get_quantity_items()
    assert total == 0

def test_deve_adicionar_um_item_com_quantidade_negativa():
    try:
        cpf = Cpf("879.444.500-12")
        order = Order(cpf=cpf)
        order.add_item(Item(),-1)
    except Exception as exception:
        assert "negative quantity" in str(exception)

def test_deve_aumentar_a_quantidade_ao_inserir_itens_repetidos():
    cpf = Cpf("879.444.500-12")
    order = Order(cpf=cpf)
    order.add_item(Item(),1)
    order.add_item(Item(),2)
    assert order.get_quantity_items() == 1
    assert order.order_items[0].quantity == 3
