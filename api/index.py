from http.server import BaseHTTPRequestHandler
import os
import requests
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        BOT_TOKEN = os.environ.get("BOT_TOKEN")
        CHANNEL_ID = os.environ.get("CHANNEL_ID")
        today = datetime.now().strftime("%d/%m/%Y")
        message = f"STAR TURF V3 AUTO - {today}"
        if BOT_TOKEN and CHANNEL_ID:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            try:
                requests.post(url, data={"chat_id": CHANNEL_ID, "text": message}, timeout=10)
            except:
                pass
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(f"TURF STAR AUTO Ready - {today}".encode())
        return
