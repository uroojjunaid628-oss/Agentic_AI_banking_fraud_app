from services.llm_service import LLMService


class DecisionAgent:
    """
    Responsible for reviewing reports from all agents,
    calculating fraud risk, generating recommendations,
    and requesting an AI explanation.
    """

    def __init__(self):
        self.name = "Decision Agent"
        self.llm_service = LLMService()

    def build_prompt(
        self,
        transaction_report,
        customer_report,
        fraud_report,
        fraud_score,
        risk_level,
        recommendation
    ):
        """
        Build a prompt for the LLM.
        The LLM explains the rule-based decision.
        """

        prompt = f"""
You are an AI Fraud Investigation Assistant.

A rule-based fraud detection system has already analyzed the transaction.

Do NOT change the decision.
Do NOT calculate a new fraud score.
Do NOT use external knowledge.

Your task is ONLY to explain the decision professionally.

Transaction Details
-------------------
Transaction ID: {transaction_report["transaction_id"]}
Customer ID: {transaction_report["customer_id"]}
Transaction Amount: {transaction_report["transaction_amount"]}
Transaction Date: {transaction_report["transaction_date"]}
Transaction Time: {transaction_report["transaction_time"]}
Transaction Type: {transaction_report["transaction_type"]}
Transaction Location: {transaction_report["transaction_location"]}

Customer Details
----------------
Home Location: {customer_report["home_location"]}
Card Type: {customer_report["card_type"]}
Account Balance: {customer_report["account_balance"]}
Previous Fraud Count: {customer_report["previous_fraud_count"]}
Total Transactions: {customer_report["total_transactions"]}

Fraud Indicators
----------------
Previous Fraud Count: {fraud_report["previous_fraud_count"]}
Failed Transactions: {fraud_report["failed_transaction_count"]}
Distance From Home: {fraud_report["distance_from_home"]}
New Merchant: {fraud_report["is_new_merchant"]}
International Transaction: {fraud_report["is_international_transaction"]}
Unusual Time Transaction: {fraud_report["unusual_time_transaction"]}

Rule-Based Decision
-------------------
Fraud Score: {fraud_score}
Risk Level: {risk_level}
Recommendation: {recommendation}

Provide ONLY a short professional explanation (4-6 lines)
explaining WHY this decision was reached.
"""

        return prompt

    def calculate_fraud_score(self, fraud_report):
        """
        Calculate fraud score using predefined business rules.
        """

        fraud_score = 0

        if fraud_report["previous_fraud_count"] > 0:
            fraud_score += 20

        if fraud_report["unusual_time_transaction"] == "Yes":
            fraud_score += 15

        if fraud_report["is_new_merchant"] == "Yes":
            fraud_score += 15

        if fraud_report["is_international_transaction"] == "Yes":
            fraud_score += 20

        if fraud_report["failed_transaction_count"] > 0:
            fraud_score += 10

        if fraud_report["distance_from_home"] > 200:
            fraud_score += 20

        if fraud_report["transaction_amount"] >= 10:
            fraud_score += 15

        return fraud_score

    def make_decision(self, reports):
        """
        Generate the final fraud investigation report.
        """

        print(f"{self.name} generating final decision")

        transaction_report = reports["transaction"]
        customer_report = reports["customer"]
        fraud_report = reports["fraud"]

        # Validate reports
        if not transaction_report["transaction_verified"]:
            return {
                "decision": "Failed",
                "reason": "Transaction verification failed."
            }

        if not customer_report["customer_verified"]:
            return {
                "decision": "Failed",
                "reason": "Customer verification failed."
            }

        if not fraud_report["fraud_analysis_completed"]:
            return {
                "decision": "Failed",
                "reason": "Fraud analysis failed."
            }

        # Calculate Fraud Score
        fraud_score = self.calculate_fraud_score(fraud_report)

        # Determine Risk Level
        if fraud_score >= 60:
            risk_level = "High"

        elif fraud_score >= 30:
            risk_level = "Medium"

        else:
            risk_level = "Low"

        # Recommendation
        if risk_level == "High":
            recommendation = "Block transaction and investigate immediately."

        elif risk_level == "Medium":
            recommendation = "Require additional customer verification."

        else:
            recommendation = "Approve the transaction."

        # Build Prompt
        prompt = self.build_prompt(
            transaction_report,
            customer_report,
            fraud_report,
            fraud_score,
            risk_level,
            recommendation
        )

        # AI Explanation
        ai_explanation = self.llm_service.generate_response(prompt)

        # Final Report
        final_report = {
            "decision": "Investigation Completed",
            "transaction_id": transaction_report["transaction_id"],
            "customer_id": customer_report["customer_id"],
            "fraud_score": fraud_score,
            "risk_level": risk_level,
            "recommendation": recommendation,
            "ai_explanation": ai_explanation,
            "reports": reports
        }

        return final_report