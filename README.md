# UDP Client and Server

This project demonstrates communication between a client and a server using
UDP datagram sockets in Python.

## Files

- `server.py` receives messages and sends a reply.
- `client.py` sends one message and displays the server's reply.

## How to run

Open two PowerShell terminals and run this command in both:

```powershell
cd "C:\Users\Administrator\Desktop\projects\User Datagram Protocol"
```

In the first terminal, start the server:

```powershell
python server.py
```

In the second terminal, start the client:

```powershell
python client.py
```

Type a message when prompted. For example:

```text
Enter a message for the server: Hello
Sending: Hello
Received from server ('127.0.0.1', 12345): Server received: Hello
```

Press `Ctrl+C` in the server terminal to stop the server.

If `python` is not recognized, use `py` instead:

```powershell
py server.py
py client.py
```

## Explanation of `server.py`

| Line | Code | Explanation |
|---:|---|---|
| 1 | `import socket` | Imports Python's built-in `socket` module for network communication. |
| 2 | *(blank)* | Blank line used for readability. |
| 3 | *(blank)* | Blank line used to separate the import from configuration. |
| 4 | `HOST = "127.0.0.1"` | Sets the server IP address. This address means the local computer. |
| 5 | `PORT = 12345` | Sets the UDP port on which the server listens. |
| 6 | `BUFFER_SIZE = 1024` | Sets the maximum number of bytes received at one time. |
| 7 | *(blank)* | Blank line used for readability. |
| 8 | *(blank)* | Blank line used to separate configuration from the function. |
| 9 | `def run_server():` | Defines the function that runs the server. |
| 10 | `"""Receive datagrams and send a reply to each client."""` | Documents the purpose of the function. |
| 11 | `with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:` | Creates an IPv4 UDP socket and closes it automatically when finished. |
| 12 | `server_socket.setsockopt(...)` | Allows the server to reuse the address after restarting. |
| 13 | `server_socket.bind((HOST, PORT))` | Assigns the IP address and port to the server socket. |
| 14 | *(blank)* | Blank line used for readability. |
| 15 | `print(f"UDP server listening on {HOST}:{PORT}")` | Displays the address where the server is listening. |
| 16 | `print("Press Ctrl+C to stop the server.")` | Tells the user how to stop the server. |
| 17 | *(blank)* | Blank line used for readability. |
| 18 | `try:` | Starts a block that handles a keyboard interruption. |
| 19 | `while True:` | Keeps the server running so it can receive multiple messages. |
| 20 | `data, client_address = server_socket.recvfrom(BUFFER_SIZE)` | Waits for a UDP datagram and gets its data and sender address. |
| 21 | `message = data.decode("utf-8")` | Converts the received bytes into readable UTF-8 text. |
| 22 | `print(f"Received from {client_address}: {message}")` | Displays the sender's address and message. |
| 23 | *(blank)* | Blank line used to separate receiving from replying. |
| 24 | `reply = f"Server received: {message}"` | Creates a response containing the received message. |
| 25 | `server_socket.sendto(...)` | Encodes and sends the response to the client. |
| 26 | `except KeyboardInterrupt:` | Catches `Ctrl+C` so the server can stop cleanly. |
| 27 | `print("\nServer stopped.")` | Displays a shutdown message. |
| 28 | *(blank)* | Blank line used for readability. |
| 29 | *(blank)* | Blank line used to separate the function from the entry point. |
| 30 | `if __name__ == "__main__":` | Checks whether the file is being run directly. |
| 31 | `run_server()` | Calls the function and starts the server. |

## Explanation of `client.py`

| Line | Code | Explanation |
|---:|---|---|
| 1 | `import socket` | Imports Python's built-in `socket` module. |
| 2 | *(blank)* | Blank line used for readability. |
| 3 | *(blank)* | Blank line used to separate the import from configuration. |
| 4 | `HOST = "127.0.0.1"` | Sets the server IP address. |
| 5 | `PORT = 12345` | Sets the server UDP port. |
| 6 | `BUFFER_SIZE = 1024` | Sets the maximum response size to receive. |
| 7 | *(blank)* | Blank line used for readability. |
| 8 | *(blank)* | Blank line used to separate configuration from the function. |
| 9 | `def run_client():` | Defines the function that runs the client. |
| 10 | `"""Send one datagram to the server and print its response."""` | Documents the purpose of the function. |
| 11 | `message = input(...)` | Reads a message typed by the user. |
| 12 | `server_address = (HOST, PORT)` | Combines the server IP address and port into an address tuple. |
| 13 | *(blank)* | Blank line used for readability. |
| 14 | `with socket.socket(...) as client_socket:` | Creates an IPv4 UDP socket and closes it automatically afterward. |
| 15 | `client_socket.settimeout(5)` | Waits a maximum of five seconds for a server response. |
| 16 | `print(f"Sending: {message}")` | Displays the message before it is sent. |
| 17 | `client_socket.sendto(...)` | Encodes the message and sends it to the server. |
| 18 | *(blank)* | Blank line used for readability. |
| 19 | `try:` | Starts a block that handles a possible timeout. |
| 20 | `data, server_address = client_socket.recvfrom(BUFFER_SIZE)` | Waits for the server response and gets its address. |
| 21 | `except socket.timeout:` | Handles the case where no response arrives in five seconds. |
| 22 | `print("No response...")` | Informs the user that the server did not respond. |
| 23 | `return` | Stops the client function after a timeout. |
| 24 | *(blank)* | Blank line used for readability. |
| 25 | `print(f"Received from server...")` | Decodes and displays the server response. |
| 26 | *(blank)* | Blank line used for readability. |
| 27 | *(blank)* | Blank line used to separate the function from the entry point. |
| 28 | `if __name__ == "__main__":` | Checks whether the file is being run directly. |
| 29 | `run_client()` | Calls the function and starts the client. |

## Important socket concepts

| Code or method | Meaning |
|---|---|
| `socket.AF_INET` | Uses IPv4 addresses. |
| `socket.SOCK_DGRAM` | Uses UDP datagrams. |
| `bind()` | Assigns an IP address and port to a socket. |
| `sendto()` | Sends a UDP message to a specific address. |
| `recvfrom()` | Receives a UDP message and the sender's address. |
| `encode("utf-8")` | Converts text into bytes for transmission. |
| `decode("utf-8")` | Converts received bytes back into text. |
