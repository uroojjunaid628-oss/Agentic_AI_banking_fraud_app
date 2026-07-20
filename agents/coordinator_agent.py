from agents.customer_verification_agent import CustomerAgent
from agents.transaction_verification_agent import TransactionAgent
from agents.fraud_analysis_agent import FraudAgent
from agents.decision_agent import DecisionAgent
from langsmith import traceable

from services.database_service import get_transaction_by_id


class CoordinatorAgent:
    """
    Coordinates the complete fraud investigation workflow.
    """

    def __init__(self):
        self.name = "Coordinator Agent"

        self.transaction_agent = TransactionAgent()
        self.customer_agent = CustomerAgent()
        self.fraud_agent = FraudAgent()
        self.decision_agent = DecisionAgent()
    @traceable(name = "Coordinator_agent")
    def run(self, transaction_id):
        """
        Execute the complete fraud investigation workflow.
        """

        print(f"{self.name} started investigation for transaction {transaction_id}")

        # Step 1: Retrieve transaction once
        transaction = get_transaction_by_id(transaction_id)

        if not transaction:
            return {
                "decision": "Failed",
                "reason": "Transaction not found."
            }

        # Step 2: Transaction Verification
        transaction_report = self.transaction_agent.analyze_transaction(transaction)

        # Step 3: Customer Verification
        customer_report = self.customer_agent.analyze_customer(
            transaction["customer_id"]
        )

        # Step 4: Fraud Analysis
        fraud_report = self.fraud_agent.analyze_fraud(transaction)

        # Step 5: Collect reports
        reports = {
            "transaction": transaction_report,
            "customer": customer_report,
            "fraud": fraud_report
        }

        # Step 6: Final Decision
        final_report = self.decision_agent.make_decision(reports)

        return final_report