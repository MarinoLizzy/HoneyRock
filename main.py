from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

cabins = [
    {"name": "Pine Cabin", "status": "dirty"},
    {"name": "Lake Cabin", "status": "clean"},
]

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "cabins": cabins}
    )