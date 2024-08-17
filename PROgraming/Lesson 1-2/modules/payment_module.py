from validate_email_address import validate_email


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