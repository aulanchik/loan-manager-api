from app.schemas import LoanApplication
from typing import List

_loans = []
_blacklist = {"0000000000"}

def is_blacklisted(personal_id: str) -> bool:
    return personal_id in _blacklist

def store_loan(app: LoanApplication, country: str):
    _loans.append({"application": app.dict(), "country": country})

def get_all_loans():
    return _loans

def get_loans_by_user(pid: str):
    return [loan for loan in _loans if loan["application"]["personal_id"] == pid]
