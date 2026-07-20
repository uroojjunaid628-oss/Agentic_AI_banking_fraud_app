from typing import Any, Dict
from pydantic import BaseModel


class InvestigationRequest(BaseModel):
    """
    Request model for fraud investigation.
    """

    transaction_id: int


class InvestigationResponse(BaseModel):
    """
    Response model for fraud investigation.
    """

    decision: str
    status: str

    transaction_id: int
    customer_id: int

    transaction_details: Dict[str, Any]

    customer_details: Dict[str, Any]

    fraud_analysis: Dict[str, Any]

    decision_analysis: Dict[str, Any]

    investigation_summary: str   