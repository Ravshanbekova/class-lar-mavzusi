class CartItem:
    def __init__(self, name, price, quantity, discount):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def total_cost(self):
        return self.price * self.quantity * (1 - self.discount / 100)


class FoodItem(CartItem):
    def total_cost(self):
        cost = super().total_cost()
        return f"Nooziq - ovqat mahsuloti: {self.name} -> {cost:.2f}$"


items = [
    FoodItem("Olma", 1.5, 3, 10),
    FoodItem("Non", 2.0, 2, 5)
]

total_sum = 0

for item in items:
    print(item.total_cost())
    total_sum += item.price * item.quantity * (1 - item.discount / 100)

print("Umumiy summa:", round(total_sum, 2), "$")