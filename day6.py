
#simple function
def greet():
    print("Welcome to your daily wellness check-in 🌿")

#adding patameters
def suggest_meal(name):
    print(f"{name}, your nourishing meal today is a quinoa salad 🥗")

# Return a Value
def suggest_flow(mood):
    if mood == "sore":
        return "Stretch & Restore"
    elif mood == "pumped":
        return "Full Body Sculpt"
    else:
        return "Gentle Core + Breathwork"

flow = suggest_flow("pumped")
print(f"Based on your mood, try: {flow}")

# Real-World Example: AI Workout Suggestion
def recommend_workout(feeling):
    if feeling == "tired":
        return "Try a 10-min walk outside"
    elif feeling == "energized":
        return "Hit a Glutes & Thighs Sculpt class"
    else:
        return "Go for a calming mobility flow"
