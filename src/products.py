class Product:
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.price} {self.quantity} шт."

    def __add__(self, other) -> float:
        return (self.price * self.quantity) + (other.price * other.quantity)