# File Handling Advanced (CSV, JSON, Pickle)

```python
# CSV File Handling
import csv

# Writing to CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "London"])

# Reading from CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# JSON File Handling
import json

# Writing JSON
data = {"name": "Alice", "age": 25, "city": "New York"}
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)

# Pickle File Handling
import pickle

# Writing Pickle
person = {"name": "Bob", "age": 30, "city": "London"}
with open("person.pkl", "wb") as file:
    pickle.dump(person, file)

# Reading Pickle
with open("person.pkl", "rb") as file:
    loaded_person = pickle.load(file)
    print(loaded_person)
