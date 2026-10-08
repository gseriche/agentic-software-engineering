from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Hosting Workshop API")

class AccountIn(BaseModel):
    customer: str
    plan: str

class DomainIn(BaseModel):
    name: str
    account_id: int

accounts = {}
domains = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/accounts", status_code=201)
def create_account(data: AccountIn):
    account_id = max(accounts, default=0) + 1
    account = {"id": account_id, **data.model_dump()}
    accounts[account_id] = account
    return account

@app.get("/accounts/{account_id}/domains")
def list_domains(account_id: int):
    if account_id not in accounts:
        raise HTTPException(404, "Account not found")
    return [d for d in domains.values() if d["account_id"] == account_id]

@app.post("/domains", status_code=201)
def create_domain(data: DomainIn):
    name = data.name.strip().lower()
    if data.account_id not in accounts:
        raise HTTPException(404, "Account not found")
    if name in domains:
        raise HTTPException(409, "Domain already exists")
    domain = {"name": name, "account_id": data.account_id}
    domains[name] = domain
    return domain
