#!/usr/bin/python3

import socket
import argparse

args = argparse.ArgumentParser()
args.add_argument("ip", help="The IP to FUZZ!")
args.add_argument("port", help="The port to FUZZ!", type=int)
args = args.parse_args()

buf = b"X" * 100

try:
    for i in range(1,101):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((args.ip, args.port))
        print(sock.recv(1024).decode())
        print(f"Sending {100 * i} bytes.")
        sock.send(buf * i)
        print(sock.recv(1024))
        sock.close
except Exception as error:
    print("It's dead Jim!")
    print(error)