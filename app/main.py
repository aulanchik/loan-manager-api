from fastapi import FastAPI, HTTPException
from app import schemas, storage

app = FastAPI()

@app.post("/apply-loan")
def apply_loan(application: schemas.LoanApplication):
    country_code = "GB"  # hardcoded for now

    if storage.is_blacklisted(application.personal_id):
        raise HTTPException(status_code=400, detail="Blacklisted personal ID")

    storage.store_loan(application, country_code)
    return {"status": "approved", "country": country_code}

@app.get("/loans")
def list_loans():
    return storage.get_all_loans()

@app.get("/loans/{personal_id}")
def list_loans_by_user(personal_id: str):
    return storage.get_loans_by_user(personal_id)
