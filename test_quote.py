import pytest


from quote import build_quote




def hammer(quantity, stock=12):
    return {
        "id": 1,
        "name": "Hammer",
        "price": 10.0,
        "stock": stock,
        "quantity": quantity,
    }




def test_quantity_below_one_is_rejected():
    with pytest.raises(ValueError, match="at least 1"):
        build_quote([hammer(0)])




def test_small_order_has_no_discount():
    quote = build_quote([hammer(2)])
    assert quote["subtotal"] == 20.0
    assert quote["discount"] == 0.0
    assert quote["tax"] == 1.0
    assert quote["total"] == 21.0
    assert quote["code"] == "673aeeb0"


