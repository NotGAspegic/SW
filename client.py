# import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

# main function
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    try:
        client.connect((HOST,PORT))
        print("Successfully connected to server")
    except:
        print(f"Unable to connect to server {HOST}{PORT}")
    
if __name__ == '__main__':
    main()