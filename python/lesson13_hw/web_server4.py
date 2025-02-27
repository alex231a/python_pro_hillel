"""Module with web-server code"""

import socket
import threading


def handle_client(client_socket)->None:
    """Function to handle a client"""
    request = client_socket.recv(1024).decode("utf-8")
    print("##########################################")
    print(f"[+] Received request:\n{request}")
    print("##########################################")

    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/plain\r\n\r\n"
    response += "Hello! This is multithreading web server!\r\n"

    client_socket.sendall(response.encode("utf-8"))
    client_socket.close()


def start_server(host="0.0.0.0", port=8080)->None:
    """Function to start the web server
    To check how to work web-server - just send HTTP GET request to:
    http://localhost:8080/
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("##########################################")
    print(f"[*] Server run on {host}:{port}")
    print("##########################################")

    while True:
        client_socket, addr = server.accept()
        print("##########################################")
        print(f"[+] New connection from {addr}")
        print("##########################################")
        client_handler = threading.Thread(target=handle_client,
                                          args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
