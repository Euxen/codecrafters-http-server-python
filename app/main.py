import socket
import sys
import os
import gzip

def compress_data(data):
    compressed_data = gzip.compress(data)
    return compressed_data

def main():
    directory = sys.argv[2] if len(sys.argv) > 2 else "/tmp"
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print(f"Server is listening on localhost:4221, serving files from {directory}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        
        request = client_socket.recv(1024).decode("utf-8")
        request_lines = request.split("\r\n")
        if not request_lines:
            client_socket.close()
            continue
        
        method, path, _ = request_lines[0].split()
        
        headers = {}
        for line in request_lines[1:]:
            if ":" in line:
                key, value = line.split(":", 1)
                headers[key.strip().lower()] = value.strip()
        
        accept_encoding = headers.get('accept-encoding', '')
        supports_gzip = 'gzip' in accept_encoding

        if path.startswith("/files/"):
            _, filename = path.split("/files/", 1)
            file_path = os.path.join(directory, filename)
            
            if method == "POST":
                content_length = int(headers.get('content-length', 0))
                body = request.split("\r\n\r\n", 1)[1][:content_length]
                
                with open(file_path, "w") as f:
                    f.write(body)
                
                response = "HTTP/1.1 201 Created\r\n\r\n"
            
            elif method == "GET":
                try:
                    with open(file_path, "rb") as f:
                        content = f.read()
                    
                    response = f"HTTP/1.1 200 OK\r\n"
                    response += f"Content-Type: application/octet-stream\r\n"

                    #add gzip support

                    if supports_gzip and len(content) > 1000:
                        content = compress_data(content)
                        response += f"Content-Encoding: gzip\r\n"

                    response += f"Content-Length: {len(content)}\r\n"
                    response += f"\r\n"
                    response = response.encode("utf-8") + content
                    
                except FileNotFoundError:
                    response = "HTTP/1.1 404 Not Found\r\n\r\n"
        
        elif path == "/":
            response = "HTTP/1.1 200 OK\r\n\r\n"
        elif path.startswith("/echo/"):
            content = path[6:]
            response = f"HTTP/1.1 200 OK\r\n"
            response += f"Content-Type: text/plain\r\n"
            response += f"Content-Length: {len(content)}\r\n"
            response += f"\r\n{content}"
        elif path == "/user-agent":
            user_agent = headers.get('user-agent', '')
            response = f"HTTP/1.1 200 OK\r\n"
            response += f"Content-Type: text/plain\r\n"
            response += f"Content-Length: {len(user_agent)}\r\n"
            response += f"\r\n{user_agent}"
        else:
            response = "HTTP/1.1 404 Not Found\r\n\r\n"
        
        if isinstance(response, str):
            response = response.encode("utf-8")
        client_socket.sendall(response)
        client_socket.close()

if __name__ == "__main__":
    main()