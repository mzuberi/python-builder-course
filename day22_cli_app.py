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
        else:
            print("Not a valid option. Try again!")

def write_journal():
    entry = input("Write your journal entry: ")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("journal_log.txt", "a") as file:
        file.write(f"{now} - {entry}\n")
    print(" Journal saved.")

def log_mood():
    mood = input("How are you feeling today? ")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("mood_log.txt", "a") as file:
        file.write(f"{now} - {mood}\n")
    print("Mood logged.")

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

