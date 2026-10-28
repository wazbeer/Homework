import pytest

from src.products import Product


@pytest.fixture
def product():
    return Product("name", "description", 1.0, 1)


def test_product(product):
    assert product.name == "name"
    assert product.description == "description"
    assert product.price == 1.0
    assert product.quantity == 1
