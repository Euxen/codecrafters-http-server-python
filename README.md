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

[![progress-banner](https://backend.codecrafters.io/progress/http-server/ae24dce3-dea4-434e-ae62-4e80179e077b)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This is a starting point for Python solutions to the
["Build Your Own HTTP server" Challenge](https://app.codecrafters.io/courses/http-server/overview).

[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is the
protocol that powers the web. In this challenge, you'll build a HTTP/1.1 server
that is capable of serving multiple clients.

Along the way you'll learn about TCP servers,
[HTTP request syntax](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html),
and more.

**Note**: If you're viewing this repo on GitHub, head over to
[codecrafters.io](https://codecrafters.io) to try the challenge.

# Passing the first stage

The entry point for your HTTP server implementation is in `app/main.py`. Study
and uncomment the relevant code, and push your changes to pass the first stage:

```sh
git add .
git commit -m "pass 1st stage" # any msg
git push origin master
```

Time to move on to the next stage!

# Stage 2 & beyond

Note: This section is for stages 2 and beyond.

1. Ensure you have `python (3.11)` installed locally
1. Run `./your_server.sh` to run your program, which is implemented in
   `app/main.py`.
1. Commit your changes and run `git push origin master` to submit your solution
   to CodeCrafters. Test output will be streamed to your terminal.

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
