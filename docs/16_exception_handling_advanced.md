# Exception Handling Advanced & Custom Exceptions

```python
# Multiple Except Blocks
try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("ValueError occurred")
except ZeroDivisionError:
    print("ZeroDivisionError occurred")

# Catching Multiple Exceptions in One Block
try:
    x = int("xyz")
    y = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

# Else with Try-Except
try:
    x = 5 + 5
except:
    print("Error occurred")
else:
    print("No error, result:", x)

# Finally with Try-Except
try:
    f = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution finished")

# Raising an Exception
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)

# Custom Exception
class CustomError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise CustomError("Negative value not allowed")
    return x

try:
    check_value(-5)
except CustomError as e:
    print("Custom Exception:", e)
