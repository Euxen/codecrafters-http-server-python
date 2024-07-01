import socket

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server is listening on localhost:4221")

    while True:
        client_socket, client_address = server_socket.accept()
        
        data = client_socket.recv(1024).decode("utf-8").split("\r\n")
        if not data:
            client_socket.close()
            continue

        path = data[0].split(" ")[1]
        
        useragent = " "
        for line in data[1:]:
            if line.startswith("User-Agent:"):
                user_agent = line.split("User-Agent:")[1].strip()
                break

        if path == "/":
            response = "HTTP/1.1 200 OK\r\n\r\n"
        elif path.startswith("/echo/"):
            content = path[6:]
            response = f"HTTP/1.1 200 OK\r\n"
            response += f"Content-Type: text/plain\r\n"
            response += f"Content-Length: {len(content)}\r\n"
            response += f"\r\n{content}"
        elif path == "/user-agent":
            response = f"HTTP/1.1 200 OK\r\n"
            response += f"Content-Type: text/plain\r\n"
            response += f"Content-Length: {len(user_agent)}\r\n"
            response += f"\r\n{user_agent}"
        else:
            response = "HTTP/1.1 404 Not Found\r\n\r\n"
        
        client_socket.sendall(response.encode("utf-8"))
        client_socket.close()

if __name__ == "__main__":
    main()