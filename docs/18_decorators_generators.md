# Decorators and Generators

```python
# Decorators
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with Arguments
def decorator_args(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@decorator_args
def add(a, b):
    return a + b

print(add(5, 3))

# Generators
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

# Generator with loop
for value in my_generator():
    print(value)

# Generator expression
squared = (x**2 for x in range(5))
for num in squared:
    print(num)
