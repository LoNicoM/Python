# just writing a program to test my understanding of base64
import tkinter as tk

def base64_decode(input):
    b64decmap = {
        "A": "000000", "Q": "010000", "g": "100000", "w": "110000",
        "B": "000001", "R": "010001", "h": "100001", "x": "110001",
        "C": "000010", "S": "010010", "i": "100010", "y": "110010",
        "D": "000011", "T": "010011", "j": "100011", "z": "110011",
        "E": "000100", "U": "010100", "k": "100100", "0": "110100",
        "F": "000101", "V": "010101", "l": "100101", "1": "110101",
        "G": "000110", "W": "010110", "m": "100110", "2": "110110",
        "H": "000111", "X": "010111", "n": "100111", "3": "110111",
        "I": "001000", "Y": "011000", "o": "101000", "4": "111000",
        "J": "001001", "Z": "011001", "p": "101001", "5": "111001",
        "K": "001010", "a": "011010", "q": "101010", "6": "111010",
        "L": "001011", "b": "011011", "r": "101011", "7": "111011",
        "M": "001100", "c": "011100", "s": "101100", "8": "111100",
        "N": "001101", "d": "011101", "t": "101101", "9": "111101",
        "O": "001110", "e": "011110", "u": "101110", '+': "111110",
        "P": "001111", "f": "011111", "v": "101111", "/": "111111"
    }
    binary, string, padding = "", "", input[-2].count("=")
    input = input.strip("=")
    for i in input:
        binary += b64decmap[i]
    if padding == 1: binary = binary[:-2]
    elif padding == 2: binary = binary[:-4]
    binary = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    for j in binary:
        string += chr(int(j, 2))
    return string


def base64_encode(input,pad = 1):
    b64encmap = {
        "000000": "A", "010000": "Q", "100000": "g", "110000": "w",
        "000001": "B", "010001": "R", "100001": "h", "110001": "x",
        "000010": "C", "010010": "S", "100010": "i", "110010": "y",
        "000011": "D", "010011": "T", "100011": "j", "110011": "z",
        "000100": "E", "010100": "U", "100100": "k", "110100": "0",
        "000101": "F", "010101": "V", "100101": "l", "110101": "1",
        "000110": "G", "010110": "W", "100110": "m", "110110": "2",
        "000111": "H", "010111": "X", "100111": "n", "110111": "3",
        "001000": "I", "011000": "Y", "101000": "o", "111000": "4",
        "001001": "J", "011001": "Z", "101001": "p", "111001": "5",
        "001010": "K", "011010": "a", "101010": "q", "111010": "6",
        "001011": "L", "011011": "b", "101011": "r", "111011": "7",
        "001100": "M", "011100": "c", "101100": "s", "111100": "8",
        "001101": "N", "011101": "d", "101101": "t", "111101": "9",
        "001110": "O", "011110": "e", "101110": "u", "111110": '+',
        "001111": "P", "011111": "f", "101111": "v", "111111": "/"
    }
    decimal, binary, base64, padding = [], "", "", ""
    for i in input: decimal.append(ord(i))
    for j in decimal: binary += f"{j:08b}"
    binary = [binary[i:i+6] for i in range(0, len(binary), 6)]
    if len(binary[-1]) != 6:
        padding = "=" if len(binary[-1]) == 4 else "=="
        binary[-1] += "00" if padding == "=" else "0000"
    for k in binary: base64 += b64encmap[k]
    return base64 + padding if pad else base64

def but_encode_click():
    txt_output.delete("0.0", tk.END)
    string_in = txt_string.get("0.0", tk.END).strip("\n")
    if string_in:
        txt_output.insert("0.0", base64_encode(string_in))
    else:
        txt_output.insert("0.0", "Invalid Input.")

def but_decode_click():
    txt_output.delete("0.0", tk.END)
    string_in = txt_string.get("0.0", tk.END).strip("\n")
    if string_in:
        try:
            txt_output.insert("0.0", base64_decode(string_in))
        except KeyError:
            txt_output.insert("0.0", "Invalid Input.")
    else:
        txt_output.insert("0.0", "Invalid Input.")

# MAIN WINDOW
window = tk.Tk()
window.title("Base64 Encoder / Decoder by LeonM")
window.iconbitmap('icon.ico')
# FRAMES
frm_1 = tk.Frame()
frm_2 = tk.Frame()
frm_3 = tk.Frame()
# INPUT / OUTPUT BOXES
lbl_string =  tk.Label(master=frm_1, text="Input:", width=10)
txt_string = tk.Text(master=frm_1, height=10)

lbl_output =  tk.Label(master=frm_2, text="Output:", width=10)
txt_output = tk.Text(master=frm_2, height=10)
# BUTTONS
but_encode = tk.Button(master=frm_3, text="Encode", width=8, height=1, command=but_encode_click)
but_decode = tk.Button(master=frm_3, text="Decode", width=8, height=1, command=but_decode_click)

# PACKING
lbl_string.pack(side=tk.LEFT)
txt_string.pack(fill=tk.BOTH)

lbl_output.pack(side=tk.LEFT)
txt_output.pack(fill=tk.BOTH)

but_encode.pack(side=tk.LEFT)
but_decode.pack(side=tk.LEFT)

frm_1.pack(fill=tk.X)
frm_2.pack(fill=tk.X)
frm_3.pack(side=tk.RIGHT)

window.mainloop()
