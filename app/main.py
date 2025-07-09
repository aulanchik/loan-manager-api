from fastapi import FastAPI, Request, HTTPException
from app import storage, schemas, country_service, rate_limiter

app = FastAPI()


@app.post("/apply-loan")
async def apply_loan(request: Request, application: schemas.LoanApplication):
    ip = request.client.host or "127.0.0.1"
    country_code = await country_service.get_country_code(ip)

    if storage.is_blacklisted(application.personal_id):
        raise HTTPException(status_code=400, detail="Blacklisted personal ID")

    if rate_limiter.is_rate_limited(country_code):
        raise HTTPException(status_code=429, detail="Rate limit exceeded for country")

    storage.store_loan(application, country_code)
    return {"status": "approved", "country": country_code}


@app.get("/loans")
def list_loans():
    return storage.get_all_loans()


@app.get("/loans/{personal_id}")
def list_loans_by_user(personal_id: str):
    return storage.get_loans_by_user(personal_id)
