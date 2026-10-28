import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def product_1():
    return Product("Product 1", "description 1", 1.0, 1)


@pytest.fixture
def product_2():
    return Product("Product 2", "description 2", 2.0, 1)


@pytest.fixture
def product_3():
    return Product("Product 3", "description 3", 3.0, 1)


@pytest.fixture
def category(product_1, product_2):
    return Category("Category 1", "description", [product_1, product_2])


def test_category(category):
    assert category.name == "Category 1"
    assert category.description == "description"


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0


def test_category_count(category: Category, product_3):
    assert Category.category_count == 1
    assert Category.product_count == 2

    Category("category 2", "description 2", [product_3])

    assert Category.category_count == 2
    assert Category.product_count == 3
