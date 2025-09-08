# Python Debugging and Logging

```python
# Debugging with print statements
x = 10
y = 0

print("Before division")
try:
    result = x / y
except ZeroDivisionError:
    print("Division by zero error")
print("After division")

# Using assert for debugging
def divide(a, b):
    assert b != 0, "b cannot be zero"
    return a / b

# divide(10, 0)  # This will raise AssertionError

# Using logging module
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename="app.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("This is a debug message")
logging.info("Informational message")
logging.warning("Warning message")
logging.error("Error occurred")
logging.critical("Critical issue")

# Example usage in code
def calculate_area(radius):
    if radius < 0:
        logging.error("Radius cannot be negative")
        return None
    area = 3.1416 * radius ** 2
    logging.info(f"Area calculated: {area}")
    return area

calculate_area(5)
calculate_area(-3)

# Debugging with pdb (interactive)
# Uncomment to use
# import pdb
# pdb.set_trace()
# x = 10
# y = 20
# z = x + y
# print(z)
