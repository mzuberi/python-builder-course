# Add a Save Function
def save_to_file(journal, filename="mood_journal.txt"):
    with open(filename, "w") as file:
        for entry in journal:
            file.write(f"Mood: {entry['mood']}\n")
            file.write(f"Entry: {entry['entry']}\n")
            file.write("-" * 20 + "\n")

# Update the Loop
mood_journal = []

while True:
    mood = input("How are you feeling today? (or type 'exit' to quit): ").strip()
    if mood.lower() == 'exit':
        break

    entry = input("Write your journal entry: ").strip()
    
    mood_journal.append({
        "mood": mood,
        "entry": entry
    })

    print("\nEntry added!")

# Save journal when done
save_to_file(mood_journal)
print("Your journal was saved to mood_journal.txt.")

