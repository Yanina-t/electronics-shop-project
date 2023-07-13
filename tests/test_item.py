# """Здесь надо написать тесты с использованием pytest для модуля item."""
from pathlib import Path, WindowsPath
from src.item import Item

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
    price = 20
    quantity = 30
    assert price * quantity == 600

def test_apply_discount():
    price = 20
    pay_rate = 0.8
    price = price * pay_rate
    assert price == 16

def test_name():
    name = 'Смартфон'
    assert name == 'Смартфон'
    name = 'СуперСмартфон'
    name = name[:10]
    assert name == 'СуперСмарт'

def test_open_csv():
    ROOT_PATH = Path(__file__).parent
    OPERATION_PATH: Path = Path.joinpath(ROOT_PATH, 'fixture.csv')
    assert OPERATION_PATH == WindowsPath('C:/Users/админ/electronics-shop-project/tests/fixture.csv')

def test_string_to_number():
    num = '5'
    assert float(num) == 5
    num = '5.0'
    assert float(num) == 5
    num = '5.5'
    assert int(float(num)) == 5

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
