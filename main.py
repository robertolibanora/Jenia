from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


def get_local_ip():
    """Ottiene l'IP locale della macchina"""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    local_ip = get_local_ip()
    
    print("\n" + "=" * 60)
    print("🚀 Server Avviato")
    print("=" * 60)
    print(f"\n📍 Porta:        {port}")
    print(f"🌐 IP Locale:    {local_ip}")
    print(f"🔗 Localhost:    http://localhost:{port}")
    print(f"🌍 IP Locale:    http://{local_ip}:{port}")
    print("=" * 60 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=port)