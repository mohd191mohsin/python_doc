# ==========================================
# Python Operators
# ==========================================

# Definition:
# Operators are symbols or keywords used to perform
# operations on values and variables.


# ==========================================
# Arithmetic Operators
# ==========================================

# Definition:
# Arithmetic operators are used to perform mathematical
# operations such as addition, subtraction, multiplication,
# and division.

x = 10
y = 3

print(x + y)   # Addition: 13
print(x - y)   # Subtraction: 7
print(x * y)   # Multiplication: 30
print(x / y)   # Division: 3.333...
print(x % y)   # Modulus: 1 (remainder)
print(x ** y)  # Exponent: 1000
print(x // y)  # Floor division: 3


# ==========================================
# Comparison Operators
# ==========================================

# Definition:
# Comparison operators are used to compare two values.
# They return a Boolean result: True or False.

print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to


# ==========================================
# Logical Operators
# ==========================================

# Definition:
# Logical operators are used to combine or reverse
# conditional expressions.
#
# and  -> True only when both conditions are True
# or   -> True when at least one condition is True
# not  -> Reverses the Boolean value

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False


# ==========================================
# Assignment Operators
# ==========================================

# Definition:
# Assignment operators are used to assign values to
# variables and update their values.

z = 5

z += 3          # Same as: z = z + 3
print(z)        # 8

z -= 2          # Same as: z = z - 2
print(z)        # 6

z *= 4          # Same as: z = z * 4
print(z)        # 24

z /= 3          # Same as: z = z / 3
print(z)        # 8.0


# ==========================================
# Membership Operators
# ==========================================

# Definition:
# Membership operators are used to check whether
# a value exists inside a sequence such as a list,
# tuple, string, or set.
#
# in     -> Checks whether a value exists
# not in -> Checks whether a value does not exist

nums = [1, 2, 3, 4, 5]

print(3 in nums)       # True
print(6 not in nums)   # True


# ==========================================
# Identity Operators
# ==========================================

# Definition:
# Identity operators are used to check whether two
# variables refer to the same object in memory.
#
# is     -> Checks whether both variables refer to the same object
# is not -> Checks whether they refer to different objects

m = [1, 2, 3]
n = [1, 2, 3]

print(m is n)          # False
print(m is not n)      # True