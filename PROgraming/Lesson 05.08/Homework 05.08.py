class Product:
    """
    Представляет продукт с названием, ценой и описанием.

    Атрибуты:
        name (str): Название продукта.
        price (str): Цена продукта в формате '$X'.
        description (str): Краткое описание продукта.
    """

    def __init__(self, name, price, description):
        """
        Инициализирует новый экземпляр класса Product.

        Аргументы:
            name (str): Название продукта.
            price (str): Цена продукта в формате '$X'.
            description (str): Краткое описание продукта.
        """
        self.name = name
        self.price = price
        self.description = description

    def get_price(self):
        """
        Возвращает цену продукта в виде числа с плавающей точкой.

        Возвращает:
            float: Цена продукта без знака доллара.
        """
        return float(self.price.strip("$"))

    def get_name(self):
        """
        Возвращает название продукта.

        Возвращает:
            str: Название продукта.
        """
        return self.name

    def __str__(self):
        """
        Возвращает строковое представление продукта.

        Возвращает:
            str: Строковое представление продукта.
        """
        return f"{self.name}: {self.price} за {self.description}"


class Cart:
    """
    Представляет корзину покупок с названием, списком сумм и словарем продуктов.

    Атрибуты:
        title (str): Название корзины.
        amount (list): Список сумм, соответствующих общей цене добавленных продуктов.
        products (dict): Словарь, где ключи - названия продуктов, а значения - вес.
    """

    def __init__(self, title):
        """
        Инициализирует новый экземпляр класса Cart.

        Аргументы:
            title (str): Название корзины.
        """
        self.title = title
        self.amount = []
        self.products = {}

    def add_amount(self, cost):
        """
        Добавляет стоимость в список общей суммы.

        Аргументы:
            cost (float): Стоимость для добавления.
        """
        self.amount.append(cost)

    def add_product(self, name, weight):
        """
        Добавляет продукт в корзину или обновляет его вес, если он уже существует.

        Аргументы:
            name (str): Название продукта.
            weight (float): Вес продукта в килограммах.
        """
        if name in self.products:
            self.products[name] += weight
        else:
            self.products[name] = weight

    def total_amount(self):
        """
        Вычисляет общую сумму корзины.

        Возвращает:
            float: Общая сумма корзины.
        """
        return sum(self.amount)

    def __str__(self):
        """
        Возвращает строковое представление корзины.

        Возвращает:
            str: Строковое представление корзины, включающее общую сумму и список продуктов.
        """
        products_list = ', '.join([f"{name} ({weight}kg)" for name, weight in self.products.items()])
        return f"Your total is {self.total_amount()}$. You have: {products_list}"


pr_1 = Product("banana", "4$", "1kg")
pr_2 = Product("apple", "6$", "1kg")
pr_3 = Product("orange", "3$", "1kg")
prs = [pr_1, pr_2, pr_3]

print(pr_1)
print(pr_2)
print(pr_3)

crt_1 = Cart("Cart 1")

while input('Do you wanna buy something? (y/n) ').lower().strip() == 'y':
    products = input("What you'd like to buy").lower().strip()
    weight = float(input("How many (weight in kilograms)? "))
    for item in prs:
        if item.get_name().lower() == products:
            cost = item.get_price()
            break
    else:
        cost = 0
    end_price = weight * cost
    crt_1.add_amount(end_price)
    crt_1.add_product(products, weight)

print(crt_1)
