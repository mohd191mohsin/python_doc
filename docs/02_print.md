# Python `print()` Function

The `print()` function in Python is used to display output on the screen.

## Basic Usage

```python
print("Hello, World!")
print(10)
print(3.14)


#Printing Multiple Values
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

#Using sep Parameter
print("apple", "banana", "cherry", sep=" | ")


#Using end Parameter

print("Hello", end=" ")
print("World")


#Printing Variables with f-strings

name = "Bob"
age = 30
print(f"My name is {name}, and I am {age} years old.")
