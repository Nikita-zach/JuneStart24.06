class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def get_price(self):
        return self.price.strip("$")

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name}: {self.price} for {self.description}"


class Cart:
    def __init__(self, title):
        self.title = title
        self.amount = []
        self.products = {}

    def add_amount(self, cost):
        self.amount.append(cost)

    def add_product(self, name, weight):
        if name in self.products:
            self.products[name] += weight
        else:
            self.products[name] = weight

    def __str__(self):
        total_amount = sum(self.amount)
        products_list = ', '.join([f"{name} ({weights}kg)" for name, weights in self.products.items()])
        return f"Your total is {total_amount}$. You have: {products_list}"


pr_1 = Product("banana", "4$", "1kg")
pr_2 = Product("apple", "6$", "1kg")
pr_3 = Product("orange", "3$", "1kg")
prs = [pr_1, pr_2, pr_3]
print(pr_1)
print(pr_2)
print(pr_3)

crt_1 = Cart("Cart 1")

while input('Do you wanna buy something? (y/n) ').lower().strip() == 'y':
    products = input("What you'd like to buy?").lower().strip()
    weight = float(input("How many (weight in kilograms)? "))
    for item in prs:
        if item.get_name().lower() == products:
            cost = float(item.get_price())
            break
    else:
        cost = 0
    end_price = weight * cost
    crt_1.add_amount(end_price)
    crt_1.add_product(products, weight)

print(crt_1)
