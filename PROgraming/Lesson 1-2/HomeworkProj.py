from validate_email_address import validate_email


class Product:
    """
    Class for product representation.
    """

    def __init__(self, name: str, price: int | float, currency='UAH'):
        """
        Initialize a product with a name, price, and currency.

        name: Name of the product
        price: Price of the product
        currency: Currency of the product price (default: 'UAH')
        """
        self.name = name
        self.price = price
        self.currency = currency

    def __str__(self):
        """
        Return a string representation of the product.

        :return: String representation of the product
        """
        return f'{self.name}: {self.price:.2f} {self.currency}'


class Discount:
    """
    Base class for discount strategies.
    """

    def apply(self, price):
        """
        Apply discount to a given price. Should be overridden by subclasses.

        price: Original price
        :return: Discounted price
        """
        pass


class PercentageDiscount(Discount):
    """
    Discount strategy that applies a percentage discount.
    """

    def __init__(self, percentage):
        """
        Initialize a percentage discount.

        percentage: Discount percentage to apply
        """
        self.percentage = percentage

    def apply(self, price):
        """
        Apply percentage discount to the given price.

        price: Original price
        :return: Discounted price
        """
        price -= price * (self.percentage / 100)
        return price


class FixedAmountDiscount(Discount):
    """
    Discount strategy that applies a fixed amount discount.
    """

    def __init__(self, amount):
        """
        Initialize a fixed amount discount.

        amount: Fixed amount to subtract from the price
        """
        self.amount = amount

    def apply(self, price):
        """
        Apply fixed amount discount to the given price.

        price: Original price
        :return: Discounted price, with a minimum of 0
        """
        price -= self.amount
        if price < 0:
            price = 0
        return price


class DiscountMixin:
    """
    Mixin class to apply discounts to products.
    """

    def apply_discount(self, discount: Discount):
        """
        Apply the given discount to all products in the cart.

        discount: Discount strategy to apply
        """
        for product in self.products:
            amount_price = product.price
            new_price = discount.apply(amount_price)
            product.price = new_price


class PaymentProcessor:
    """
    Base class for payment processing.
    """

    def pay(self, amount):
        """
        Process payment for the given amount. Should be overridden by subclasses.

        amount: Amount to pay
        :return: Payment status message
        """
        pass


class CreditCardProcessor(PaymentProcessor):
    """
    Payment processor for credit card payments.
    """

    def __init__(self, card_number: str, card_holder: str, cvv: str, expiry_date: str):
        """
        Initialize a credit card processor with card details.

        card_number: Credit card number
        card_holder: Name of the card holder
        cvv: Card verification value
        expiry_date: Expiry date of the card
        """
        if len(card_number) != 19:
            raise ValueError("Номер карты должен содержать 19 символов")
        if len(cvv) != 3:
            raise ValueError("Код СVV должен содержать 3 символа")
        if len(expiry_date) != 5:
            raise ValueError("Срок важности карты должен иметь 5 символов")
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount):
        """
        Process payment via credit card.

        amount: Amount to pay
        :return: Payment status message
        """
        return f"Оплата по кредитной карте на сумму {amount} прошла успешно"


class PayPalProcessor(PaymentProcessor):
    """
    Payment processor for PayPal payments.
    """

    def __init__(self, email: str):
        """
        Initialize a PayPal processor with an email address.

        email: Email address associated with the PayPal account
        """
        if not validate_email(email):
            raise ValueError("Введен неверный e-mail")
        self.email = email

    def pay(self, amount):
        """
        Process payment via PayPal.

        amount: Amount to pay
        :return: Payment status message
        """
        return f"Оплата через PayPal на сумму {amount} прошла успешно"


class BankTransferProcessor(PaymentProcessor):
    """
    Payment processor for bank transfer payments.
    """

    def __init__(self, account_number: int | str, account_holder: str):
        """
        Initialize a bank transfer processor with account details.

        account_number: Bank account number
        account_holder: Name of the account holder
        """
        if len(account_number) != 9:
            raise ValueError("Номер аккаунта должен иметь 9 символов")
        self.account_number = account_number
        self.account_holder = account_holder

    def pay(self, amount):
        """
        Process payment via bank transfer.

        amount: Amount to pay
        :return: Payment status message
        """
        return f"Оплата по банковскому переводу на сумму {amount} прошла успешно"


class Cart(DiscountMixin):
    """
    Class for representing a shopping cart.
    """

    def __init__(self):
        """
        Initialize a cart with an empty product list.
        """
        self.products = {}

    def add_product(self, product: Product, quantity: int | float = 1):
        """
        Add a product to the cart with a specified quantity.

        product: Product to add
        quantity: Quantity of the product to add (default: 1)
        """
        self.products[product] = self.products.get(product, 0) + quantity

    def total_cost(self):
        """
        Calculate the total cost of all products in the cart.

        :return: Total cost of the cart
        """
        return sum(product.price * quantity for product, quantity in self.products.items())

    def pay(self, payment_method: PaymentProcessor):
        """
        Process payment using the specified payment method.

        payment_method: Payment method to use
        """
        amount = self.total_cost()
        print(payment_method.pay(amount))

    def __str__(self):
        """
        Return a string representation of the cart contents.

        :return: String representation of the cart
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
    product3 = Product("Keyboard", 100.00)
    product4 = Product("Smartphone", 1000.00)
    product5 = Product("Earbuds", 300.00)
    product6 = Product("Chair", 500.00)

    # Creating an instance of the Cart class and adding products
    cart = Cart()
    cart.add_product(product1, 1)
    cart.add_product(product2, 2)
    cart.add_product(product3, 1)
    cart.add_product(product4, 1)
    cart.add_product(product5, 1)
    cart.add_product(product6, 1)

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
