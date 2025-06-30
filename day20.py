# Day 20 – Smart Mood Tracker with Dictionaries

# A dictionary to store moods for each day
mood_log = {}

while True:
    day = input("Enter the day (e.g., Monday): ")
    mood = input("How are you feeling today? ")
    
    # Store the mood under the day key
    mood_log[day] = mood

    another = input("Log another day? (yes/no): ").lower()
    if another != "yes":
        break

print("\n=== Mood Summary ===")
for day, mood in mood_log.items():
    print(f"{day}: {mood}")


