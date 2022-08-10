from source.coupon import Coupon
def test_deve_criar_um_cupom():
    assert Coupon('VALE10', 10, '2002-12-20T10:00:00')

def test_deve_aplicar_deconto_do_coupon(): 
    coupon = Coupon('VALE10', 10, '2032-12-20T10:00:00')
    total = 100    
    new_total = total - coupon.getDiscount(total)
    assert new_total == 90

def test_deve_criar_cupon_expirado(): 
    coupon = Coupon('VALE10', 10, '2032-04-20T10:00:00')
    isExpired = coupon.isExpired() 
    assert isExpired == False   

def test_deve_retornar_o_valor_integral_da_compra_cupons_expirados():
    coupon = Coupon('VALE10', 10, '2002-12-20T10:00:00')
    total = 100    
    new_total = total - coupon.getDiscount(total)
    assert new_total == 100