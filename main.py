"""
# main.py
# This script sets up a simple Flask web application with a single endpoint.
"""

from fastapi import FastAPI, Form, Request, status
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

# from flask import Flask, jsonify
# app = Flask(__name__)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    print('Request for index page received')
    return templates.TemplateResponse('index.html', {"request": request})

@app.get('/favicon.ico')
async def favicon():
    file_name = 'favicon.ico'
    file_path = './static/' + file_name
    return FileResponse(path=file_path, headers={'mimetype': 'image/vnd.microsoft.icon'})

# @app.route("/hello", methods=["GET"])
# def hello():
#     return jsonify(message="Hello from Flask endpoint!"), 200

@app.post('/hello', response_class=HTMLResponse)
async def hello(request: Request, name: str = Form(...)):
    if name:
        print('Request for hello page received with name=%s' % name)
        return templates.TemplateResponse('hello.html', {"request": request, 'name':name})
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return RedirectResponse(request.url_for("index"), status_code=status.HTTP_302_FOUND)
    
# def main():
#     pass

if __name__ == "__main__":
    # main()
    # app.run(host="0.0.0.0", port=8000)
    uvicorn.run('main:app', host="0.0.0.0", port=8000)

# EOF
