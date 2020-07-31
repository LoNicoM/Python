# I am writing this program to get an understanding of how a hash function works,
# most of this comes from wikipedia and got some hints from stack exchange
# IMPORTS
import tkinter as tk
# CONSTANTS

s = [[7, 12, 17, 22], [5, 9, 14, 20], [4, 11, 16, 23], [6, 10, 15, 21]]  # bit shift amounts

k = [3614090360, 3905402710, 606105819, 3250441966, 4118548399,  # I pre calculated these
     1200080426, 2821735955, 4249261313, 1770035416, 2336552879,  # using a list so i don't
     4294925233, 2304563134, 1804603682, 4254626195, 2792965006,  # have to import the math module
     1236535329, 4129170786, 3225465664, 643717713, 3921069994,
     3593408605, 38016083, 3634488961, 3889429448, 568446438,
     3275163606, 4107603335, 1163531501, 2850285829, 4243563512,
     1735328473, 2368359562, 4294588738, 2272392833, 1839030562,
     4259657740, 2763975236, 1272893353, 4139469664, 3200236656,
     681279174, 3936430074, 3572445317, 76029189, 3654602809,
     3873151461, 530742520, 3299628645, 4096336452, 1126891415,
     2878612391, 4237533241, 1700485571, 2399980690, 4293915773,
     2240044497, 1873313359, 4264355552, 2734768916, 1309151649,
     4149444226, 3174756917, 718787259, 3951481745]

# FUNCTIONS


def swap_end(x):
    return (((x << 24) & 4278190080) | ((x << 8) & 16711680) |
            ((x >> 8) & 65280) | ((x >> 24) & 255))  # doesnt require any imports


def str2bin(x):
    return "".join([f"{i:08b}" for i in [ord(j2) for j2 in x]])  # string to bin string


def prep_message(msg):
    print(msg)
    result = str2bin(msg) + "1"  # create the variable and append a 1
    length = f"{len(result) - 1:064b}"  # get length in bits
    while len(result) % 512 != 448:
        result += "0"  # pad until modulo 512 == 448
    result = [result[i:i + 512] for i in range(0, len(result), 512)]  # split into 16 word blocks
    result = [[swap_end(int(j[i:i+32], 2)) for i in range(0, len(j), 32)] for j in result]  # split those into words
    result[-1].extend([int(length[33:], 2), int(length[:33], 2)])  # extend the length values
    print(result)
    return result


def rot_left(x, n):
    return int(f"{x:032b}"[n:] + f"{x:032b}"[:n], 2)


def mod_add(a, b):
    return (a + b) % (2 ** 32)


def md5_sum(message):

    message = prep_message(message)
    a0, b0, c0, d0 = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476

    for item in range(len(message)):
        a, b, c, d = a0, b0, c0, d0
        for i in range(64):
            if i < 16:
                f = (b & c) | (~b & d)
                g = i
                rnd = 0
            elif 15 < i < 32:
                f = (d & b) | (c & ~d)
                g = (5 * i + 1) % 16
                rnd = 1
            elif 31 < i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
                rnd = 2
            else:
                f = c ^ (b | ~d)
                g = (7 * i) % 16
                rnd = 3

            f = mod_add(rot_left(mod_add(mod_add(mod_add
                        (f, a), (k[i])), message[item][g]), s[rnd][i % 4]), b)

            a, d, c, b = d, c, b, f

        a0, b0, c0, d0 = mod_add(a0, a), mod_add(b0, b), mod_add(c0, c), mod_add(d0, d)

    return f"{swap_end(a0):08x}{swap_end(b0):08x}{swap_end(c0):08x}{swap_end(d0):08x}"

# GUI STUFF


def but_hash_click():
    txt_output.delete("0.0", tk.END)
    string_in = txt_string.get("0.3", tk.END)[:-1]
    txt_output.insert("0.0", md5_sum(string_in))


def but_clear_click():
    txt_output.delete("0.0", tk.END)
    txt_string.delete("0.0", tk.END)


# MAIN WINDOW
window = tk.Tk()
window.title("md5_Sum by LeonM")
window.iconbitmap('icon.ico')
window.resizable(True, False)
# FRAMES
frm_1 = tk.Frame()
frm_2 = tk.Frame()
frm_3 = tk.Frame()
# INPUT / OUTPUT BOXES
lbl_string = tk.Label(master=frm_1, text="Input:", width=10)
txt_string = tk.Text(master=frm_1, height=10)

lbl_output = tk.Label(master=frm_2, text="MD5:", width=10)
txt_output = tk.Text(master=frm_2, height=10)
# BUTTONS
but_encode = tk.Button(master=frm_3, text="Hash", width=8, height=1, command=but_hash_click)
but_decode = tk.Button(master=frm_3, text="Clear", width=8, height=1, command=but_clear_click)

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
