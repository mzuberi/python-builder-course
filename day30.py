import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return temp, description
    except Exception as e:
        print("Could not fetch weather:", e)
        return None, None

def save_entry(city, temp, description, mood):
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"{today} | {city} | {temp}°C | {description} | Mood: {mood}\n"

    with open("weather_journal.txt", "a") as file:
        file.write(entry)

    print("\n✅ Entry saved to weather_journal.txt")

# --- Run It ---
print("📍 Weather Journal")
city = input("Enter your city: ")
temp, description = get_weather(city)

if temp:
    print(f"\nCurrent weather in {city}: {temp}°C, {description}")
    mood = input("How are you feeling today? ")
    save_entry(city, temp, description, mood)
else:
    print("Try again later.")
