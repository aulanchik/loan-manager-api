from pydantic import BaseModel

class LoanApplication(BaseModel):
    loan_amount: float
    term: int
    name: str
    surname: str
    personal_id: str
