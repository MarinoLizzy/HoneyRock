from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Cabin, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):

    db = SessionLocal()
    cabins = db.query(Cabin).all()
    db.close()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "cabins": cabins}
    )

# templates = Jinja2Templates(directory="templates")

# cabins = [
#     {"name": "Loberg", "status": "dirty", "next_arrival": "Mar 14", "next_guest": "Rob Ribbe"},
#     {"name": "Voy", "status": "clean", "next_arrival": "Mar 14", "next_guest": "Muhia"},
# ]

# @app.get("/")
# def home(request: Request):
#     return templates.TemplateResponse(
#         "index.html",
#         {"request": request, "cabins": cabins}




# @app.post("/update/{cabin}")
# def update_status(cabin: str, status: str):
#     for c in cabins:
#         if c["name"] == cabin:
#             c["status"] = status