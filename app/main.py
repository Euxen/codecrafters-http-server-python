import socket


def main():
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept()[0].sendall(b"HTTP/1.1 200 OK\r\n\r\n") # respond with a 200 OK response


if __name__ == "__main__":
    main()
