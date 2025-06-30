# This function calculates the area of a rectangle
def calculate_area(length, width):
    area = length * width  # Area formula: length x width
    return area

# Ask user for input
user_length = float(input("Enter the length of the rectangle: "))
user_width = float(input("Enter the width of the rectangle: "))

# Call the function and store result
rectangle_area = calculate_area(user_length, user_width)

# Display the result to the user
print(f"The area of the rectangle is {rectangle_area} square units.")

# This function calculates the perimeter of a rectangle
def calculate_perimeter(length, width):
    return 2 * (length + width)

rectangle_perimeter = calculate_perimeter(user_length, user_width)
print(f"The perimeter of the rectangle is {rectangle_perimeter} units.")

