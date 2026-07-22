async function investigateTransaction() {

    const transactionId = document.getElementById("transactionId").value;

    if (transactionId === "") {
        alert("Enter Transaction ID");
        return;
    }

    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("result").classList.add("hidden");

    try {

        const response = await fetch("/investigate", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                transaction_id: Number(transactionId)
            })

        });

        const data = await response.json();

        document.getElementById("loading").classList.add("hidden");

        if (!response.ok) {
            alert(data.detail);
            return;
        }

        // ===========================================
        // REPORT OVERVIEW
        // ===========================================

        document.getElementById("transaction_id").innerText =
            data.transaction_id;

        document.getElementById("customer_id").innerText =
            data.customer_id;

        document.getElementById("report_id").innerText =
            "BFI-" + data.transaction_id;

        document.getElementById("report_date").innerText =
            new Date().toLocaleString();    

        document.getElementById("status").innerText =
            data.status;

        document.getElementById("fraud_score").innerText =
            data.decision_analysis.fraud_score;

        document.getElementById("risk_level").innerText =
            data.decision_analysis.risk_level;

        document.getElementById("recommendation").innerText =
            data.decision_analysis.recommendation;

        // ===========================================
        // EXECUTIVE SUMMARY
        // ===========================================

        document.getElementById("executive_summary").innerHTML = `
        This report presents the findings of an automated fraud investigation
        conducted for Transaction ID <b>${data.transaction_id}</b>.
        The transaction was analyzed using multiple specialized AI agents,
        including the Transaction Agent, Customer Agent, Fraud Agent and
        Decision Agent.

        Based on the complete investigation, the transaction received a
        fraud score of <b>${data.decision_analysis.fraud_score}</b>,
        corresponding to a
        <b>${data.decision_analysis.risk_level}</b>
        risk level.

        The system recommends
        <b>${data.decision_analysis.recommendation}</b>.
        `;

        // ===========================================
        // TRANSACTION ANALYSIS
        // ===========================================

        document.getElementById("transaction_amount").innerText =
            data.transaction_details.transaction_amount;

        document.getElementById("transaction_date").innerText =
            data.transaction_details.transaction_date;

        document.getElementById("transaction_time").innerText =
            data.transaction_details.transaction_time;

        document.getElementById("transaction_type").innerText =
            data.transaction_details.transaction_type;

        document.getElementById("transaction_location").innerText =
            data.transaction_details.transaction_location;

        document.getElementById("transaction_amount_analysis").innerText =
            "The transaction amount was evaluated against historical customer behaviour and fraud indicators.";

        document.getElementById("transaction_date_analysis").innerText =
            "The transaction date was verified during the investigation process.";

        document.getElementById("transaction_time_analysis").innerText =
            "The transaction time was examined to identify unusual banking activity.";

        document.getElementById("transaction_type_analysis").innerText =
            "The transaction type was compared with the customer's previous transactions.";

        document.getElementById("transaction_location_analysis").innerText =
            "The transaction location was reviewed for geographical anomalies.";

        // ===========================================
        // CUSTOMER ANALYSIS
        // ===========================================

                document.getElementById("home_location").innerText =
            data.customer_details.home_location;

        document.getElementById("card_type").innerText =
            data.customer_details.card_type;

        document.getElementById("account_balance").innerText =
            data.customer_details.account_balance;

        document.getElementById("previous_fraud_count").innerText =
            data.customer_details.previous_fraud_count;

        document.getElementById("total_transactions").innerText =
            data.customer_details.total_transactions;

        document.getElementById("home_location_analysis").innerText =
            "The customer's registered home location was compared with the transaction location to detect geographical inconsistencies.";

        document.getElementById("card_type_analysis").innerText =
            "The payment card used for this transaction was verified as part of the customer profile analysis.";

        document.getElementById("account_balance_analysis").innerText =
            "The available account balance was reviewed to identify unusual spending behaviour.";

        document.getElementById("previous_fraud_analysis").innerText =
            "Previous confirmed fraud incidents increase the overall fraud risk associated with the customer.";

        document.getElementById("total_transactions_analysis").innerText =
            "Historical customer transactions were reviewed to understand normal banking behaviour.";

        // ===========================================
        // FRAUD INDICATOR ANALYSIS
        // ===========================================

        document.getElementById("international_transaction").innerText =
            data.fraud_analysis.is_international_transaction;

        document.getElementById("new_merchant").innerText =
            data.fraud_analysis.is_new_merchant;

        document.getElementById("unusual_time_transaction").innerText =
            data.fraud_analysis.unusual_time_transaction;

        document.getElementById("failed_transaction_count").innerText =
            data.fraud_analysis.failed_transaction_count;

        document.getElementById("distance_from_home").innerText =
            data.fraud_analysis.distance_from_home;

        // ===========================================
        // DECISION ANALYSIS
        // ===========================================

                document.getElementById("decision").innerText =
            data.decision;

        document.getElementById("recommendation_report").innerText =
            data.decision_analysis.recommendation;

        document.getElementById("decision_analysis").innerHTML = `
        After reviewing transaction details, customer history,
        fraud indicators and overall risk assessment,
        the Decision Agent classified this transaction as
        <b>${data.decision_analysis.risk_level}</b>
        risk with a fraud score of
        <b>${data.decision_analysis.fraud_score}</b>.
        The recommended action is
        <b>${data.decision_analysis.recommendation}</b>.
        `;

        // ===========================================
        // AI INVESTIGATION SUMMARY
        // ===========================================

        document.getElementById("investigation_summary").innerText =
            data.investigation_summary;

        // ===========================================
        // SHOW REPORT
        // ===========================================

        document.getElementById("result").classList.remove("hidden");

        const pdfButton = document.getElementById("downloadPdf");

        pdfButton.disabled = false;

    }

    catch (error) {

        document.getElementById("loading").classList.add("hidden");

        alert("An unexpected error occurred.");

        console.error(error);

    }

}

document.getElementById("downloadPdf").addEventListener("click", function () {

    window.open("/download-pdf", "_blank");

});