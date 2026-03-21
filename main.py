from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager

# from OLD_STUFF.database import engine, SessionLocal
# from models import Cabin, Base
from create_db import engine, SessionLocal, Cabin, Booking, Base, cabins


from fastapi import Body



@asynccontextmanager
async def lifespan(app: FastAPI):
    #Create tables
    Base.metadata.create_all(bind=engine)
    #Add cabin data
    db = SessionLocal()
    db.add_all(cabins)
    db.commit()
    db.close()
    print('Database and cabins created!')
    # Allow the rest of the app to run
    yield
    #Put anything here that I want to happen on app shutdown

app = FastAPI(lifespan=lifespan)



templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):

    db = SessionLocal()
    print("querying cabins")
    cabins = db.query(Cabin).all()
    db.close()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "cabins": cabins}
    )


@app.post("/update_status")
def update_status(cabin_name: str = Body(...), status: str = Body(...)):

    db = SessionLocal()

    cabin = db.query(Cabin).filter(Cabin.Name == cabin_name).first()
    cabin.Status = status

    db.commit()
    db.close()

    return {"message": "updated"}


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