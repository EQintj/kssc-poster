import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import webbrowser
from threading import Timer
import os

app = FastAPI()

# 정적 파일 및 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

def open_browser():
    url = "http://127.0.0.1:8000"
    try:
        # 윈도우에서 크롬 경로 시도
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    except Exception:
        # 실패 시 기본 브라우저 사용
        webbrowser.open(url)

if __name__ == "__main__":
    # 서버 시작 시 브라우저 자동 호출 (1초 후 실행)
    Timer(1, open_browser).start()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
