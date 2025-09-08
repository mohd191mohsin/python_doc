# Python Advanced Topics (Context Managers, Itertools, functools)

```python
# Context Managers
with open("example.txt", "w") as f:
    f.write("Hello, context manager!")

# Custom context manager using class
class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")

with MyContext() as mc:
    print("Inside context")

# Itertools examples
import itertools

# Infinite iterator
count = itertools.count(10, 2)
for i in range(5):
    print(next(count))

# Cycle
colors = ["red", "green", "blue"]
cycler = itertools.cycle(colors)
for i in range(6):
    print(next(cycler))

# Combinations
items = [1, 2, 3]
comb = list(itertools.combinations(items, 2))
print(comb)

# Permutations
perm = list(itertools.permutations(items))
print(perm)

# functools examples
from functools import reduce, lru_cache

# reduce
nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
print(total)

# lru_cache
@lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(10)])
