import httpx
from fastapi import FastAPI, Request


TOKEN = Token
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
client = httpx.AsyncClient()

app = FastAPI()
@app.post("/webhook/")
async def webhook(req: Request):
    data = await req.json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    await client.get(f"{BASE_URL}/sendMessage?chat_id={chat_id}&text={text}")

    return data
