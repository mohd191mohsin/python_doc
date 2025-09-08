# Modules, Packages, and pip

```python
# Creating a Module (save as my_module.py)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Using the Module
import my_module

print(my_module.add(5, 3))
print(my_module.subtract(10, 4))

# Import specific function
from my_module import add
print(add(7, 2))

# Using Aliases
import my_module as mm
print(mm.subtract(20, 5))

# Built-in Modules
import os
print(os.name)
print(os.getcwd())

import sys
print(sys.version)

# Creating a Package (folder structure)
# my_package/
# ├── __init__.py
# ├── math_ops.py
# └── string_ops.py

# Using a package
from my_package.math_ops import multiply
print(multiply(5, 4))

# Using pip to install external packages
# Example (run in terminal, not Python code)
# pip install requests

# Using installed package
import requests
response = requests.get("https://www.example.com")
print(response.status_code)
