# Simple HTTP Server

A lightweight HTTP server implemented in Python with file serving capabilities, echo functionality, and gzip compression support.

## Features

- Custom routing for various endpoints
- File upload and retrieval
- Echo functionality
- User-agent information endpoint
- Gzip compression for larger responses and echo content
- Configurable serving directory

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-http-server.git
   cd simple-http-server
   ```

2. No additional dependencies are required as the server uses Python's standard library.

### Usage

Run the server with:

```
python server.py [port] [directory]
```

- `port` (optional): The port number to run the server on. Default is 4221.
- `directory` (optional): The directory to serve files from. Default is "/tmp".

Example:
```
python server.py 8080 /home/user/files
```

## Endpoints

- `/`: Returns a 200 OK response.
- `/echo/<message>`: Echoes back the message in the URL path.
- `/user-agent`: Returns the User-Agent header from the request.
- `/files/<filename>`: 
  - GET: Retrieve a file from the serving directory.
  - POST: Upload a file to the serving directory.

## Gzip Compression

The server supports gzip compression for:
- File responses larger than 1000 bytes
- Echo responses when the client supports gzip encoding

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
