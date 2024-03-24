import pytest
from project import (
    read_products, update_products,
    read_info, update_info,
    read_users, update_users
)

def test_read_products():
    products = read_products()
    assert isinstance(products, list)

def test_read_info():
    info = read_info()
    assert isinstance(info, list)

def test_update_info():
    # Create dummy data for testing
    dummy_info = [
        {"receipt_code": 2}, {"currency_type": "€"}, {"company_name": "Sample Company"}, {
            "current_role": "c"}, {"current_cashier": "cashier1"}
    ]
    update_info(dummy_info)
    updated_info = read_info()
    assert updated_info[0]["receipt_code"] == 2

def test_read_users():
    users = read_users()
    assert isinstance(users, list)

