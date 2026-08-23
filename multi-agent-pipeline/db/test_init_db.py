import pytest
from init_db import SimpleDB


def test_insert_and_count():
    db = SimpleDB()
    db.insert("users", {"id": 1, "name": "Alice"})
    assert db.count("users") == 1


def test_find_by_id():
    db = SimpleDB()
    db.insert("users", {"id": 1, "name": "Alice"})
    result = db.find_by_id("users", 1)
    assert result["name"] == "Alice"


def test_find_by_id_not_found():
    db = SimpleDB()
    assert db.find_by_id("users", 999) is None


def test_insert_invalid_table():
    db = SimpleDB()
    with pytest.raises(ValueError):
        db.insert("orders", {"id": 1})