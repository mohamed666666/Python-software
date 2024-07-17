
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
    def get_stat(self):
        return self.__status
    
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


"""
If we wish to add a new payment method, we would have to make modifications to 
the PaymentManager class. This violates the Open-Closed Principle, which, as we know, 
states that software entities should be open for extension but closed for modification.
"""

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code: str):
        ...


class CreditCardPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code: str):
        print("Processing credit card payment")
        print(f"Verifying security code: {security_code}")
        order.set_stauts ("paid")


class DebitCardPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code: str):
        print("Processing debit card payment")
        print(f"Verifying security code: {security_code}")
        order.set_stauts ("paid")


class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code: str):
        print("Processing paypal payment")
        print(f"Verifying email: {security_code}")
        order.set_stauts ("paid")

#applying strategy pattern 
class PaymentManager2:
    def __init__(self , PaymentProcessor:PaymentProcessor) -> None:
        self.PaymentProcessor=PaymentProcessor
    def paying(slef , ord,secty_code):
        slef.PaymentProcessor.pay(order=ord,security_code=secty_code)
        

order = NewOrder()

order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

processor = CreditCardPaymentProcessor()
processor.pay(order, "0372846")
p=DebitCardPaymentProcessor()
p.pay(order, "0372846")
print(order.get_stat())


paymemtmanager=PaymentManager2(DebitCardPaymentProcessor())
paymemtmanager.paying(order, "1452846")
"""
output :

210
Processing debit payment type
Verifying security code: 0372846
Processing credit card payment
Verifying security code: 0372846
Processing debit card payment
Verifying security code: 0372846
paid
Processing debit card payment
Verifying security code: 1452846

"""