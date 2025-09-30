
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import time
import os
from dotenv import load_dotenv

from chatbot.kernel import create_kernel

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

kernel = create_kernel()

class ChatRequest(BaseModel):
    message: str

class LoginRequest(BaseModel):
    username: str
    password: str

# In-memory store for failed attempts and cooldowns
failed_attempts = {}

@app.post("/login")
async def login(login_request: LoginRequest):
    username = login_request.username
    password = login_request.password

    # Cooldown logic
    if username in failed_attempts and time.time() < failed_attempts[username]['cooldown_until']:
        return {"status": "failure", "message": f"Too many failed attempts. Please try again in {int(failed_attempts[username]['cooldown_until'] - time.time())} seconds."}

    # Validate credentials
    if username == os.getenv("USERNAME") and password == os.getenv("PASSWORD"):
        if username in failed_attempts:
            del failed_attempts[username]
        return {"status": "success", "message": "Login successful"}
    else:
        if username not in failed_attempts:
            failed_attempts[username] = {'count': 0, 'cooldown_until': 0}
        
        failed_attempts[username]['count'] += 1
        count = failed_attempts[username]['count']

        if count >= 2:
            cooldown = 60 * (5 ** (count - 2))
            failed_attempts[username]['cooldown_until'] = time.time() + cooldown
            return {"status": "failure", "message": f"Invalid credentials. Too many failed attempts. Please try again in {cooldown} seconds."}
        else:
            return {"status": "failure", "message": "Invalid credentials."}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    response = await kernel.invoke_prompt(chat_request.message)
    return {"response": str(response)}
