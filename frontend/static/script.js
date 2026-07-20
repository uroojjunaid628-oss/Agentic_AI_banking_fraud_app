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
        console.log(data);

        document.getElementById("loading").classList.add("hidden");

        if (!response.ok) {
            alert(data.detail);
            return;
        }

        // =========================
        // Investigation Summary
        // =========================

        document.getElementById("transaction_id").innerText = data.transaction_id;
        document.getElementById("customer_id").innerText = data.customer_id;

        document.getElementById("fraud_score").innerText =
            data.decision_analysis.fraud_score;

        document.getElementById("risk_level").innerText =
            data.decision_analysis.risk_level;

        document.getElementById("recommendation").innerText =
            data.decision_analysis.recommendation;


        // =========================
        // Transaction Agent Report
        // =========================

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


        // =========================
        // Customer Agent Report
        // =========================

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


        // =========================
        // Fraud Agent Report
        // =========================

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


        // =========================
        // Decision Agent Report
        // =========================

        document.getElementById("decision_fraud_score").innerText =
            data.decision_analysis.fraud_score;

        document.getElementById("decision_risk_level").innerText =
            data.decision_analysis.risk_level;

        document.getElementById("decision_recommendation").innerText =
            data.decision_analysis.recommendation;


        // =========================
        // AI Investigation Summary
        // =========================

        document.getElementById("investigation_summary").innerText =
            data.investigation_summary;


        document.getElementById("result").classList.remove("hidden");
        const pdfButton = document.getElementById("downloadPdf");

        if (pdfButton) {
           pdfButton.disabled = false;

    }
}   

    catch (error) {

        document.getElementById("loading").classList.add("hidden");
        

        alert("An unexpected error occurred.");

        console.error(error);

    }
    document.getElementById("downloadPdf").addEventListener("click", function(){

    window.open("/download-pdf", "_blank");

});

}