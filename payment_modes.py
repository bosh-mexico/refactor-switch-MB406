from enum import Enum
from paypal_processor import PayPalProcessor
from googlepay_processor import GooglePayProcessor
from creditcard_processor import CreditCardProcessor
from invalid_processor import InvalidProcessor
import logging

# Define Payment Modes as Enum
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

PROCESSOR_MAP = {}

def register_processor(mode: PaymentMode, processor):
    """Dynamically register a new payment processor."""
    PROCESSOR_MAP[mode] = processor

# Register default processors
def _register_defaults():
    register_processor(PaymentMode.PAYPAL, PayPalProcessor())
    register_processor(PaymentMode.GOOGLEPAY, GooglePayProcessor())
    register_processor(PaymentMode.CREDITCARD, CreditCardProcessor())
_register_defaults()

def checkout(mode: PaymentMode, amount: float) -> bool:
    """Process a payment and return True if successful, False otherwise."""
    processor = PROCESSOR_MAP.get(mode, InvalidProcessor())
    return processor.process(amount)

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    amount = 150.75
    print("--- Example 1: PayPal ---")
    checkout(PaymentMode.PAYPAL, amount)
    print("\n--- Example 2: GooglePay ---")
    checkout(PaymentMode.GOOGLEPAY, amount)
    print("\n--- Example 3: CreditCard ---")
    checkout(PaymentMode.CREDITCARD, amount)
    print("\n--- Example 4: Unknown ---")
    checkout(PaymentMode.UNKNOWN, amount)

    # Additional: User input demo
    print("\n--- Example 5: User Input Demo ---")
    user_input = input("Enter payment mode (PayPal, GooglePay, CreditCard): ").strip().upper()
    try:
        mode = PaymentMode[user_input]
    except KeyError:
        mode = PaymentMode.UNKNOWN
    checkout(mode, 99.99)
