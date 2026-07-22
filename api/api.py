import os 
from xhtml2pdf import pisa
from io import BytesIO
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from datetime import datetime

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
@app.get("/report", response_class=HTMLResponse)
def show_report(request: Request):

    global latest_report

    if latest_report is None:
        raise HTTPException(
            status_code=404,
            detail="No investigation report available."
        )

    return templates.TemplateResponse(
        request=request,
        name="report.html",
        context={
            "report": latest_report,
            "generated_date": datetime.now().strftime("%d %B %Y %I:%M %p")
        }
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
def download_pdf(request: Request):

    global latest_report

    if latest_report is None:
        raise HTTPException(
            status_code=404,
            detail="No investigation report available."
        )

    html = templates.get_template("report.html").render(
        request=request,
        report=latest_report,
        generated_date=datetime.now().strftime("%d %B %Y %I:%M %p")
    )

    pdf = BytesIO()

    pisa_status = pisa.CreatePDF(
        src=html,
        dest=pdf
    )

    if pisa_status.err:
        raise HTTPException(
            status_code=500,
            detail="Failed to generate PDF."
        )

    pdf.seek(0)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=Banking_Fraud_Investigation_Report.pdf"
        }
    )