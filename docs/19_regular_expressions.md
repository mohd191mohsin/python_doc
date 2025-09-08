# Regular Expressions (re module)

```python
import re

# Simple match
pattern = r"hello"
text = "hello world"
match = re.match(pattern, text)
print(match.group() if match else "No match")

# Search
pattern = r"world"
search = re.search(pattern, text)
print(search.group() if search else "No match")

# Find all
pattern = r"\d+"
text = "There are 12 apples and 30 bananas"
numbers = re.findall(pattern, text)
print(numbers)

# Split
pattern = r"\s+"
text = "Split this text by spaces"
result = re.split(pattern, text)
print(result)

# Substitution
pattern = r"apples"
text = "I like apples"
new_text = re.sub(pattern, "oranges", text)
print(new_text)

# Compile pattern
pattern = re.compile(r"[A-Za-z]+")
matches = pattern.findall("Hello 123 World 456")
print(matches)

# Using groups
pattern = r"(\d+)-(\d+)-(\d+)"
text = "Date: 2025-09-08"
match = re.search(pattern, text)
if match:
    print(match.group(0))  # full match
    print(match.group(1))  # first group
    print(match.group(2))  # second group
    print(match.group(3))  # third group
