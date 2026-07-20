from services.llm_service import LLMService
from langsmith import traceable


class DecisionAgent:
    """
    Responsible for reviewing reports from all agents,
    calculating fraud risk, generating recommendations,
    and creating final investigation report.
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
        Build prompt for generating investigation explanation.
        """

        prompt = f"""

Generate a professional banking fraud investigation explanation.

Generate ONLY these three sections:

Executive Summary

Decision Justification

Final Recommendation

Investigation Summary


Rules:

- Use only the provided information.
- Do not create new facts.
- Do not make assumptions or infer intentions.
- Do not accuse the customer of fraud; only describe risk indicators.
- Do not use terms such as money laundering, hacking, unauthorized access, exploitation, or criminal activity.
- Do not explain reasons that are not directly present in the provided data.
- Do not interpret unusual time as an attack or suspicious behavior; only state that it is a risk indicator.
- Do not interpret failed transactions as system testing or intentional attempts.
- Do not compare account balance and transaction amount to create unsupported conclusions.
- Do not mention AI, LLM, Groq, or agents.
- Do not change fraud score, risk level, or recommendation.
- Use professional banking language.
- Use phrases like "indicates", "shows", "requires verification", or "requires further review".
- Do not describe single values as patterns unless multiple historical records are provided.
- Describe indicators directly instead of interpreting their possible causes.
- Do not define what unusual time means; only mention that it is marked as unusual.
- Do not explain the reason behind failed transactions.
- Do not evaluate whether account balance supports or does not support the transaction.
- Do not add comparisons unless explicitly requested.
- Do not mention relationships between events unless explicitly provided in the data.


Transaction Details:

Transaction ID: {transaction_report["transaction_id"]}
Customer ID: {transaction_report["customer_id"]}
Transaction Amount: {transaction_report["transaction_amount"]}
Transaction Date: {transaction_report["transaction_date"]}
Transaction Time: {transaction_report["transaction_time"]}
Transaction Location: {transaction_report["transaction_location"]}
Transaction Type: {transaction_report["transaction_type"]}


Customer Details:

Home Location: {customer_report["home_location"]}
Card Type: {customer_report["card_type"]}
Account Balance: {customer_report["account_balance"]}
Previous Fraud Count: {customer_report["previous_fraud_count"]}
Total Transactions: {customer_report["total_transactions"]}


Fraud Indicators:

Failed Transaction Count: {fraud_report["failed_transaction_count"]}
Previous Fraud Count: {fraud_report["previous_fraud_count"]}
New Merchant: {fraud_report["is_new_merchant"]}
International Transaction: {fraud_report["is_international_transaction"]}
Unusual Time Transaction: {fraud_report["unusual_time_transaction"]}
Distance From Home: {fraud_report["distance_from_home"]}


Final Decision:

Fraud Score: {fraud_score}
Risk Level: {risk_level}
Recommendation: {recommendation}


For the "Final Recommendation" section:

- Clearly state the final action using the provided recommendation.
- Do not create a new recommendation.
- Use the recommendation exactly as provided below.
- Mention the risk level and fraud score.
- Keep it concise (5 to 6 sentences).

"""

        return prompt



    def calculate_fraud_score(self, fraud_report):
        """
        Calculate fraud score using predefined rules.
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



    @traceable(name="Decision_agent")
    def make_decision(self, reports):
        """
        Generate final fraud investigation report.
        """

        print(f"{self.name} generating final decision")


        transaction_report = reports["transaction"]
        customer_report = reports["customer"]
        fraud_report = reports["fraud"]


        # Validation

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



        # Fraud Score

        fraud_score = self.calculate_fraud_score(fraud_report)



        # Risk Calculation

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



        # Generate Explanation

        prompt = self.build_prompt(
            transaction_report,
            customer_report,
            fraud_report,
            fraud_score,
            risk_level,
            recommendation
        )


        ai_explanation = self.llm_service.generate_response(prompt)



        # Final Report

        final_report = {
    "decision": "Investigation Completed",

    "transaction_id": transaction_report["transaction_id"],
    "customer_id": customer_report["customer_id"],

    "transaction_details": transaction_report,

    "customer_details": customer_report,

    "fraud_analysis": fraud_report,
   
   "decision_analysis": {
    "fraud_score": fraud_score,
    "risk_level": risk_level,
    "recommendation": recommendation
},

   "investigation_summary": ai_explanation,
    
    
    "status": "Investigation Completed"

}


        return final_report