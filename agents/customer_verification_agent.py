from services.database_service import get_customer_transactions


class CustomerAgent:
    """
    Responsible for verifying customer information
    and preparing a customer verification report.
    """

    def __init__(self):
        self.name = "Customer Agent"

    def analyze_customer(self, customer_id):
        """
        Retrieve customer history and prepare
        a customer verification report.
        """

        print(f"{self.name} analyzing customer {customer_id}")

        # Retrieve all transactions of the customer
        transactions = get_customer_transactions(customer_id)

        # Customer not found
        if not transactions:
            return {
                "customer_verified": False,
                "customer_id": customer_id,
                "message": "Customer not found."
            }

        # Customer information (same for all transactions)
        customer = transactions[0]

        customer_report = {
            "customer_verified": True,
            "customer_id": customer["customer_id"],
            "home_location": customer["customer_home_location"],
            "card_type": customer["card_type"],
            "account_balance": customer["account_balance_million"],
            "previous_fraud_count": customer["previous_fraud_count"],
            "total_transactions": len(transactions)
        }

        return customer_report