from .log_module import *


class Discount:
    """
    Base class for discount strategies.

    price: The original price to which the discount will be applied.
    """

    def apply(self, price):
        """
        Apply discount to a given price. Should be overridden by subclasses.
        """
        raise NotImplementedError


class PercentageDiscount(Discount):
    """
    Discount strategy that applies a percentage discount.

    percentage: The discount percentage to apply.
    """

    def __init__(self, percentage):
        if not isinstance(percentage, int | float):
            raise TypeError("Percentage must be a number")
        self.percentage = percentage

    def apply(self, price):
        """
        Apply percentage discount to the given price.
        """
        price -= price * (self.percentage / 100)
        return price


class FixedAmountDiscount(Discount):
    """
    Discount strategy that applies a fixed amount discount.

    amount: The fixed amount to subtract from the price.
    """

    def __init__(self, amount):
        if not isinstance(amount, int | float):
            raise TypeError("Amount must be a number")
        self.amount = amount

    def apply(self, price):
        """
        Apply fixed amount discount to the given price.
        """
        price -= self.amount
        if price < 0:
            price = 0
        return price


class DiscountMixin(LoggingMixin):
    """
    Mixin class to apply discounts to products.

    discount: The discount strategy to apply.
    """

    def apply_discount(self, discount: Discount):
        if hasattr(self, 'products'):
            for product in self.products:
                amount_price = product.price
                new_price = discount.apply(amount_price)
                product.price = new_price
                self.log(f"{discount.__class__.__name__} were applied on {product.name}")
                self.log(f"Price for {product.name} were changed from {amount_price} {product.currency}"
                         f" to {new_price} {product.currency}")