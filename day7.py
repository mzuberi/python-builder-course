# List of flows
flows = ["Gentle Core", "Stretch & Restore", "Glutes & Thighs Sculpt", "Full Body Burn", "Mobility Flow"]

# Function to Suggest a Flow Based on Mood
def recommend_flow(mood):
    if mood == "sore":
        return flows[1]  # Stretch & Restore
    elif mood == "energized":
        return flows[2]  # Glutes & Thighs Sculpt
    elif mood == "stiff":
        return flows[4]  # Mobility Flow
    else:
        return flows[0]  # Gentle Core

# Ask User for Input + Call the Function
user_mood = input("How are you feeling today? ").lower()
flow = recommend_flow(user_mood)
print(f"Based on your mood, try this flow: {flow}")

