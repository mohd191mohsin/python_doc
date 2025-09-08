# Try-Except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Try-Except-Else
try:
    y = 5 + 5
except:
    print("Error")
else:
    print("No error, result:", y)

# Try-Except-Finally
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution finished")
