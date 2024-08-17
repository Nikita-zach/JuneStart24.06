from .discount_module import *
from .error_module import *
from .log_module import *
from .payment_module import *


class Product:
    """
    Class for product representation.

    name: The name of the product.
    price: The price of the product.
    currency: The currency of the product price (default: 'UAH').
    """

    def __init__(self, name: str, price: int | float, currency='UAH'):
        if not isinstance(price, int | float):
            raise TypeError(f"Entered text {price} instead of of number ")
        if price <= 0:
            raise InvalidPriceError(price, f"Price must be a positive number")
        self.name = name
        self.price = price
        self.currency = currency

    def __str__(self):
        """
        Return a string representation of the product.
        """
        return f'{self.name}: {self.price:.2f} {self.currency}'


class Cart(DiscountMixin, LoggingMixin):
    """
    Class for representing a shopping cart.

    product: The product to add to the cart.
    quantity: The quantity of the product to add (default: 1).
    payment_method: The payment method to use for processing the payment.
    """

    def __init__(self):
        super().__init__()
        self.products = {}

    def add_product(self, product: Product, quantity: int | float = 1):
        """
        Add a product to the cart with a specified quantity.
        """
        if not isinstance(quantity, int | float):
            raise TypeError("Quantity must be a number")
        if quantity <= 0:
            raise InvalidQuantityError(quantity, "Quantity can't be a negative number nor equal zero")
        self.log(f"{product} x {quantity} were added to cart")
        self.products[product] = self.products.get(product, 0) + quantity

    def total_cost(self):
        """
        Calculate the total cost of all products in the cart.
        """
        return sum(product.price * quantity for product, quantity in self.products.items())

    def pay(self, payment_method: PaymentProcessor):
        """
        Process payment using the specified payment method.
        """
        amount = self.total_cost()
        self.log(f"{self.total_cost()} were paid with {payment_method.__class__.__name__.replace('Processor', '')}")
        print(payment_method.pay(amount))

    def __str__(self):
        """
        Return a string representation of the cart contents.
        """
        return '\n'.join([f'{product} x {quantity} = {product.price * quantity} {product.currency}'
                          for product, quantity in self.products.items()])
