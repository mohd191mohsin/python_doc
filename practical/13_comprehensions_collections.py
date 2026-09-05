# ==========================================
# List, Dictionary & Set Comprehensions
# ==========================================

# Definition:
# A comprehension is a concise way to create a new
# collection from an existing iterable.
#
# Python supports:
# 1. List comprehension
# 2. Dictionary comprehension
# 3. Set comprehension


# ==========================================
# 1. List Comprehension
# ==========================================

# Definition:
# List comprehension provides a short and readable way
# to create a new list using an existing iterable.
#
# Syntax:
# [expression for item in iterable]

nums = [1, 2, 3, 4, 5]

squared = [x ** 2 for x in nums]

print(squared)


# ==========================================
# 2. List Comprehension with Condition
# ==========================================

# Definition:
# A condition can be added to a list comprehension
# to include only elements that satisfy the condition.
#
# Syntax:
# [expression for item in iterable if condition]

even_nums = [x for x in nums if x % 2 == 0]

print(even_nums)


# ==========================================
# 3. Dictionary Comprehension
# ==========================================

# Definition:
# Dictionary comprehension provides a concise way
# to create a dictionary using an iterable.
#
# Syntax:
# {key: value for item in iterable}

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

score_dict = {
    names[i]: scores[i]
    for i in range(len(names))
}

print(score_dict)


# ==========================================
# 4. Dictionary Comprehension with Condition
# ==========================================

# Definition:
# A condition can be added to dictionary comprehension
# to include only the required key-value pairs.

high_scores = { 
    name: score
    for name, score in score_dict.items()
    if score > 80
}

print(high_scores)


# ==========================================
# 5. Set Comprehension
# ==========================================

# Definition:
# Set comprehension provides a concise way to create
# a set from an iterable.
#
# Since sets contain unique values, duplicate results
# are automatically removed.

num_set = {x ** 2 for x in range(6)}

print(num_set)


# ==========================================
# Advanced Collections
# ==========================================

# Definition:
# The collections module provides specialized
# container data types that extend Python's
# built-in collection types.

from collections import (
    Counter,
    defaultdict,
    namedtuple,
    deque,
    OrderedDict
)


# ==========================================
# 6. Counter
# ==========================================

# Definition:
# Counter is a dictionary subclass used to count
# the frequency of elements in an iterable.
#
# It is useful for counting words, characters,
# numbers, or other repeated values.

words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]

word_count = Counter(words)

print(word_count)


# ==========================================
# 7. defaultdict
# ==========================================

# Definition:
# defaultdict is a dictionary subclass that provides
# a default value when a key does not exist.
#
# It avoids KeyError when accessing missing keys.

d = defaultdict(int)

d["a"] += 1
d["b"] += 2

print(d)


# ==========================================
# 8. namedtuple
# ==========================================

# Definition:
# namedtuple creates tuple-like objects whose values
# can be accessed using meaningful field names.
#
# It is useful when we want the benefits of a tuple
# with more readable attribute access.

Point = namedtuple("Point", ["x", "y"])

p = Point(10, 20)

print(p.x)
print(p.y)


# ==========================================
# 9. deque
# ==========================================

# Definition:
# deque stands for "double-ended queue".
# It allows efficient insertion and removal of elements
# from both the left and right sides.

dq = deque([1, 2, 3])

dq.append(4)       # Add to the right
dq.appendleft(0)   # Add to the left

dq.pop()           # Remove from the right
dq.popleft()       # Remove from the left

print(dq)


# ==========================================
# 10. OrderedDict
# ==========================================

# Definition:
# OrderedDict is a dictionary subclass that provides
# operations for working with dictionary order.
#
# In modern Python (3.7+), regular dictionaries also
# preserve insertion order, so OrderedDict is less
# commonly required for basic ordering.

od = OrderedDict()

od["one"] = 1
od["two"] = 2
od["three"] = 3

print(od)