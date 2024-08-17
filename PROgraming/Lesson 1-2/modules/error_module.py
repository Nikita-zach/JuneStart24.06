class InvalidPriceError(Exception):
    """
    Exception raised for errors in the product price.

    expression: The input expression that caused the error.
    message: Explanation of the error.
    """

    def __init__(self, price, message):
        super().__init__(message)
        self.price = price
        self.message = message


class InvalidQuantityError(Exception):
    """
    Exception raised for errors in the product quantity.

    expression: The input expression that caused the error.
    message: Explanation of the error.
    """

    def __init__(self, quantity, message):
        super().__init__(message)
        self.quantity = quantity
        self.message = message
