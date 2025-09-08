# Python Testing (unittest & pytest)

```python
# Using unittest
import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertNotEqual(add(2, 2), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertNotEqual(subtract(5, 3), 1)

if __name__ == "__main__":
    unittest.main()

# Using pytest
# Install pytest (run in terminal)
# pip install pytest

# Save this as test_math.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add():
    assert add(5, 3) == 8
    assert add(2, 2) != 5

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(5, 3) != 1

# Run pytest in terminal:
# pytest test_math.py
