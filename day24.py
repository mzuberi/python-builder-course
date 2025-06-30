import datetime

def main():
    print("\n🌸 Welcome to Move With Mona CLI 🌸")
    print("Your Daily Wellness Tracker")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Write a journal entry")
        print("2. Log your mood")
        print("3. View mood history")
        print("4. Exit")
        print("4. Show Today’s Mood Summary")


        choice = input("Enter 1, 2, 3, or 4: ").strip()

        if choice == "1":
            write_journal()
        elif choice == "2":
            log_mood()
        elif choice == "3":
            view_history()
        elif choice == "4":
            print("Goodbye beautiful soul!")
        
            break
        elif choice == "4":
          show_today_summary()

        else:
            print("Not a valid option. Try again!")
        

def write_journal():
    entry = input("Write your journal entry: ")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("journal_log.txt", "a") as file:
        file.write(f"{now} - {entry}\n")
    print(" Journal saved.")

def log_mood():
    mood = input("How are you feeling today? ").lower()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save mood to log file
    with open("mood_log.txt", "a") as file:
        file.write(f"{now} - {mood}\n")
    
    print("✅ Mood logged.")

    # Give movement suggestion
    mood_to_workout = {
        "sore": "Try the Soft Sculpt Flow → monaskhana.com/move/soft-sculpt",
        "energized": "Full Body Reset Sculpt → monaskhana.com/move/full-body-reset",
        "tired": "Slow Stretch Session → monaskhana.com/move/slow-stretch",
        "pumped": "Glutes & Thighs Sculpt → monaskhana.com/move/glutes-thighs",
        "anxious": "Mindful Mat Flow → monaskhana.com/move/mindful-mat",
    }

    suggestion = mood_to_workout.get(mood)
    if suggestion:
        print(f"\n✨ Based on your mood, here's a recommended workout:\n{suggestion}")
    else:
        print("\n💡 No suggestion available for that mood yet, but keep moving with love!")



def view_history():
    print("\n Your Mood History:")
    try:
        with open("mood_log.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No mood history yet!")

if __name__ == "__main__":
    main()

def show_today_summary():
    today = datetime.datetime.now().date()
    moods_today = []

    try:
        with open("mood_log.txt", "r") as file:
            for line in file:
                timestamp_str, mood = line.strip().split(" - ")
                timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                if timestamp.date() == today:
                    moods_today.append(mood)
    except FileNotFoundError:
        print("\n📁 No mood logs found yet.")
        return

    if moods_today:
        print(f"\n📅 Today's Mood Summary ({len(moods_today)} logs):")
        for i, mood in enumerate(moods_today, 1):
            print(f"{i}. {mood}")
        print(f"\n💭 Most recent mood: {moods_today[-1]}")
    else:
        print("\n🕊️ You haven’t logged any moods today.")
