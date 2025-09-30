from enum import Enum

class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

class PaymentProcessor:
    def process(self, amount: float):
        raise NotImplementedError("Process method not implemented.")

class PayPalProcessor(PaymentProcessor):
    def process(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}")
        # Add PayPal-specific logic here

class GooglePayProcessor(PaymentProcessor):
    def process(self, amount: float):
        print(f"Processing GooglePay payment of ${amount:.2f}")
        # Add GooglePay-specific logic here

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount: float):
        print(f"Processing Credit Card payment of ${amount:.2f}")
        # Add Credit Card-specific logic here

class InvalidProcessor(PaymentProcessor):
    def process(self, amount: float):
        print("Invalid payment mode selected!")

PROCESSOR_MAP = {
    PaymentMode.PAYPAL: PayPalProcessor(),
    PaymentMode.GOOGLEPAY: GooglePayProcessor(),
    PaymentMode.CREDITCARD: CreditCardProcessor(),
}

def checkout(mode: PaymentMode, amount: float):
    processor = PROCESSOR_MAP.get(mode, InvalidProcessor())
    processor.process(amount)

if __name__ == "__main__":
    amount = 150.75
    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(PaymentMode.UNKNOWN, amount)
