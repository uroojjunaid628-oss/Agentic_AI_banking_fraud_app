from pydantic import BaseModel


class InvestigationRequest(BaseModel):
     """
    Request model for fraud investigation.
    """
     
     transaction_id : int



class InvestigationResponse(BaseModel):
      """
    Response model for fraud investigation.
    """

      decision:str
      transaction_id:int
      customer_id:int
      fraud_score:int
      risk_level:str
      recommendation:str
      ai_explanation:str    