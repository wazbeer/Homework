import pytest

from src.products import BaseProduct, LawnGrass, Product, Smartphone


@pytest.fixture
def product():
    return Product("name", "description", 1.0, 1)


@pytest.fixture
def product_2():
    return Product("name", "description", 1.0, 1)


@pytest.fixture
def product_dict():
    return {"name": "name", "description": "description", "price": 1.0, "quantity": 1}


@pytest.fixture
def smartphone():
    return Smartphone("name", "description", 1.0, 1, 1.0, "model", 1, "color")


@pytest.fixture
def grass():
    return LawnGrass(
        "name", "description", 1.0, 1, "country", "germination_period", "color"
    )


def test_product(product):
    assert product.name == "name"
    assert product.description == "description"
    assert product.price == 1.0
    assert product.quantity == 1


def test_smartphone(smartphone):
    assert smartphone.name == "name"
    assert smartphone.description == "description"
    assert smartphone.price == 1.0
    assert smartphone.quantity == 1
    assert smartphone.efficiency == 1.0
    assert smartphone.model == "model"
    assert smartphone.memory == 1
    assert smartphone.color == "color"


def test_grass(grass):
    assert grass.name == "name"
    assert grass.description == "description"
    assert grass.price == 1.0
    assert grass.quantity == 1
    assert grass.country == "country"
    assert grass.germination_period == "germination_period"
    assert grass.color == "color"


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


def test_product_str(product):
    assert str(product) == "name, 1.0 руб. Остаток: 1 шт."


def test_product_add(product, product_2):
    assert product + product_2 == 2.0


def test_add_different_product_types(smartphone, grass):
    with pytest.raises(TypeError):
        _ = smartphone + grass


def test_print_mixin(capsys):
    Product("Product_1", "description", 1.0, 1)
    captured = capsys.readouterr()
    assert "Product('Product_1', 'description', 1.0, 1)" in captured.out


def test_BaseProduct():
    pytest.raises(TypeError, lambda: BaseProduct("Product_1", "description", 1.0, 1))


def test_smartphone_mixin(capsys):
    Smartphone("name", "description", 1.0, 1, 1.0, "model", 1, "color")
    captured = capsys.readouterr()
    assert "Smartphone('name', 'description', 1.0, 1)\n" in captured.out


def test_grass_mixin(capsys):
    LawnGrass("name", "description", 1.0, 1, "country", "germination_period", "color")
    captured = capsys.readouterr()
    assert "LawnGrass('name', 'description', 1.0, 1)\n" in captured.out


def test_MRO(smartphone, grass, product):
    assert issubclass(Smartphone, Product)
    assert issubclass(Smartphone, BaseProduct)
    assert issubclass(LawnGrass, Product)
    assert issubclass(LawnGrass, BaseProduct)
    assert not issubclass(LawnGrass, Smartphone)
    assert not issubclass(Smartphone, LawnGrass)
    assert isinstance(smartphone, BaseProduct)
    assert isinstance(smartphone, Smartphone)
    assert isinstance(smartphone, Product)
    assert not isinstance(smartphone, LawnGrass)
    assert isinstance(grass, BaseProduct)
    assert isinstance(grass, Product)
    assert isinstance(grass, LawnGrass)
