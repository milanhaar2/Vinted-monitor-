import requests
import os

# Discord webhook a GitHub Secretből
WEBHOOK = os.environ["DISCORD_WEBHOOK"]

# Te Vinted link (férfi Ralph Lauren, 0–6000 HUF)
URL = "https://www.vinted.hu/catalog?search_text=férfi ralph lauren&currency=HUF&order=relevance&page=1&time=1772045609&status_ids[]=6&status_ids[]=1&status_ids[]=2&price_from=0&price_to=6000&brand_ids[]=88&brand_ids[]=4273"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Lekérjük a Vinted JSON adatokat
r = requests.get(URL, headers=headers)
data = r.json()

# Végigmegyünk az összes hirdetésen
for item in data.get("items", []):
    title = item.get("title", "N/A")
    price = item.get("price", {}).get("amount", "N/A")
    currency = item.get("price", {}).get("currency", "HUF")
    link = item.get("url")
    # Az első kép linkje
    photo = item.get("photos", [{}])[0].get("url_fullxfull", "")

    # Discord üzenet formázás
    content = f"🆕 **{title}**\n💰 {price} {currency}\n🔗 {link}\n{photo}"

    # Küldés a Discord webhookra
    requests.post(WEBHOOK, json={"content": content})
