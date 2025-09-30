import logging

class PaymentProcessor:
    """Abstract base class for payment processors."""
    def process(self, amount: float) -> bool:
        """Process the payment. Returns True if successful, False otherwise."""
        raise NotImplementedError("Process method not implemented.")

    @staticmethod
    def validate_amount(amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
