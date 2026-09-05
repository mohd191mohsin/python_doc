# ==========================================
# Creating Variables
# ==========================================

# Definition:
# A variable is a name used to store a value in memory.
# Python automatically determines the data type based on the value.

x = 10
y = 3.14
name = "Alice"

print(x)
print(y)
print(name)


# ==========================================
# Variable Naming Rules
# ==========================================

# Definition:
# Variable names can contain letters, numbers, and underscores.
# A variable name cannot start with a number.
# Python keywords cannot be used as variable names.
# Variable names are case-sensitive.

age = 25
first_name = "Bob"
_name = "secret"

print(age)
print(first_name)
print(_name)


# ==========================================
# Invalid Variable Names
# ==========================================

# Variable names cannot start with a number.
# 2nd_place = "Tom"     # Invalid

# Python keywords cannot be used as variable names.
# for = "loop"          # Invalid


# ==========================================
# Changing Variable Values
# ==========================================

# Definition:
# Python variables are dynamically typed.
# This means the same variable can hold values of different data types
# at different points in the program.

x = 100
print(x)

x = "Now I am text"
print(x)


# ==========================================
# Multiple Assignments
# ==========================================

# Definition:
# Python allows us to assign values to multiple variables
# in a single statement.

a, b, c = 1, 2, 3

print(a, b, c)


# We can also assign the same value to multiple variables.

x = y = z = 10

print(x, y, z)


# ==========================================
# Data Types of Variables
# ==========================================

# Definition:
# The type() function is used to check the data type
# of a variable or value.

num = 42
pi = 3.1416
name = "Alice"
is_active = True
items = [1, 2, 3]

print(type(num))        # int
print(type(pi))         # float
print(type(name))       # str
print(type(is_active))  # bool
print(type(items))      # list