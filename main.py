from agents.coordinator_agent import CoordinatorAgent


def main():
    """
    Entry point of the Banking Fraud Investigation System.
    """

    coordinator = CoordinatorAgent()

    transaction_id = 108721

    report = coordinator.run(transaction_id)

    print("\n")
   
    print("        BANKING FRAUD INVESTIGATION REPORT")
    

    print(f"Transaction ID : {report['transaction_id']}")
    print(f"Customer ID    : {report['customer_id']}")

    

    print(f"Fraud Score    : {report['fraud_score']}")
    print(f"Risk Level     : {report['risk_level']}")

    

    print("Recommendation")
    
    print(report["recommendation"])

    

    print("AI Investigation Summary")
   
    print(report["ai_explanation"])



if __name__ == "__main__":
    main()