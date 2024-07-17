class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for quantity, price in zip(self.quantities, self.prices):
            total += quantity * price
        return total

    def pay(self, payment_type: str, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
order.pay("debit", "0372846")
"""
This code violates the SRP because it is both responsible for managing the order and the payment. 
This results in our code being highly coupled and makes it harder to understand, maintain, and test."""



class NewOrder:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.set_stauts("open")  

    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for quantity, price in zip(self.quantities, self.prices):
            total += quantity * price
        return total
    def set_stauts(self, stat):
        self.__status=stat
    
    
class PaymentManager:

    def __init__(self) -> None:
        pass

    def pay(self, payment_type: str, security_code:str ,order:NewOrder):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            order.set_stauts("paid")
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            order.set_stauts("paid")
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


order = NewOrder()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())

paymemtmanager=PaymentManager()
paymemtmanager.pay("debit", "0372846",order)