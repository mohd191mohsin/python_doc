# ==========================================
# Loops in Python
# ==========================================

# Definition:
# A loop is used to execute a block of code repeatedly
# until a specific condition is met or all items in a
# sequence have been processed.


# ==========================================
# 1. For Loop
# ==========================================

# Definition:
# A for loop is used to iterate over a sequence or
# iterable, such as a list, tuple, string, or range.
#
# range(5) generates numbers from 0 to 4.

for i in range(5):
    print("Number:", i)


# ==========================================
# 2. While Loop
# ==========================================

# Definition:
# A while loop repeatedly executes a block of code
# as long as the given condition remains True.
#
# We must update the condition inside the loop to
# avoid creating an infinite loop.

count = 0

while count < 5:
    print("Count:", count)
    count += 1


# ==========================================
# 3. Loop with Else
# ==========================================

# Definition:
# Python allows an else block with loops.
# The else block executes when the loop completes
# normally without being stopped by a break statement.

for i in range(3):
    print("Iteration:", i)

else:
    print("Loop finished")


# ==========================================
# 4. Break Statement
# ==========================================

# Definition:
# The break statement immediately terminates the loop
# and transfers control to the statement after the loop.

for i in range(10):

    if i == 5:
        break

    print(i)


# ==========================================
# 5. Continue Statement
# ==========================================

# Definition:
# The continue statement skips the current iteration
# and moves directly to the next iteration of the loop.

for i in range(5):

    if i == 2:
        continue

    print(i)


# ==========================================
# 6. Nested Loops
# ==========================================

# Definition:
# A nested loop is a loop inside another loop.
# The inner loop runs completely for every iteration
# of the outer loop.

for i in range(1, 4):

    for j in range(1, 3):
        print(f"i={i}, j={j}")