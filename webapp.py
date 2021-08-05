from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

import main

app = FastAPI()

app.mount("/public/static", StaticFiles(directory="public/static"), name="static")
templates = Jinja2Templates(directory="public/templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    main.get_temp_files()

    companies = main.get_companies()
    projects = main.get_projects()

    return templates.TemplateResponse("index.html", {"request": request, "title": "test", "projects": projects, "companies": companies})
