''' from abc import ABC, abstractmethod

class PaymentProcess(ABC):
    @abstractmethod
    def make_payment(self):
        pass  # no logic here — just a rule

class PapalPayment(PaymentProcess):
    def make_payment(self):
        print("Paid by Paypal")

class VISAPayment(PaymentProcess):
    def make_payment(self):
        print("Paid by VISA")

class MasterCardPayment(PaymentProcess):
    def make_payment(self):
        print("Paid by MAster Card")


makeapayment = int(input("[1] Master Card\n[2] VISA Card\n[3] Paypal\nInsert your option [1,2,3]: "))

if makeapayment == 1:
    payment = MasterCardPayment()
elif makeapayment == 2:
    payment = VISAPayment()
else:
    payment = PapalPayment()

payment.make_payment()
'''

class PaymentProcess:
    def make_payment_paypal(self):
        print("Paid by PayPal")

    def make_payment_visa(self):
        print("Paid by VISA")

    def make_payment_master(self):
        print("Paid by Master Card")


mypayment = PaymentProcess()

makeapayment = int(input("[1] Master Card\n[2] VISA Card\n[3] PayPal\nInsert your option [1,2,3]: "))

if makeapayment == 1:
    mypayment.make_payment_master()
elif makeapayment == 2:
    mypayment.make_payment_visa()
elif makeapayment == 3:
    mypayment.make_payment_paypal()
else:
    print("Invalid choice.")
