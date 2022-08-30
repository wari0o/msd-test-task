import json
import requests
from fastapi import FastAPI
import datetime
from datetime import timezone
from pydantic import BaseModel

app = FastAPI()

db = []
tempservertime = ''


@app.get('/')
async def index():
    get_eur_btc_rate = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    servertime = json.loads(get_eur_btc_rate.text)['time']['updated']
    global tempservertime
    if servertime != tempservertime:
        clientrequesttime = datetime.datetime.now(timezone.utc).strftime('%b %d, %Y %H:%M:%S UTC')
        eur_btc_rate = json.loads(get_eur_btc_rate.text)['bpi']['EUR']['rate_float']
        get_czk_eur_rate = requests.get(
            'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/czk.json')
        czk_btc_rate = json.loads(get_czk_eur_rate.text)['czk'] * eur_btc_rate
        out_json = OutJson(servertime=servertime, clientrequesttime=clientrequesttime,
                           BTCrates={"EUR": round(eur_btc_rate, 2), "CZK": round(czk_btc_rate, 2)})
        db.append(out_json)
        tempservertime = servertime
        return out_json
    else:
        return db[-1]


@app.get('/history')
async def history():
    return db


class Rates(BaseModel):
    EUR: float
    CZK: float


class OutJson(BaseModel):
    servertime: str
    clientrequesttime: str
    BTCrates: Rates
