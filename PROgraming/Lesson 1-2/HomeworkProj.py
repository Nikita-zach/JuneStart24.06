from modules.product_cart_module import *


def main():
    """
    Main function to demonstrate the usage of the classes.
    """
    # Creating instances of the Product class
    product1 = Product("Laptop", 1500.00)
    product2 = Product("Mouse", 50.00)
    product3 = Product("Keyboard", 100.00)
    product4 = Product("Tablet", 300.00)
    product5 = Product("Webcam", 60.00)
    product6 = Product("External Hard Drive", 150.00)

    # Creating an instance of the Cart class and adding products
    cart = Cart()
    cart.add_product(product1, 1)
    cart.add_product(product2, 2)
    cart.add_product(product3, 1)
    cart.add_product(product4, 1)
    cart.add_product(product5, 2)
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
