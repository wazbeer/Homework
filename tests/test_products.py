import pytest

from src.products import Product


@pytest.fixture
def product():
    return Product("name", "description", 1.0, 1)


@pytest.fixture
def product_dict():
    return {"name": "name", "description": "description", "price": 1.0, "quantity": 1}


def test_product(product):
    assert product.name == "name"
    assert product.description == "description"
    assert product.price == 1.0
    assert product.quantity == 1


def test_negative_price(product):
    product.price = -1.0
    assert product.price == 1.0


def test_zero_price(product):
    product.price = 0.0
    assert product.price == 1.0


def test_new_product_price(product):
    product.price = 2.0
    assert product.price == 2.0


def test_product_data(product_dict):
    new_product = Product.new_product(product_dict)
    assert new_product.name == "name"
    assert new_product.description == "description"
    assert new_product.price == 1.0
    assert new_product.quantity == 1
