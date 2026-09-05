# ==========================================
# Functions in Python
# ==========================================

# Definition:
# A function is a reusable block of code designed to
# perform a specific task.
#
# Functions help us avoid code duplication and make
# the program easier to maintain and understand.


# ==========================================
# 1. Simple Function
# ==========================================

# Definition:
# A function can be created using the 'def' keyword.
# This function does not take any parameters.

def greet():
    print("Hello!")


# Calling the function
greet()


# ==========================================
# 2. Function with Parameters
# ==========================================

# Definition:
# Parameters are variables defined in a function.
# They allow us to pass data into the function.
#
# 'return' sends a value back to the caller.

def add(a, b):
    return a + b


result = add(5, 3)
print(result)


# ==========================================
# 3. Function with Default Parameters
# ==========================================

# Definition:
# A default parameter has a default value.
# If the caller does not provide a value,
# Python uses the default value.

def greet_name(name="User"):
    print(f"Hello, {name}!")


greet_name()          # Uses default value
greet_name("Alice")   # Uses provided value


# ==========================================
# 4. Function with Multiple Return Values
# ==========================================

# Definition:
# Python allows a function to return multiple values.
# Internally, Python returns them as a tuple,
# which can be unpacked into multiple variables.

def operations(x, y):
    return x + y, x * y, x - y


sum_, product, diff = operations(5, 2)

print(sum_)
print(product)
print(diff)


# ==========================================
# 5. Lambda Function
# ==========================================

# Definition:
# A lambda function is a small anonymous function.
# It is usually used for short operations where
# defining a complete function is unnecessary.
#
# Syntax:
# lambda arguments: expression

square = lambda x: x ** 2

print(square(5))


# ==========================================
# 6. Function Inside a Function
# ==========================================

# Definition:
# A function defined inside another function is called
# a nested function.
#
# The inner function can access variables from the
# outer function.

def outer(a):

    def inner(b):
        return a + b

    return inner


func = outer(10)

print(func(5))