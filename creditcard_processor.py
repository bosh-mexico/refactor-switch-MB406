from base_processor import PaymentProcessor
import logging

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount: float) -> bool:
        """Process a credit card payment.

        Args:
            amount (float): The amount to be processed.

        Returns:
            bool: True if processing was successful, False otherwise.
        """
        try:
            self.validate_amount(amount)
            logging.info(f"Processing Credit Card payment of ${amount:.2f}")
            print(f"Processing Credit Card payment of ${amount:.2f}")
            # Simulate success
            return True
        except Exception as e:
            logging.error(f"Credit Card payment failed: {e}")
            print(f"Credit Card payment failed: {e}")
            return False
