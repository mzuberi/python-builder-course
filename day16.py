# Day 16 - Mood Journal File Logger

def write_to_journal(entry):
    with open("mood_journal.txt", "a") as file:  # Append mode
        file.write(entry + "\n")

def read_journal():
    try:
        with open("mood_journal.txt", "r") as file:
            print("\n📝 Your Mood Journal Entries:")
            print(file.read())
    except FileNotFoundError:
        print("No journal entries found yet. Start writing!")

# User input
print("🌤️ Welcome to your Mood Journal")
mood = input("How are you feeling today? ")
reflection = input("What do you want to remember from today? ")

entry = f"Mood: {mood} | Reflection: {reflection}"
write_to_journal(entry)

# Option to read past entries
show = input("Would you like to see your past entries? (yes/no): ").strip().lower()
if show == "yes":
    read_journal()
else:
    print("Entry saved! See you tomorrow 🌙")
