import socket
import threading

def udp_server(host='0.0.0.0', port=12345):
    """
    Starts a UDP server that listens for messages and sends back the same message (echo).
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Server started on {host}:{port}")

    while True:
        data, addr = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received message from {addr}: {data.decode()}")
        server_socket.sendto(data, addr)  # Echo the received data back to the sender

def udp_client(server_ip='127.0.0.1', server_port=12345, message="Hello, Server!"):
    """
    Sends a message to the UDP server and receives the echoed response.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (server_ip, server_port)

    try:
        # Send message to the server
        print(f"Sending message to {server_ip}:{server_port}")
        client_socket.sendto(message.encode(), server_address)

        # Receive echo response from the server
        data, _ = client_socket.recvfrom(1024)
        print(f"Received echo: {data.decode()}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    # Start the server in a separate thread
    server_thread = threading.Thread(target=udp_server, args=('0.0.0.0', 12345), daemon=True)
    server_thread.start()

    # Allow the server to initialize
    import time
    time.sleep(1)

    # Act as a client and send data
    udp_client(message="Test Message from Client")