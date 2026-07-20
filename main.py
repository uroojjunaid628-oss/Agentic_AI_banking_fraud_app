from agents.coordinator_agent import CoordinatorAgent


def main():

    coordinator = CoordinatorAgent()

    transaction_id = 108721

    report = coordinator.run(transaction_id)

    print("\n")
    print("    BANKING FRAUD INVESTIGATION REPORT")
    


    print("\nTRANSACTION DETAILS")
    print("--------------------------------")

    transaction = report["transaction_details"]

    print(f"Transaction Verified     : {transaction['transaction_verified']}")
    print(f"Transaction ID           : {transaction['transaction_id']}")
    print(f"Customer ID              : {transaction['customer_id']}")
    print(f"Amount                   : {transaction['transaction_amount']} Million")
    print(f"Transaction Date         : {transaction['transaction_date']}")
    print(f"Transaction Time         : {transaction['transaction_time']}")
    print(f"Location                 : {transaction['transaction_location']}")
    print(f"Transaction Type         : {transaction['transaction_type']}")
    print(f"International Transaction: {transaction['international_transaction']}")
    print(f"Unusual Time Transaction : {transaction['unusual_time_transaction']}")


    print("\nCUSTOMER DETAILS")
    print("--------------------------------")

    customer = report["customer_details"]

    print(f"Customer Verified        : {customer['customer_verified']}")
    print(f"Customer ID              : {customer['customer_id']}")
    print(f"Home Location            : {customer['home_location']}")
    print(f"Card Type                : {customer['card_type']}")
    print(f"Account Balance          : {customer['account_balance']} Million")
    print(f"Previous Fraud Count     : {customer['previous_fraud_count']}")
    print(f"Total Transactions       : {customer['total_transactions']}")


    print("\nFRAUD ANALYSIS")
    print("--------------------------------")

    fraud = report["fraud_analysis"]

    print(f"Fraud Analysis Completed : {fraud['fraud_analysis_completed']}")
    print(f"Transaction ID           : {fraud['transaction_id']}")
    print(f"Transaction Amount       : {fraud['transaction_amount']} Million")
    print(f"Merchant Category        : {fraud['merchant_category']}")
    print(f"Failed Transaction Count : {fraud['failed_transaction_count']}")
    print(f"Previous Fraud Count     : {fraud['previous_fraud_count']}")
    print(f"New Merchant             : {fraud['is_new_merchant']}")
    print(f"International Transaction: {fraud['is_international_transaction']}")
    print(f"Unusual Time Transaction : {fraud['unusual_time_transaction']}")
    print(f"Distance From Home       : {fraud['distance_from_home']} km")


    print("\nDECISION ANALYSIS")
    print("--------------------------------")

    decision = report["decision_analysis"]

    print(f"Fraud Score              : {decision['fraud_score']}")
    print(f"Risk Level               : {decision['risk_level']}")
    print(f"Recommendation            : {decision['recommendation']}")


    print("\nINVESTIGATION SUMMARY")
    print("--------------------------------")

    print(report["investigation_summary"])


    print("\nSTATUS")
    

    print(report["status"])


if __name__ == "__main__":
    main()