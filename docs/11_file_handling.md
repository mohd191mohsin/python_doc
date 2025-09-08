# Writing to a file
f = open("test.txt", "w")
f.write("Hello, Python!\n")
f.write("File handling example.")
f.close()

# Reading from a file
f = open("test.txt", "r")
content = f.read()
print(content)
f.close()

# Reading line by line
f = open("test.txt", "r")
for line in f:
    print(line.strip())
f.close()

# Using with statement (auto close)
with open("test.txt", "a") as f:
    f.write("\nAppending new line")

with open("test.txt", "r") as f:
    print(f.read())
