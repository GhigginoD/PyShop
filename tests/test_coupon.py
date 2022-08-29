from source.coupon import Coupon
def test_deve_criar_um_cupom():
    assert Coupon('VALE10', 10, '2002-12-20T10:00:00')

def test_deve_aplicar_deconto_do_coupon(): 
    coupon = Coupon('VALE10', 10, '2032-12-20T10:00:00')
    total = 100    
    new_total = total - coupon.get_discount(total)
    assert new_total == 90

def test_deve_criar_cupon_expirado(): 
    coupon = Coupon('VALE10', 10, '2032-04-20T10:00:00')
    is_expired = coupon.is_expired("2042-03-05T10:00:00") 
    assert is_expired == True