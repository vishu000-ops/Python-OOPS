class ChaiOrder():

    def __init__(self, type, size):
        self.type = type
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.type} chai"

order_1 = ChaiOrder("masala", 200)
order_2 = ChaiOrder("ginger", 100)

print(order_1.summary())
print(order_2.summary())