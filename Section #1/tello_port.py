import socket
import time

# Tello IP and port
TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
LOCAL_PORT = 9000

# Initialize a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', LOCAL_PORT))

def send_command(command):
    try:
        sock.sendto(command.encode('utf-8'), (TELLO_IP, TELLO_PORT))
        print(f"Sent command: {command}")

        # Receive response from Tello
        response, _ = sock.recvfrom(1024)
