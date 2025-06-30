import requests
from datetime import datetime

def get_daily_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        response.raise_for_status()
        data = response.json()
        return data["content"], data["author"]
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch quote: {e}")
        return None, None

def save_quote_to_file(quote, author):
    today = datetime.now().strftime("%Y-%m-%d")
    entry = f"{today} — \"{quote}\" — {author}\n"

    with open("daily_quotes.txt", "a") as file:
        file.write(entry)
    print("Quote saved to daily_quotes.txt")

# --- Run It ---
quote, author = get_daily_quote()

if quote:
    print(f"\n✨ Quote of the Day ✨\n\"{quote}\"\n   — {author}\n")
    save_quote_to_file(quote, author)
else:
    print("Try again later.")
