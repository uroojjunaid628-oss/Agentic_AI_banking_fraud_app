class TransactionAgent:
    """
    Responsible for verifying transaction details
    and preparing a transaction verification report.
    """

    def __init__(self):
        self.name = "Transaction Agent"

    def analyze_transaction(self, transaction):
        """
        Analyze a transaction and prepare a
        transaction verification report.
        """

        # Validate input
        if not transaction:
            return {
                "transaction_verified": False,
                "message": "Transaction not found."
            }

        print(
            f"{self.name} analyzing transaction "
            f"{transaction['transaction_id']}"
        )

        transaction_report = {
            "transaction_verified": True,
            "transaction_id": transaction["transaction_id"],
            "customer_id": transaction["customer_id"],
            "transaction_amount": transaction["transaction_amount_million"],
            "transaction_date": transaction["transaction_date"],
            "transaction_time": transaction["transaction_time"],
            "transaction_location": transaction["transaction_location"],
            "transaction_type": transaction["transaction_type"],
            "international_transaction": transaction["is_international_transaction"],
            "unusual_time_transaction": transaction["unusual_time_transaction"]
        }

        return transaction_report