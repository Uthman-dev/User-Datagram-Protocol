import socket


HOST = "127.0.0.1"
PORT = 12345
BUFFER_SIZE = 1024


def run_client():
    """Send one datagram to the server and print its response."""
    message = input("Enter a message for the server: ")
    server_address = (HOST, PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.settimeout(5)
        print(f"Sending: {message}")
        client_socket.sendto(message.encode("utf-8"), server_address)

        try:
            data, server_address = client_socket.recvfrom(BUFFER_SIZE)
        except socket.timeout:
            print("No response received within 5 seconds.")
            return

        print(f"Received from server {server_address}: {data.decode('utf-8')}")


if __name__ == "__main__":
    run_client()