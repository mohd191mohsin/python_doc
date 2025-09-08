# List & Dictionary Comprehensions and Advanced Collections

```python
# List Comprehensions
nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums]
print(squared)

# List comprehension with condition
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)

# Dictionary Comprehensions
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
score_dict = {names[i]: scores[i] for i in range(len(names))}
print(score_dict)

# Dictionary comprehension with condition
high_scores = {name: score for name, score in score_dict.items() if score > 80}
print(high_scores)

# Set Comprehensions
num_set = {x**2 for x in range(6)}
print(num_set)

# Advanced Collections
from collections import Counter, defaultdict, namedtuple, deque, OrderedDict

# Counter
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(word_count)

# defaultdict
d = defaultdict(int)
d["a"] += 1
d["b"] += 2
print(d)

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)

# deque
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(dq)

# OrderedDict
od = OrderedDict()
od["one"] = 1
od["two"] = 2
od["three"] = 3
print(od)
