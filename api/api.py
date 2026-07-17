from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from agents.coordinator_agent import CoordinatorAgent
from api.schemas import InvestigationRequest, InvestigationResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Banking fraud investigating API",
    description="Agentic AI Banking Fraud investigating system",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="frontend/templates"
)


coordinator = CoordinatorAgent()

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
def investigate_transaction(request:InvestigationRequest):
      """
    Investigate a banking transaction.
    """
      report = coordinator.run(request.transaction_id)
      if report.get("decision") == "Failed":
            raise HTTPException(
                  status_code=404,
                  detail=report["reason"]
            )
      
      return InvestigationResponse(
            decision=report["decision"],
            transaction_id=report["transaction_id"],
            customer_id=report["customer_id"],
            fraud_score=report["fraud_score"],
            risk_level=report["risk_level"],
            recommendation=report["recommendation"],
            ai_explanation=report["ai_explanation"]
      )

