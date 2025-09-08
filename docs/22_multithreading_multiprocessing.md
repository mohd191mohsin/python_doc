# Python Multithreading and Multiprocessing

```python
# Multithreading
import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in "ABCDE":
        print(f"Letter: {letter}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Threads finished")

# Multiprocessing
from multiprocessing import Process

def square(n):
    print(f"Square of {n} is {n**2}")

if __name__ == "__main__":
    p1 = Process(target=square, args=(5,))
    p2 = Process(target=square, args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Processes finished")
