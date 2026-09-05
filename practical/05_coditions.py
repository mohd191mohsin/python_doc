# ==========================================
# Conditional Statements in Python
# ==========================================

# Definition:
# Conditional statements are used to make decisions
# in a program based on whether a condition is True or False.


# ==========================================
# 1. If Statement
# ==========================================

# Definition:
# An if statement executes a block of code only when
# the given condition is True.

x = 10

if x > 5:
    print("x is greater than 5")


# ==========================================
# 2. If-Else Statement
# ==========================================

# Definition:
# An if-else statement provides two possible paths.
# If the condition is True, the if block executes.
# Otherwise, the else block executes.

y = 3

if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")


# ==========================================
# 3. If-Elif-Else Statement
# ==========================================

# Definition:
# An if-elif-else statement is used when we need
# to check multiple conditions.
#
# if    -> Checks the first condition
# elif  -> Checks another condition if the previous
#          condition was False
# else  -> Executes when all conditions are False

marks = 85

if marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 50:
    print("Grade: C")

else:
    print("Grade: F")


# ==========================================
# 4. Nested If Statement
# ==========================================

# Definition:
# A nested if statement means using one if statement
# inside another if statement.
# It is useful when a second condition depends on
# the first condition.

age = 20

if age >= 18:

    if age < 21:
        print("You are an adult but not 21 yet")

    else:
        print("You are 21 or older")

else:
    print("You are a minor")