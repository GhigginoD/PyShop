from source.coupon import Coupon
from source.cpf import Cpf
from source.order import Order
from source.item import Item

def test_deve_criar_um_pedido():
    cpf = Cpf("879.444.500-12")
    order = Order(cpf)
    quant_items = order.get_quantity_items()
    total = order.get_total()
    assert quant_items == 0
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

def test_deve_gerar_erro_ao_inserir_dois_cupons_no_pedido():
    cpf = Cpf("879.444.500-12")
    order = Order(cpf=cpf)
    coupon = Coupon('VALE10', 10, "2023-04-20T10:00:00")
    coupon2 = Coupon('VALE20', 20, "2024-04-20T10:00:00")
    try:
        order.add_coupon(coupon)
        order.add_coupon(coupon2)
    except Exception as exception:
        assert "there is coupon in order" in str(exception)

def test_deve_gerar_erro_ao_inserir_coupon_invalido():
    cpf = Cpf("879.444.500-12")
    order = Order(cpf=cpf)
    coupon = Coupon('VALE10', 10, "2012-04-20T10:00:00")
    try:
        order.add_coupon(coupon)
    except Exception as exception:
        assert "coupon invalid" in str(exception)