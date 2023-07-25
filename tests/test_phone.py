import pytest

from src.phone import Phone

def test_initial_value():
    obj_1 = Phone("Test_1", 20.5, 100, 12)
    assert obj_1.name == "Test_1"
    assert obj_1.price == 20.5
    assert obj_1.quantity == 100
    assert obj_1.number_of_sim == 12

def test__repr__():
    phone1 = Phone("Смартфон", 10000, 20, 12)
    assert repr(phone1) == "Phone('Смартфон', 10000, 20, 12)"

def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120000, 5, 0)
