# UDP Client and Server

A small Python example showing how a client and a server communicate with
**UDP datagram sockets**.

## Features

- Uses IPv4 and UDP.
- Sends a message from the client to the server.
- Sends a response from the server back to the client.
- Demonstrates `sendto()` and `recvfrom()`.
- Uses only Python's standard library.

## Requirements

- Python 3.8 or newer
- No external packages are required.

Check that Python is installed:

```bash
python --version
```

On some Windows installations, use:

```powershell
py --version
```

## Project structure

```text
.
├── client.py
├── server.py
└── README.md
```

## Usage

Clone the repository and enter its directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

Open two terminals in the repository directory.

### 1. Start the server

In the first terminal, run:

```bash
python server.py
```

The server should display:

```text
UDP server listening on 127.0.0.1:12345
Press Ctrl+C to stop the server.
```

### 2. Start the client

In the second terminal, run:

```bash
python client.py
```

Enter a message when prompted:

```text
Enter a message for the server: Hello
Sending: Hello
Received from server ('127.0.0.1', 12345): Server received: Hello
```

On Windows, use `py` instead of `python` if necessary:

```powershell
py server.py
py client.py
```

Press `Ctrl+C` in the server terminal to stop it.

## Configuration

Both scripts use these default values:

| Setting | Value | Description |
|---|---|---|
| Host | `127.0.0.1` | The local computer. |
| Port | `12345` | The UDP port used by the server. |
| Buffer size | `1024` bytes | Maximum datagram size read by the examples. |

To communicate between different computers, change `HOST` in `client.py` to
the server computer's IP address. The server may also need to bind to an
appropriate network interface, and the UDP port must be allowed through the
firewall.

## Important note about UDP

UDP is connectionless and does not guarantee delivery, ordering, or duplicate
prevention. This example is intended for learning and local testing. Production
applications should add the reliability and validation behavior they require.

## Line-by-line explanation: `server.py`

| Line | Code | Explanation |
|---:|---|---|
| 1 | `import socket` | Imports Python's built-in networking module. |
| 4 | `HOST = "127.0.0.1"` | Sets the server IP address to the local computer. |
| 5 | `PORT = 12345` | Sets the UDP port on which the server listens. |
| 6 | `BUFFER_SIZE = 1024` | Sets the maximum number of bytes received at once. |
| 9 | `def run_server():` | Defines the function that runs the server. |
| 10 | `"""Receive datagrams and send a reply to each client."""` | Documents the function's purpose. |
| 11 | `with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:` | Creates an IPv4 UDP socket and closes it automatically. |
| 12 | `server_socket.setsockopt(...)` | Allows the server to reuse the address after restarting. |
| 13 | `server_socket.bind((HOST, PORT))` | Assigns the IP address and port to the socket. |
| 15 | `print(f"UDP server listening on {HOST}:{PORT}")` | Displays the server's listening address. |
| 16 | `print("Press Ctrl+C to stop the server.")` | Explains how to stop the server. |
| 18 | `try:` | Begins handling a keyboard interruption. |
| 19 | `while True:` | Keeps the server running continuously. |
| 20 | `data, client_address = server_socket.recvfrom(BUFFER_SIZE)` | Waits for a datagram and gets its data and sender address. |
| 21 | `message = data.decode("utf-8")` | Converts received bytes into UTF-8 text. |
| 22 | `print(f"Received from {client_address}: {message}")` | Displays the sender and received message. |
| 24 | `reply = f"Server received: {message}"` | Creates a response containing the received message. |
| 25 | `server_socket.sendto(...)` | Encodes and sends the response to the client. |
| 26 | `except KeyboardInterrupt:` | Catches `Ctrl+C` for a clean shutdown. |
| 27 | `print("\nServer stopped.")` | Displays a shutdown message. |
| 30 | `if __name__ == "__main__":` | Checks whether the file is being run directly. |
| 31 | `run_server()` | Calls the function and starts the server. |

Blank lines in the source file are intentionally omitted from this table.

## Line-by-line explanation: `client.py`

| Line | Code | Explanation |
|---:|---|---|
| 1 | `import socket` | Imports Python's built-in networking module. |
| 4 | `HOST = "127.0.0.1"` | Sets the server IP address. |
| 5 | `PORT = 12345` | Sets the server UDP port. |
| 6 | `BUFFER_SIZE = 1024` | Sets the maximum response size to receive. |
| 9 | `def run_client():` | Defines the function that runs the client. |
| 10 | `"""Send one datagram to the server and print its response."""` | Documents the function's purpose. |
| 11 | `message = input(...)` | Reads a message typed by the user. |
| 12 | `server_address = (HOST, PORT)` | Creates the server address tuple. |
| 14 | `with socket.socket(...) as client_socket:` | Creates an IPv4 UDP socket and closes it automatically. |
| 15 | `client_socket.settimeout(5)` | Waits up to five seconds for a response. |
| 16 | `print(f"Sending: {message}")` | Displays the message being sent. |
| 17 | `client_socket.sendto(...)` | Encodes and sends the message to the server. |
| 19 | `try:` | Begins handling a possible timeout. |
| 20 | `data, server_address = client_socket.recvfrom(BUFFER_SIZE)` | Waits for the server response and gets its address. |
| 21 | `except socket.timeout:` | Handles a response that does not arrive in time. |
| 22 | `print("No response...")` | Informs the user that no response was received. |
| 23 | `return` | Stops the client after a timeout. |
| 25 | `print(f"Received from server...")` | Decodes and displays the server response. |
| 28 | `if __name__ == "__main__":` | Checks whether the file is being run directly. |
| 29 | `run_client()` | Calls the function and starts the client. |

Blank lines in the source file are intentionally omitted from this table.

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

## License

No license has been specified for this repository yet. Add a license file if
you want others to reuse, modify, or distribute the code under defined terms.
