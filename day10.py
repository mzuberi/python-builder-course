def suggest_workout(mood):
    if mood.lower() == "sore":
        return "Try the Soft Sculpt Recovery Flow — slow and stretchy to release tension."
    elif mood.lower() == "pumped":
        return "Let’s go! Do the Full Body Reset Sculpt workout to match your energy."
    elif mood.lower() == "low energy":
        return "Start with a Calm & Grounded Flow. Gentle movement will wake you up."
    elif mood.lower() == "anxious":
        return "Try a Pilates + Breathwork flow to soothe your nervous system."
    else:
        return "How about a Walk and Core Flow? Gentle yet energizing."

# Ask the User and Show a Suggestion
mood_input = input("How are you feeling today? ").strip()
recommendation = suggest_workout(mood_input)
print(f"\nSuggested Workout:\n{recommendation}")

#