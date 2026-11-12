from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict):
        pass  # pragma: no cover

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        else:
            return (self.price * self.quantity) + (other.price * other.quantity)


class PrintMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print(
            f"{self.__class__.__name__}({self.name!r}, {self.description!r}, {self.price!r}, {self.quantity!r})"  # type: ignore[attr-defined]
        )


class Product(PrintMixin, BaseProduct):
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
