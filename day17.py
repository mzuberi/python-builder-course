# Day 17 - Wellness Assistant CLI

def breathwork_tip():
    return "Try this: Inhale for 4, hold for 4, exhale for 6. Repeat 3x."

def workout_suggestion(mood):
    if mood == "tired":
        return "Do a Slow Flow Stretch or go for a short walk."
    elif mood == "energized":
        return "Time for Full Body Sculpt or Core & Glutes!"
    else:
        return "Try Soft Sculpt for a gentle yet effective workout."

def mindset_quote():
    return "“You are the sky. Everything else – it’s just the weather.” – Pema Chödrön"

def main():
    print("✨ Welcome to your Wellness Assistant ✨")
    mood = input("How are you feeling today? (tired/energized/neutral): ").strip().lower()

    print("\n💨 Breathwork Tip:")
    print(breathwork_tip())

    print("\n💪 Workout Suggestion:")
    print(workout_suggestion(mood))

    print("\n🧘 Mindset Quote:")
    print(mindset_quote())

if __name__ == "__main__":
    main()
