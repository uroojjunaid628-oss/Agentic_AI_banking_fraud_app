async function investigateTransaction(){

    const transactionId =
        document.getElementById("transactionId").value;

    if(transactionId===""){

        alert("Enter Transaction ID");

        return;
    }

    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("result").classList.add("hidden");

    const response = await fetch("/investigate",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            transaction_id:Number(transactionId)

        })

    });

    const data = await response.json();

    document.getElementById("loading").classList.add("hidden");

    if(!response.ok){

        alert(data.detail);

        return;
    }

    document.getElementById("transaction_id").innerText=data.transaction_id;
    document.getElementById("customer_id").innerText=data.customer_id;
    document.getElementById("fraud_score").innerText=data.fraud_score;
    document.getElementById("risk_level").innerText=data.risk_level;
    document.getElementById("recommendation").innerText=data.recommendation;
    document.getElementById("ai_explanation").innerText=data.ai_explanation;

    document.getElementById("result").classList.remove("hidden");

}