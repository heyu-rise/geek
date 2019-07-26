# assert 1 == 2, 'hello word'


def apply_discount(price, discount):
    update_price = price * (1 - discount)
    assert 0 <= update_price <= price, '折扣异常'
    return update_price


print(apply_discount(100, 0.1))


