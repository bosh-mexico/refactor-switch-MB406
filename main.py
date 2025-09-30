from payment_modes import PaymentMode, checkout
import logging

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
