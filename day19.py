# Day 19 – Handling Errors Gracefully

def divide_numbers(a: float, b: float) -> float:
    try:
        result = a / b
        return round(result, 2)
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except Exception as e:
        return f"Something went wrong: {e}"

print("=== Division Tool ===")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

print("Result:", divide_numbers(x, y))


def get_energy_level() -> int:
    try:
        level = int(input("How energized are you today (1-10)? "))
        if 1 <= level <= 10:
            return level
        else:
            print("Please enter a number between 1 and 10.")
            return get_energy_level()
    except ValueError:
        print("Oops! Enter a number only.")
        return get_energy_level()

energy = get_energy_level()
print(f"Thanks! Your energy level is: {energy}")


#save errors to log file
import datetime

def log_error(error_message: str):
    with open("error_log.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {error_message}\n")

except Exception as e:
    log_error(str(e))
    return "Something went wrong. We've logged the issue."
