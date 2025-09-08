# Python Project Structure & Best Practices

```text
# Recommended Python Project Structure
my_project/
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── main.py
├── config/
│   └── settings.py
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_app.py
└── data/
    └── sample_data.csv




# Example of a main.py
from app.utils import greet

def main():
    print("Starting application...")
    greet("Alice")

if __name__ == "__main__":
    main()



# Example of utils.py
def greet(name):
    print(f"Hello, {name}!")



# Best Practices

1. Use virtual environments (`venv` or `conda`)
2. Follow PEP8 coding standards
3. Separate code into modules and packages
4. Write tests using unittest or pytest
5. Use logging instead of print for production
6. Keep configuration separate (config/settings.py)
7. Use requirements.txt to manage dependencies
8. Document code with docstrings and README.md
9. Handle exceptions gracefully
10. Version control your project (git)
