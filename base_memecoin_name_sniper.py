import requests, time, re

WATCHED = [
    "brett", "degen", "toshi", "migi", "aero", "moon", "pepe", "wif", "cat", "dog", "shib"
]

def name_sniper():
    print("Base — Meme Name Sniper (catches by name/symbol in <3 sec)")
    seen = set()
    pattern = re.compile("|".join(WATCHED), re.IGNORECASE)

    while True:
        r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base?limit=100")
        for pair in r.json().get("pairs", []):
            addr = pair["pairAddress"]
            if addr in seen: continue

            age = time.time() - pair.get("pairCreatedAt", 0) / 1000
            if age > 3: continue  # старше 3 секунд — пропускаем

            name = pair["baseToken"]["name"]
            symbol = pair["baseToken"]["symbol"]

            if pattern.search(name) or pattern.search(symbol):
                seen.add(addr)
                print(f"NAME SNIPE HIT in {age:.1f}s!\n"
                      f"{symbol} — {name}\n"
                      f"Price: ${float(pair['priceUsd']):.12f}\n"
                      f"Liq: ${pair['liquidity']['usd']:,.0f}\n"
                      f"https://dexscreener.com/base/{addr}\n"
                      f"CA: {pair['baseToken']['address']}\n"
                      f"{'='*80}")

        time.sleep(1.1)

if __name__ == "__main__":
    name_sniper()
