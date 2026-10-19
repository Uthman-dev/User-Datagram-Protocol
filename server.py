import socket


HOST = "127.0.0.1"
PORT = 12345
BUFFER_SIZE = 1024


def run_server():
    """Receive datagrams and send a reply to each client."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))

        print(f"UDP server listening on {HOST}:{PORT}")
        print("Press Ctrl+C to stop the server.")

        try:
            while True:
                data, client_address = server_socket.recvfrom(BUFFER_SIZE)
                message = data.decode("utf-8")
                print(f"Received from {client_address}: {message}")

                reply = f"Server received: {message}"
                server_socket.sendto(reply.encode("utf-8"), client_address)
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    run_server()