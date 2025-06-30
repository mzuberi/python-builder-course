# for Loops — Flows on Repeat
flows = ["Full Body Sculpt", "Core Burn", "Stretch & Restore"]

for flow in flows:
    print(f"Today’s workout suggestion: {flow}")



# while Loops — Loop Until You're Done
energy = 3

while energy > 0:
    print("Do a few gentle stretches 🧘🏽")
    energy -= 1  # Decrease energy by 1


# add some logic
flows = ["Glutes", "Arms", "Core"]

for i in range(len(flows)):
    print(f"Day {i+1}: Focus on {flows[i]}")

