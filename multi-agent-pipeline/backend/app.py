class Inventory:
    def __init__(self):
        self.stock = {}

    def add_item(self, name, qty):
        if qty < 0:
            raise ValueError("Quantity cannot be negative")
        self.stock[name] = self.stock.get(name, 0) + qty
        return self.stock[name]

    def remove_item(self, name, qty):
        if name not in self.stock or self.stock[name] < qty:
            raise ValueError(f"Not enough stock for '{name}'")
        self.stock[name] -= qty
        return self.stock[name]

    def get_stock(self, name):
        return self.stock.get(name, 0)


def calculate_total(prices, quantities):
    """prices and quantities are lists of equal length"""
    if len(prices) != len(quantities):
        raise ValueError("prices and quantities must be the same length")
    return sum(p * q for p, q in zip(prices, quantities))


if __name__ == "__main__":
    inv = Inventory()
    inv.add_item("laptop", 10)
    inv.remove_item("laptop", 3)
    print(f"Laptops in stock: {inv.get_stock('laptop')}")

    total = calculate_total([500, 20], [2, 5])
    print(f"Order total: ${total}")