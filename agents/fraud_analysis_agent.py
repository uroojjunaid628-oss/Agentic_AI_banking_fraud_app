class FraudAgent:
    """
    Responsible for analyzing fraud indicators
    and preparing a fraud analysis report.
    """

    def __init__(self):
        self.name = "Fraud Agent"

    def analyze_fraud(self, transaction):
        """
        Analyze fraud-related indicators from the transaction
        and prepare a fraud analysis report.
        """

        # Validate input
        if not transaction:
            return {
                "fraud_analysis_completed": False,
                "message": "Transaction not found."
            }

        print(
            f"{self.name} analyzing transaction "
            f"{transaction['transaction_id']}"
        )

        fraud_report = {
            "fraud_analysis_completed": True,
            "transaction_id": transaction["transaction_id"],
            "transaction_amount": transaction["transaction_amount_million"],
            "merchant_category": transaction["merchant_category"],
            "failed_transaction_count": transaction["failed_transaction_count"],
            "previous_fraud_count": transaction["previous_fraud_count"],
            "is_new_merchant": transaction["is_new_merchant"],
            "is_international_transaction": transaction["is_international_transaction"],
            "unusual_time_transaction": transaction["unusual_time_transaction"],
            "distance_from_home": transaction["distance_from_home"]
           
        }

        return fraud_report