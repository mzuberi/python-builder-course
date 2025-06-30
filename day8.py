# Define a Dictionary of Plans
plans = {
    "sore": {
        "flow": "Stretch & Restore",
        "duration": 20,
        "intention": "gentle release"
    },
    "energized": {
        "flow": "Full Body Burn",
        "duration": 30,
        "intention": "build heat"
    },
    "stiff": {
        "flow": "Mobility Flow",
        "duration": 25,
        "intention": "create space"
    },
    "tired": {
        "flow": "Gentle Core",
        "duration": 15,
        "intention": "slow activation"
    }
}

# Ask for Mood + Return a Plan
user_mood = input("How are you feeling today? ").lower()

if user_mood in plans:
    plan = plans[user_mood]
    print(f"\n🌿 Your Personalized Wellness Plan 🌿")
    print(f"Flow: {plan['flow']}")
    print(f"Duration: {plan['duration']} minutes")
    print(f"Intention: {plan['intention']}")
else:
    print("Sorry, I don't have a plan for that mood yet.")

