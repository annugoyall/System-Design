from abc import ABC, abstractmethod

class UPIPayment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class NetBankingPayment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PhonePeUPIPayment(UPIPayment):
    def pay(self, amount):
        print("PhonePe UPI Payment of amount: ", amount)


class RazorPayUPIPayment(UPIPayment):
    def pay(self, amount):
        print("RazorPay UPI Payment of amount: ", amount)


class PhonePeNetBankingPayment(NetBankingPayment):
    def pay(self, amount):
        print("PhonePe NetBanking Payment of amount: ", amount)


class RazorPayNetBankingPayment(NetBankingPayment):
    def pay(self, amount):
        print("RazorPay NetBanking Payment of amount: ", amount)

class PaymentProviderFactory(ABC):
    @abstractmethod
    def get_upi_payment(self):
        pass

    @abstractmethod
    def get_net_banking_payment(self):
        pass

class PhonePePaymentProviderFactory(PaymentProviderFactory):
    def get_upi_payment(self):
        return PhonePeUPIPayment()

    def get_net_banking_payment(self):
        return PhonePeNetBankingPayment()
    
class RazorPayPaymentProviderFactory(PaymentProviderFactory):
    def get_upi_payment(self):
        return RazorPayUPIPayment()

    def get_net_banking_payment(self):
        return RazorPayNetBankingPayment()
    

class PaymentManager:
    _instance = None

    def get_instance(self):
        if PaymentManager._instance is None:
            PaymentManager._instance = PaymentManager()
        return PaymentManager._instance

    def __init__(self):
        self.payment_provider_factory = None
        self._instance = self

    def reset_payment_solutions(self, payment_provider):
        if payment_provider == "PhonePe":
            self.payment_provider_factory = PhonePePaymentProviderFactory()
        else:
            self.payment_provider_factory = RazorPayPaymentProviderFactory()

    def proceedUPIPayment(self, amount):
        self.payment_provider_factory.get_upi_payment().pay(amount)

    def proceedNetBankingPayment(self, amount):
        self.payment_provider_factory.get_net_banking_payment().pay(amount)


payment_manager = PaymentManager()
payment_manager.reset_payment_solutions("PhonePe")
payment_manager.proceedUPIPayment(100)
payment_manager.proceedNetBankingPayment(100)

payment_manager.reset_payment_solutions("RazorPay")
payment_manager.proceedUPIPayment(100)
payment_manager.proceedNetBankingPayment(120)
