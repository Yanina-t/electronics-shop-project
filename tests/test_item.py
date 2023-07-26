# """Здесь надо написать тесты с использованием pytest для модуля item."""
from pathlib import Path

import pytest

from src.items import Item, InstantiateCSVError
from src.phone import Phone

def test_initial_value():
    obj_1 = Item("Test_1", 20.5, 100)
    assert obj_1.name == "Test_1"
    assert obj_1.price == 20.5
    assert obj_1.quantity == 100
    item1 = Item.all[0]
    assert item1.name == "Test_1"


def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test__str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_calculate_total_price():
    item1 = Item("Смартфон", 20, 30)
    assert item1.calculate_total_price() == 600

def test_apply_discount():
    item1 = Item("Смартфон", 200, 30)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 160

def test_name():
    item1 = Item("Смартфон", 200, 30)
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    with pytest.raises(InstantiateCSVError, match='Файл items_test.csv поврежден'):
        Item.OPERATION_PATH = Path.joinpath(Item.ROOT_PATH, 'items_test.csv')
        Item.instantiate_from_csv()

    with pytest.raises(FileNotFoundError, match='Отсутствует файл item.csv'):
        Item.OPERATION_PATH = Path.joinpath(Item.ROOT_PATH, 'item.csv')
        Item.instantiate_from_csv()


def test__add__():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

