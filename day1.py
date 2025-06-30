""" 
def suggest_workout(mood):
    mood_workout_map = {
        "sore": "Soft Sculpt",
        "pumped": "Full Body Reset",
        "tired": "Slow Flow Stretch",
        "anxious": "Grounding Core"
    }
    return mood_workout_map.get(mood.lower(), "Gentle Walk or Rest Day")

user_mood = input("How are you feeling today? ")
suggestion = suggest_workout(user_mood)
print(f"Suggested workout for your mood: {suggestion}") """




# Day 1: Python Builder — Core Concepts

# 1. Variables and Types
name = "Mona"
project = "Wellness AI Chatbot"
days_learning = 1
is_motivated = True

# 2. Print Statements
print("Hi, my name is", name)
print("I'm building a", project)
print("I've been learning for", days_learning, "day(s). Am I motivated?", is_motivated)

# 3. Bonus: Create a short wellness journal entry
feeling = "pumped"
workout_today = "Soft Sculpt Glute Flow"
journal_entry = f"Today I felt {feeling}, so I did the {workout_today}. It felt amazing!"

print("\n🧘 Wellness Journal:")
print(journal_entry)

