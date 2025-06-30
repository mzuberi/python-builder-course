# 👀 Let's decide what workout to do based on energy

energy = "low"

if energy == "high":
    print("Let's do a Full Body Sculpt 💪🏽")
elif energy == "medium":
    print("Go for a Core Flow 🧘🏽‍♀️")
else:
    print("How about a Stretch + Restore 🌸")

# checks how many hours you slept and recommends a flow

hours_slept = 5

if hours_slept >= 8:
    print("You’re rested! Try a powerful glute sculpt 💥")
elif hours_slept >= 6:
    print("You’re doing alright, go for a steady full-body flow 🌿")
else:
    print("Be gentle with yourself. A slow stretch will feel good 💗")

# you can nest conditions too

mood = "tired"
weather = "rainy"

if mood == "tired" and weather == "rainy":
    print("Perfect day for journaling and a slow flow.")
