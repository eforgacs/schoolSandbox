from socket import socket, AF_INET, SOCK_DGRAM

# Create socket
server_name = "127.0.0.1"
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
# Send to the server
client_socket.sendto(message.encode(), (server_name, server_port))
# Receiver response back
try:
    modified_message, server_address = client_socket.recvfrom(2048)
    print("ENOUGH")
except socket.timeout:
    print("ENOUGH")
print(modified_message.decode())
# Close the socket
client_socket.close()
