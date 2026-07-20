from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
) 
from reportlab.lib.styles import getSampleStyleSheet

from agents.coordinator_agent import CoordinatorAgent
from api.schemas import InvestigationRequest, InvestigationResponse


app = FastAPI(
    title="Banking Fraud Investigation API",
    description="Agentic AI Banking Fraud Investigation System",
    version="1.0.0"
)


# Static files (CSS, JS)
app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static"
)


# HTML templates
templates = Jinja2Templates(
    directory="frontend/templates"
)


# Initialize Coordinator Agent
coordinator = CoordinatorAgent()
latest_report = None


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Display the Banking Fraud Investigation webpage.
    """

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post(
    "/investigate",
    response_model=InvestigationResponse
)
def investigate_transaction(request: InvestigationRequest):
    """
    Investigate a banking transaction.
    """

    global latest_report

    report = coordinator.run(request.transaction_id)

    latest_report = report


    # Handle failed investigation
    if report.get("decision") == "Failed":
        raise HTTPException(
            status_code=404,
            detail=report["reason"]
        )


       # Return complete investigation report
    return InvestigationResponse(
        decision=report["decision"],
        status=report["status"],

        transaction_id=report["transaction_id"],
        customer_id=report["customer_id"],

        transaction_details=report["transaction_details"],

        customer_details=report["customer_details"],

        fraud_analysis=report["fraud_analysis"],

        decision_analysis=report["decision_analysis"],

        investigation_summary=report["investigation_summary"]
    
    )

@app.get("/download-pdf")
def download_pdf():

    global latest_report

    if latest_report is None:
        raise HTTPException(
            status_code=404,
            detail="No investigation report available"
        )


    file_name = "Banking_Fraud_Investigation_Report.pdf"


    pdf = SimpleDocTemplate(
        file_name,
        pagesize=letter
    )


    styles = getSampleStyleSheet()

    content = []


   
    # Title
    

    content.append(
        Paragraph(
            "BANKING FRAUD INVESTIGATION REPORT",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))


    
    # Investigation Summary
    

    content.append(
        Paragraph(
            "INVESTIGATION SUMMARY",
            styles["Heading2"]
        )
    )


    decision = latest_report["decision_analysis"]


    summary_data = [

        ["Field", "Value"],

        [
            "Transaction ID",
            str(latest_report["transaction_id"])
        ],

        [
            "Customer ID",
            str(latest_report["customer_id"])
        ],

        [
            "Fraud Score",
            str(decision["fraud_score"])
        ],

        [
            "Risk Level",
            decision["risk_level"]
        ],

        [
            "Recommendation",
            decision["recommendation"]
        ]

    ]


    table = Table(summary_data)

    table.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1), 1, None),
            ("BACKGROUND", (0,0), (-1,0), None)
        ])
    )

    content.append(table)

    content.append(Spacer(1,20))


    
    # Transaction Agent
   

    content.append(
        Paragraph(
            "TRANSACTION AGENT REPORT",
            styles["Heading2"]
        )
    )


    transaction = latest_report["transaction_details"]


    transaction_data = [

        ["Field", "Value"],

        ["Amount", str(transaction["transaction_amount"])],

        ["Date", str(transaction["transaction_date"])],

        ["Time", str(transaction["transaction_time"])],

        ["Type", str(transaction["transaction_type"])],

        ["Location", str(transaction["transaction_location"])]

    ]


    table = Table(transaction_data)

    table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),1,None)
        ])
    )


    content.append(table)

    content.append(Spacer(1,20))


    # Customer Agent
    

    content.append(
        Paragraph(
            "CUSTOMER AGENT REPORT",
            styles["Heading2"]
        )
    )


    customer = latest_report["customer_details"]


    customer_data = [

        ["Field","Value"],

        ["Home Location", str(customer["home_location"])],

        ["Card Type", str(customer["card_type"])],

        ["Account Balance", str(customer["account_balance"])],

        ["Previous Fraud Count", str(customer["previous_fraud_count"])],

        ["Total Transactions", str(customer["total_transactions"])]

    ]


    table = Table(customer_data)

    table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),1,None)
        ])
    )


    content.append(table)

    content.append(Spacer(1,20))


    
    # Fraud Agent
   

    content.append(
        Paragraph(
            "FRAUD AGENT REPORT",
            styles["Heading2"]
        )
    )


    fraud = latest_report["fraud_analysis"]


    fraud_data = [

        ["Field","Value"],

        [
            "International Transaction",
            str(fraud["is_international_transaction"])
        ],

        [
            "New Merchant",
            str(fraud["is_new_merchant"])
        ],

        [
            "Unusual Time Transaction",
            str(fraud["unusual_time_transaction"])
        ],

        [
            "Failed Transaction Count",
            str(fraud["failed_transaction_count"])
        ],

        [
            "Distance From Home",
            str(fraud["distance_from_home"])
        ]

    ]


    table = Table(fraud_data)

    table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),1,None)
        ])
    )


    content.append(table)

    content.append(Spacer(1,20))


    
    # AI Summary
   

    content.append(
        Paragraph(
            "AI INVESTIGATION SUMMARY",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            latest_report["investigation_summary"],
            styles["Normal"]
        )
    )


    pdf.build(content)


    return FileResponse(
        file_name,
        media_type="application/pdf",
        filename=file_name
    )