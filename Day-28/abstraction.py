from abc import ABC,abstractmethod
class payment(ABC):
    def source(self):
        print("scanner/upiid/mobilenumber")
    def amount(self):
        print("enter the amount: ")
    def bank(self):
        print("select the bank")
    def pin(self):
        print("enter pin: ")
    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("payment success/failure")
class HDFC(payment):
    def paymentprocess(self):
        print("payment process through HDFC bank")
class ICIC(payment):
    def paymentprocess(self):
        print("payment process through ICIC bank")
class UNION(payment):
    def paymentprocess(self):
        print("payment process through UNION bank")
class AXIS(payment):
    def paymentprocess(self):
        print("payment process through AXIS bank")
prasanna=HDFC()
prasanna.source()
prasanna.amount()
prasanna.bank()
prasanna.pin()
prasanna.paymentprocess()
prasanna.paymentstatus()


ramya=ICIC()
ramya.source()
ramya.amount()
ramya.bank()
ramya.pin()
ramya.paymentprocess()
ramya.paymentstatus()

sai=UNION()
sai.source()
sai.amount()
sai.bank()
sai.pin()
sai.paymentprocess()
sai.paymentstatus()

ram=AXIS()
ram.source()
ram.amount()
ram.bank()
ram.pin()
ram.paymentprocess()
ram.paymentstatus()

