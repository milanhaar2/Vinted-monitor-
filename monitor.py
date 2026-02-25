import requests
import os

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

URL = "https://www.vinted.hu/catalog?catalog[]=1242&currency=HUF&order=newest_first&page=1&size_ids[]=780&size_ids[]=781&size_ids[]=782&size_ids[]=783&size_ids[]=784&size_ids[]=785&size_ids[]=786&size_ids[]=787&size_ids[]=788&brand_ids[]=14&brand_ids[]=53&brand_ids[]=2703&price_from=0&price_to=6000&status_ids[]=6&status_ids[]=1&status_ids[]=2"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)

if r.status_code == 200:
    requests.post(WEBHOOK, json={
        "content": "🔎 A Vinted monitor lefutott."
    })
