from datetime import datetime

# Step 1: Ask for mood
mood = input("How are you feeling right now? ")

# Step 2: Get the current time
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Step 3: Append to mood journal
with open("mood_history.txt", "a") as file:
    file.write(f"{timestamp} - {mood}\n")

print("✅ Your mood has been logged.")

# Step 4: Ask if they want to read the history
see_history = input("Want to read your mood history? (yes/no): ").strip().lower()

if see_history == "yes":
    print("\n🕰️ Your Mood History:")
    with open("mood_history.txt", "r") as file:
        for line in file:
            print(line.strip())

