# Function to calculate area
def calculate_area(length, width):
    return length * width

# Function to calculate perimeter
def calculate_perimeter(length, width):
    return 2 * (length + width)

# Function to give size feedback
def size_feedback(area):
    if area > 100:
        return "Wow, that's a big rectangle!"
    elif area > 50:
        return "Pretty spacious!"
    else:
        return "Compact and cozy."

# Main flow
user_length = float(input("Enter length: "))
user_width = float(input("Enter width: "))

area = calculate_area(user_length, user_width)
perimeter = calculate_perimeter(user_length, user_width)
feedback = size_feedback(area)

print("\n📏 Rectangle Summary")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
print(feedback)
