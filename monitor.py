import requests
import os

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

URL = "https://www.vinted.hu/catalog?search_text=férfi ralph lauren&currency=HUF&order=relevance&page=1&time=1772045609&status_ids[]=6&status_ids[]=1&status_ids[]=2&price_from=0&price_to=6000&brand_ids[]=88&brand_ids[]=4273"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)

if r.status_code == 200:
    requests.post(WEBHOOK, json={
        "content": "🔎 A Vinted monitor lefutott."
    })
