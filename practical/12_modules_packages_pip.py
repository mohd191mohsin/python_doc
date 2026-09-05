# ==========================================
# Modules, Packages, and pip in Python
# ==========================================

# Definition:
# A module is a Python file (.py) that contains reusable
# code such as functions, classes, and variables.
#
# A package is a directory containing related Python modules.
#
# pip is Python's package installer. It is used to install
# and manage external Python packages.


# ==========================================
# 1. Creating a Module
# ==========================================

# Suppose we create a file named:
# my_module.py
#
# Content of my_module.py:

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# ==========================================
# 2. Using a Module
# ==========================================

# Definition:
# The import statement allows us to use code from
# another Python module.

import my_module

print(my_module.add(5, 3))
print(my_module.subtract(10, 4))


# ==========================================
# 3. Importing a Specific Function
# ==========================================

# Definition:
# We can import only the required function from
# a module using 'from ... import'.

from my_module import add

print(add(7, 2))


# ==========================================
# 4. Using Aliases
# ==========================================

# Definition:
# An alias gives a module another name using
# the 'as' keyword.
#
# It is useful when we want a shorter module name.

import my_module as mm

print(mm.subtract(20, 5))


# ==========================================
# 5. Built-in Modules
# ==========================================

# Definition:
# Python provides many built-in modules that are
# available without installing external packages.

import os

# os.name gives information about the operating system.
print(os.name)

# os.getcwd() returns the current working directory.
print(os.getcwd())


import sys

# sys.version returns the Python version.
print(sys.version)


# ==========================================
# 6. Creating a Package
# ==========================================

# Definition:
# A package is a directory used to organize related
# Python modules.
#
# Example structure:
#
# my_package/
# ├── __init__.py
# ├── math_ops.py
# └── string_ops.py
#
# math_ops.py could contain:
#
# def multiply(a, b):
#     return a * b


# ==========================================
# 7. Using a Package
# ==========================================

# Definition:
# We can import a function from a specific module
# inside a package.

from my_package.math_ops import multiply

print(multiply(5, 4))


# ==========================================
# 8. pip
# ==========================================

# Definition:
# pip is Python's package installer.
# It is used to install, upgrade, and remove
# third-party Python packages.
#
# These commands are executed in the terminal,
# NOT inside a Python program.
#
# Install a package:
# pip install requests
#
# Upgrade a package:
# pip install --upgrade requests
#
# Remove a package:
# pip uninstall requests
#
# Show installed packages:
# pip list


# ==========================================
# 9. Using an Installed Package
# ==========================================

# Definition:
# After installing an external package using pip,
# we can import and use it in our Python program.

import requests

response = requests.get("https://www.example.com")

print(response.status_code)