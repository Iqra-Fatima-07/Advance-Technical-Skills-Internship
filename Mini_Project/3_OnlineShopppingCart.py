# 3. Online Shopping Cart
# Suggested Classes: Product, Cart, Customer, Order
# Features: Add/remove items, quantity, discount, checkout
# OOP Concepts: Composition, Encapsulation, Inheritance



# Parent class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


# Inheritance
class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_price(self):
        return self.price - (self.price * self.discount / 100)


# Cart Item
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total(self):
        return self.product.get_price() * self.quantity


class Cart:
    def __init__(self):
        # Composition: Cart contains CartItems
        self.__items = []

    def add_item(self, product, quantity):
        self.__items.append(CartItem(product, quantity))

    def remove_item(self, product_name):
        self.__items = [
            item for item in self.__items
            if item.product.name != product_name
        ]

    def get_total(self):
        total = 0

        for item in self.__items:
            total += item.get_total()

        return total

    def display_cart(self):
        for item in self.__items:
            print(
                item.product.name,
                "x", item.quantity,
                "=", item.get_total()
            )


class Customer:
    def __init__(self, name):
        self.name = name
        # Composition: Customer has a Cart
        self.cart = Cart()

    def checkout(self):
        total = self.cart.get_total()

        if total == 0:
            print("Cart is empty!")
            return

        order = Order(self, total)
        order.place_order()


class Order:
    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount
        self.status = "Pending"

    def place_order(self):
        self.status = "Confirmed"

        print("\nOrder placed successfully!")
        print("Customer:", self.customer.name)
        print("Total:", self.amount)
        print("Status:", self.status)


# -------------------------
# Example Usage
# -------------------------

# Products
laptop = Product("Laptop", 60000)

phone = DiscountedProduct(
    "Phone",
    30000,
    10
)

# Customer
customer = Customer("Iqra")

# Add items
customer.cart.add_item(laptop, 1)
customer.cart.add_item(phone, 2)

# Display cart
print("Cart:")
customer.cart.display_cart()

# Total
print("\nCart Total:", customer.cart.get_total())

# Remove item
customer.cart.remove_item("Laptop")

print("\nAfter removing Laptop:")
customer.cart.display_cart()

# Checkout
customer.checkout()