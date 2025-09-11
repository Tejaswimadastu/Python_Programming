class Payment:
    def pay(self,amount):
        self.amount=amount
class CashPayment(Payment):
    def pay(self,amount):
        print(f"paid ${amount} by cash")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"paid ${amount} by card")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"paid ${amount} by UPI")
payments=[CardPayment(),CashPayment(),UPIPayment()]
for payment in payments:
    payment.pay(10000)


