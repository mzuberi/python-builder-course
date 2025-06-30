# Create the function
def add_journal_entry(mood, entry, journal):
    journal.append({
        "mood": mood,
        "entry": entry
    })


# Create the Loop
mood_journal = []

while True:
    mood = input("How are you feeling today? (or type 'exit' to quit): ").strip()
    if mood.lower() == 'exit':
        break

    entry = input("Write your journal entry: ").strip()
    add_journal_entry(mood, entry, mood_journal)

    print("\nEntry added! Here's your current journal:\n")
    for i, item in enumerate(mood_journal, 1):
        print(f"{i}. Mood: {item['mood']}\n   Entry: {item['entry']}\n")

