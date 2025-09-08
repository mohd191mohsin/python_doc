## Classes & Objects
```python
# Defining a Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating Objects
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

p1.greet()
p2.greet()

# Accessing Attributes
print(p1.name)
print(p2.age)

# Modifying Attributes
p1.age = 26
print(p1.age)

# Class with Class Variable
class Dog:
    species = "Canine"

    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name, dog1.species)
print(dog2.name, dog2.species)

# Inheritance
class Animal:
    def sound(self):
        print("Some sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
c.sound()

# Encapsulation (private attributes)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())

# Polymorphism
class Bird:
    def speak(self):
        print("Tweet")

class Parrot(Bird):
    def speak(self):
        print("I can talk!")

b = Bird()
p = Parrot()
b.speak()
p.speak()
