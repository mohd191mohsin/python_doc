# Python Networking (sockets, requests, HTTP)

```python
# Using sockets
import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server
s.connect(("example.com", 80))

# Send a request
request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
s.send(request.encode())

# Receive response
response = s.recv(4096)
print(response.decode())

s.close()

# Using requests module
import requests

# GET request
response = requests.get("https://www.example.com")
print(response.status_code)
print(response.text[:200])  # Print first 200 chars

# POST request
data = {"name": "Alice", "age": 25}
response = requests.post("https://httpbin.org/post", data=data)
print(response.json())

# HTTP headers
headers = {"User-Agent": "MyApp/1.0"}
response = requests.get("https://www.example.com", headers=headers)
print(response.status_code)

# Handling timeouts
try:
    response = requests.get("https://www.example.com", timeout=2)
    print(response.status_code)
except requests.Timeout:
    print("Request timed out")
