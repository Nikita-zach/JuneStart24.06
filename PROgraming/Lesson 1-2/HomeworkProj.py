from validate_email_address import validate_email
import logging

# Logger setup
logger = logging.getLogger("__name__")
logger.setLevel(logging.DEBUG)

f_handler = logging.FileHandler("Logging proj.log")
f_handler.setLevel(logging.INFO)
f_format = logging.Formatter("%(asctime)s  - %(name)s - %(levelname)s - %(message)s")
f_handler.setFormatter(f_format)

logger.addHandler(f_handler)


class InvalidPriceError(Exception):
    """
    Exception raised for errors in the product price.

    expression: The input expression that caused the error.
    message: Explanation of the error.
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class InvalidQuantityError(Exception):
    """
    Exception raised for errors in the product quantity.

    expression: The input expression that caused the error.
    message: Explanation of the error.
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class LoggingMixin:
    """
    Mixin class that provides logging functionality.

    message: The message to log.
    """

    def log(self, message):
        logger.info(message)


class Product(LoggingMixin):
    """
    Class for product representation.

    name: The name of the product.
    price: The price of the product.
    currency: The currency of the product price (default: 'UAH').
    """

    def __init__(self, name: str, price: int | float, currency='UAH'):
        self.name = name
        self.price = price
        self.currency = currency

    def __str__(self):
        """
        Return a string representation of the product.
        """
        return f'{self.name}: {self.price:.2f} {self.currency}'


class Discount:
    """
    Base class for discount strategies.

    price: The original price to which the discount will be applied.
    """

    def apply(self, price):
        """
        Apply discount to a given price. Should be overridden by subclasses.
        """
        pass


class PercentageDiscount(Discount):
    """
    Discount strategy that applies a percentage discount.

    percentage: The discount percentage to apply.
    """

    def __init__(self, percentage):
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
                self.log(f"price for {product.name} were changed from {amount_price} {product.currency}"
                         f" to {new_price} {product.currency}")


class PaymentProcessor:
    """
    Base class for payment processing.

    amount: The amount to pay.
    """

    def pay(self, amount):
        """
        Process payment for the given amount. Should be overridden by subclasses.
        """
        pass


class CreditCardProcessor(PaymentProcessor):
    """
    Payment processor for credit card payments.

    card_number: The credit card number.
    card_holder: The name of the card holder.
    cvv: The card verification value.
    expiry_date: The expiry date of the card.
    """

    def __init__(self, card_number: str, card_holder: str, cvv: str, expiry_date: str):
        if len(card_number) != 19:
            raise ValueError("Card number must contain 19 characters")
        if len(cvv) != 3:
            raise ValueError("CVV code must contain 3 characters")
        if len(expiry_date) != 5:
            raise ValueError("Expiry date must contain 5 characters")
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount):
        """
        Process payment via credit card.
        """
        return f"Payment of {amount} via credit card was successful"


class PayPalProcessor(PaymentProcessor):
    """
    Payment processor for PayPal payments.

    email: The email address associated with the PayPal account.
    """

    def __init__(self, email: str):
        if not validate_email(email):
            raise ValueError("Invalid email address")
        self.email = email

    def pay(self, amount):
        """
        Process payment via PayPal.
        """
        return f"Payment of {amount} via PayPal was successful"


class BankTransferProcessor(PaymentProcessor):
    """
    Payment processor for bank transfer payments.

    account_number: The bank account number.
    account_holder: The name of the account holder.
    """

    def __init__(self, account_number: int | str, account_holder: str):
        if len(account_number) != 9:
            raise ValueError("Account number must contain 9 characters")
        self.account_number = account_number
        self.account_holder = account_holder

    def pay(self, amount):
        """
        Process payment via bank transfer.
        """
        return f"Payment of {amount} via bank transfer was successful"


class Cart(DiscountMixin, LoggingMixin):
    """
    Class for representing a shopping cart.

    product: The product to add to the cart.
    quantity: The quantity of the product to add (default: 1).
    payment_method: The payment method to use for processing the payment.
    """

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, quantity: int | float = 1):
        """
        Add a product to the cart with a specified quantity.
        """
        if quantity <= 0:
            raise InvalidQuantityError(quantity, "Quantity can't be a negative number nor equal zero")
        if product.price <= 0:
            raise InvalidPriceError(product.price, "Product price can't be negative or zero")
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


def main():
    """
    Main function to demonstrate the usage of the classes.
    """
    # Creating instances of the Product class
    product1 = Product("Laptop", 1500.00)
    product2 = Product("Mouse", 50.00)
    product3 = Product("Keyboard", -100.00)
    product4 = Product("Tablet", 300.00)
    product5 = Product("Webcam", 60.00)
    product6 = Product("External Hard Drive", 150.00)

    # Creating an instance of the Cart class and adding products
    cart = Cart()
    cart.add_product(product1, 1)
    cart.add_product(product2, 2)
    cart.add_product(product3, 1)
    cart.add_product(product4, -1)
    cart.add_product(product5, 2)
    cart.add_product(product6, -1)

    print(cart)
    print("Total cost:", cart.total_cost())

    # Applying different types of discounts
    percentage_discount = PercentageDiscount(10)
    fixed_amount_discount = FixedAmountDiscount(100)

    cart.apply_discount(percentage_discount)
    print(cart)
    print("Total cost after percentage discount:", cart.total_cost())

    cart.apply_discount(fixed_amount_discount)
    print(cart)
    print("Total cost after fixed amount discount:", cart.total_cost())

    # Using different payment systems
    credit_card_processor = CreditCardProcessor("1234-5678-9876-5432", "John Doe", "123", "12/25")
    paypal_processor = PayPalProcessor("john.doe@example.com")
    bank_transfer_processor = BankTransferProcessor("987654321", "John Doe")

    cart.pay(credit_card_processor)
    cart.pay(paypal_processor)
    cart.pay(bank_transfer_processor)


if __name__ == '__main__':
    main()
