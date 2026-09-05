# ==========================================
# File Handling in Python
# ==========================================

# Definition:
# File handling is used to create, read, write, append,
# and modify files using Python.
#
# Python provides the built-in open() function for
# working with files.


# ==========================================
# 1. Writing to a File
# ==========================================

# Definition:
# The "w" mode opens a file for writing.
# If the file does not exist, Python creates it.
# If the file already exists, its previous content
# is overwritten.

f = open("test.txt", "w")

f.write("Hello, Python!\n")
f.write("File handling example.")

f.close()


# ==========================================
# 2. Reading from a File
# ==========================================

# Definition:
# The "r" mode opens a file for reading.
# The read() method reads the entire file content.

f = open("test.txt", "r")

content = f.read()

print(content)

f.close()


# ==========================================
# 3. Reading Line by Line
# ==========================================

# Definition:
# A file object is iterable, so we can use a for loop
# to read the file one line at a time.
#
# Reading line by line is useful when working with
# large files because we don't need to load the
# entire file into memory.

f = open("test.txt", "r")

for line in f:
    print(line.strip())

f.close()


# ==========================================
# 4. Using the with Statement
# ==========================================

# Definition:
# The "with" statement is the recommended way to
# work with files.
#
# It automatically closes the file after the block
# is completed, even if an exception occurs.

with open("test.txt", "a") as f:
    f.write("\nAppending new line")


with open("test.txt", "r") as f:
    print(f.read())