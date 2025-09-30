from base_processor import PaymentProcessor
import logging

class PayPalProcessor(PaymentProcessor):
    def process(self, amount: float) -> bool:
        """Process a payment through PayPal.

        Args:
            amount (float): The amount to be processed.

        Returns:
            bool: True if the payment was processed successfully, False otherwise.
        """
        try:
            self.validate_amount(amount)
            logging.info(f"Processing PayPal payment of ${amount:.2f}")
            print(f"Processing PayPal payment of ${amount:.2f}")
            # Simulate success
            return True
        except Exception as e:
            logging.error(f"PayPal payment failed: {e}")
            print(f"PayPal payment failed: {e}")
            return False
