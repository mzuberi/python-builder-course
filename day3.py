# 🧺 A list is like a basket that can hold multiple things

favorite_foods = ["mango", "biryani", "pizza"]
print(f"My favorite foods are: {favorite_foods}")

# 🎯 Accessing items
print("I love", favorite_foods[0])  # mango
print("Also love", favorite_foods[2])  # biryani 

# ✏️ Changing an item
favorite_foods[1] = "veggie biryani"
print("Updated foods:", favorite_foods)

# ➕ Adding to the list
favorite_foods.append("green smoothie")
print("After adding:", favorite_foods)

# ❌ Removing an item
favorite_foods.remove("mango")
print("After removing mango:", favorite_foods)




daily_moves = ["bridge", "plank", "hundred"]
print(f"My go-to move is {daily_moves[0]}")
daily_moves.append("side kick")
daily_moves.remove("plank")
print("Updated moves:", daily_moves)
