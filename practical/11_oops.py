# ==========================================
# Classes and Objects in Python
# ==========================================

# Definition:
# A class is a blueprint used to create objects.
# An object is an instance of a class.
#
# A class can contain attributes (data) and methods (functions).


# ==========================================
# 1. Defining a Class
# ==========================================

# Definition:
# A class is created using the 'class' keyword.
# __init__() is a constructor that is automatically called
# when an object is created.
#
# 'self' refers to the current object.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(
            f"Hello, my name is {self.name} "
            f"and I am {self.age} years old."
        )


# ==========================================
# 2. Creating Objects
# ==========================================

# Definition:
# An object is an instance of a class.
# We create an object by calling the class like a function.

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

p1.greet()
p2.greet()


# ==========================================
# 3. Accessing Attributes
# ==========================================

# Definition:
# Attributes are variables associated with an object.
# We access them using the dot (.) operator.

print(p1.name)
print(p2.age)


# ==========================================
# 4. Modifying Attributes
# ==========================================

# Definition:
# Object attributes can be modified after the object
# has been created, provided they are accessible.

p1.age = 26

print(p1.age)


# ==========================================
# 5. Class Variable
# ==========================================

# Definition:
# A class variable is shared by all objects of the class.
# It is defined directly inside the class, outside methods.

class Dog:

    # Class variable
    species = "Canine"

    def __init__(self, name):
        # Instance variable
        self.name = name


dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name, dog1.species)
print(dog2.name, dog2.species)


# ==========================================
# 6. Inheritance
# ==========================================

# Definition:
# Inheritance allows a child class to reuse attributes
# and methods from a parent class.
#
# Animal -> Parent class
# Cat    -> Child class

class Animal:

    def sound(self):
        print("Some sound")


class Cat(Animal):

    def sound(self):
        print("Meow")


c = Cat()

c.sound()


# ==========================================
# 7. Encapsulation
# ==========================================

# Definition:
# Encapsulation means bundling data and methods together
# and restricting direct access to internal data.
#
# In Python, __ before an attribute triggers name mangling,
# commonly used to indicate that an attribute is intended
# for internal/private use.

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


# ==========================================
# 8. Polymorphism
# ==========================================

# Definition:
# Polymorphism means the same method name can behave
# differently depending on the object that calls it.

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