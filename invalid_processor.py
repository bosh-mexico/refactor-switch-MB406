from base_processor import PaymentProcessor
import logging

class InvalidProcessor(PaymentProcessor):
    """
    Processor for handling invalid payment modes.
    Inherits from the PaymentProcessor base class.
    """

    def process(self, amount: float) -> bool:
        """
        Processes the payment with an invalid mode.
        
        Args:
            amount (float): The amount to process.
        
        Returns:
            bool: Always returns False, as the payment mode is invalid.
        """
        logging.warning("Invalid payment mode selected!")
        print("Invalid payment mode selected!")
        return False
