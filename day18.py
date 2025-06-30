name: str = "Mona"
age: int = 36
height: float = 5.4
is_certified: bool = True
favorite_moves: list[str] = ["Slow Flow", "Full Body Reset", "Soft Sculpt"]


# Day 18 - Type Hints Practice

def greet_user(name: str) -> str:
    return f"Hi {name}, welcome to your Python Builder course!"

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    return round(weight_kg / (height_m ** 2), 2)

def get_workout_by_energy(energy: int) -> str:
    if energy > 7:
        return "Full Body Sculpt"
    elif 4 <= energy <= 7:
        return "Soft Sculpt Stretch"
    else:
        return "Slow Flow Recovery"

# Main Program
if __name__ == "__main__":
    print(greet_user("Mona"))
    
    bmi = calculate_bmi(58.0, 1.62)
    print(f"Your BMI is: {bmi}")
    
    print("Workout suggestion based on energy level (1–10):")
    level = int(input("Enter your energy level: "))
    print("Suggested Workout:", get_workout_by_energy(level))
