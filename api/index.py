import os
import requests
from datetime import datetime

def handler(request):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    CHANNEL_ID = os.environ.get("CHANNEL_ID")
    today = datetime.now().strftime("%d/%m/%Y")
    message = f"⭐ TURF STAR V3 AUTO - {today} ⭐\n\n🏇 Pronostic du jour est pret!\n🎯 Base solide + outsiders\n\n#TURF #PMU"
    if BOT_TOKEN and CHANNEL_ID:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHANNEL_ID, "text": message}
        requests.post(url, data=data)
        return {"statusCode": 200, "body": "Sent!"}
    return {"statusCode": 200, "body": "TURF STAR AUTO Ready"}
