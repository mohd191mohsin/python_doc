# For Loop
for i in range(5):
    print("Number:", i)

# While Loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Loop with else
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop finished")

# Break in Loop
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue in Loop
for i in range(5):
    if i == 2:
        continue
    print(i)

# Nested Loops
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")
