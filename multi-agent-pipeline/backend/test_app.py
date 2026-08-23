import pytest
from app import Inventory, calculate_total


def test_add_item():
    inv = Inventory()
    assert inv.add_item("phone", 5) == 5
    assert inv.add_item("phone", 3) == 8


def test_remove_item():
    inv = Inventory()
    inv.add_item("phone", 5)
    assert inv.remove_item("phone", 2) == 3


def test_remove_item_insufficient_stock():
    inv = Inventory()
    inv.add_item("phone", 2)
    with pytest.raises(ValueError):
        inv.remove_item("phone", 5)


def test_calculate_total():
    assert calculate_total([10, 20], [2, 1]) == 40


def test_calculate_total_mismatched_lengths():
    with pytest.raises(ValueError):
        calculate_total([10, 20], [1])