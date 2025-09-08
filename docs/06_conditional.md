# If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# If-Else Statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

# If-Elif-Else Statement
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Nested If
age = 20
if age >= 18:
    if age < 21:
        print("You are an adult but not 21 yet")
    else:
        print("You are 21 or older")
else:
    print("You are a minor")
