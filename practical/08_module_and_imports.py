# ==========================================
# Modules in Python
# ==========================================

# Definition:
# A module is a Python file that contains reusable code,
# such as functions, classes, and variables.
#
# Modules help us organize code and reuse functionality
# without writing the same code again.


# ==========================================
# 1. Import Entire Module
# ==========================================

# Definition:
# The 'import' statement imports an entire module.
# We can access its functions and variables using
# the module name followed by a dot (.).

import math

print(math.sqrt(16))
print(math.pi)


# ==========================================
# 2. Import a Specific Function
# ==========================================

# Definition:
# 'from module import function' allows us to import
# only a specific function or object from a module.
#
# After importing, we can use the function directly
# without writing the module name.

from math import factorial

print(factorial(5))


# ==========================================
# 3. Import Module with an Alias
# ==========================================

# Definition:
# An alias gives a module a shorter or alternative name.
# The 'as' keyword is used to create an alias.
#
# This is useful when a module name is long or when
# we want a shorter name for convenience.

import random as rnd

print(rnd.randint(1, 10))


# ==========================================
# 4. Built-in Module Example
# ==========================================

# Definition:
# Python provides many built-in modules that can be
# used without installing external packages.
#
# The datetime module provides classes and functions
# for working with dates and times.

import datetime

print(datetime.datetime.now())