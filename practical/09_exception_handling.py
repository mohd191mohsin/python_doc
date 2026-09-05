# ==========================================
# Exception Handling in Python
# ==========================================

# Definition:
# Exception handling is used to handle runtime errors
# without stopping the entire program unexpectedly.
#
# Python mainly uses:
# try, except, else, and finally
# to handle exceptions.


# ==========================================
# 1. Try-Except
# ==========================================

# Definition:
# The try block contains code that may cause an exception.
# The except block handles the exception if it occurs.

try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")


# ==========================================
# 2. Try-Except-Else
# ==========================================

# Definition:
# The else block executes only when no exception
# occurs in the try block.
#
# try   -> Code that may cause an exception
# except -> Handles the exception
# else  -> Runs when there is no exception

try:
    y = 5 + 5

except:
    print("Error")

else:
    print("No error, result:", y)


# ==========================================
# 3. Try-Except-Finally
# ==========================================

# Definition:
# The finally block always executes whether an exception
# occurs or not.
#
# It is commonly used for cleanup operations such as
# closing files, database connections, or network resources.

try:
    f = open("file.txt")

except FileNotFoundError:
    print("File not found")

finally:
    print("Execution finished")