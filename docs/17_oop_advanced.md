# Object-Oriented Programming Advanced

```python
# Inheritance
class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

d = Dog()
c = Cat()
d.speak()
c.speak()

# Multilevel Inheritance
class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(B):
    def show_c(self):
        print("Class C")

obj = C()
obj.show_a()
obj.show_b()
obj.show_c()

# Multiple Inheritance
class X:
    def x_method(self):
        print("X method")

class Y:
    def y_method(self):
        print("Y method")

class Z(X, Y):
    pass

z = Z()
z.x_method()
z.y_method()

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

# Encapsulation (private attributes)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
