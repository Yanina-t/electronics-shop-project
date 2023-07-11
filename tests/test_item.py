# """Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_calculate_total_price():
    price = 20
    quantity = 30
    assert price * quantity == 600


def test_apply_discount():
    price = 20
    pay_rate = 0.8
    price = price * pay_rate
    assert price == 16
