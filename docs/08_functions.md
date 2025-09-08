# Simple Function
def greet():
    print("Hello!")

greet()

# Function with Parameters
def add(a, b):
    return a + b

print(add(5, 3))

# Function with Default Parameters
def greet_name(name="User"):
    print(f"Hello, {name}!")

greet_name()
greet_name("Alice")

# Function with Multiple Return Values
def operations(x, y):
    return x+y, x*y, x-y

sum_, product, diff = operations(5, 2)
print(sum_, product, diff)

# Lambda Function
square = lambda x: x**2
print(square(5))

# Function inside a Function
def outer(a):
    def inner(b):
        return a+b
    return inner

func = outer(10)
print(func(5))
