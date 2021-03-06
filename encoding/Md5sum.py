# I am writing this program to get an understanding of how a hash function works,
# most of this comes from wikipedia and got some hints from stack exchange
# IMPORTS
import tkinter as tk
# CONSTANTS


class Md5Sum:
    def __init__(self):

        """ Calculate the MD5 Sum of the given."""
        self.message = ""

        self.__s = [[7, 12, 17, 22], [5, 9, 14, 20], [4, 11, 16, 23], [6, 10, 15, 21]]  # bit shift amounts

        self.__k = [3614090360, 3905402710, 606105819, 3250441966, 4118548399, 1200080426,
                    2821735955, 4249261313, 1770035416, 2336552879, 4294925233, 2304563134,
                    1804603682, 4254626195, 2792965006, 1236535329, 4129170786, 3225465664,
                    643717713, 3921069994, 3593408605, 38016083, 3634488961, 3889429448,
                    568446438, 3275163606, 4107603335, 1163531501, 2850285829, 4243563512,
                    1735328473, 2368359562, 4294588738, 2272392833, 1839030562, 4259657740,
                    2763975236, 1272893353, 4139469664, 3200236656, 681279174, 3936430074,
                    3572445317, 76029189, 3654602809, 3873151461, 530742520, 3299628645,
                    4096336452, 1126891415, 2878612391, 4237533241, 1700485571, 2399980690,
                    4293915773, 2240044497, 1873313359, 4264355552, 2734768916, 1309151649,
                    4149444226, 3174756917, 718787259, 3951481745]  # precalculated sin constants

    def set_message(self, input):
        self.message = input

    def digest(self):

        def prep_message(msg):
            result = list(bytearray(msg, "utf-8"))  # make a byte array
            length = int.to_bytes(len(result) * 8, 8, "big")  # get length in bits
            result.append(128)  # append a 10000000
            result = [int.from_bytes(result[j:j + 4], "little") for j in range(0, len(result), 4)]
            while len(result) % 16 != 14:  # pad bytes
                result.append(0)
            result.extend([int.from_bytes(length[4:], "big"), int.from_bytes(length[:4], "big")])
            result = [result[j:j + 16] for j in range(0, len(result), 16)]

            return result

        def swap_end(x):
            return (((x << 24) & 4278190080) | ((x << 8) & 16711680) |
                    ((x >> 8) & 65280) | ((x >> 24) & 255))  # doesnt require any imports

        def add32(x, y):
            return (x + y) % 4294967296  # modulo 32 bits

        def rot_left(x, n):
            return (x << n) | (x >> (32 - n))

        message = prep_message(self.message)
        a0, b0, c0, d0 = 1732584193, 4023233417, 2562383102, 271733878  # initialize the values

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

                f = add32(rot_left(add32(add32(add32(f, a),
                                               (self.__k[i])), message[item][g]), self.__s[rnd][i % 4]), b)

                a, d, c, b = d, c, b, f

            a0, b0, c0, d0 = add32(a0, a), add32(b0, b), add32(c0, c), add32(d0, d)

        return f"{swap_end(a0):08x}{swap_end(b0):08x}" \
               f"{swap_end(c0):08x}{swap_end(d0):08x}"

# GUI STUFF

md5 = Md5Sum()

def but_hash_click():
    ent_output.delete(0, tk.END)
    string_in = txt_string.get("0.3", tk.END)[:-1]
    md5.set_message(string_in)
    ent_output.insert(0, md5.digest())


def but_clear_click():
    ent_output.delete(0, tk.END)
    txt_string.delete("0.0", tk.END)


# MAIN WINDOW
window = tk.Tk()
window.title("md5_Sum by LeonM")
window.iconbitmap("icon.ico")
window.minsize(470, 230)
# FRAMES
frm_1 = tk.Frame()
frm_2 = tk.Frame()
# INPUT / OUTPUT BOXES
lbl_string = tk.Label(master=frm_1, text="Input:", width=10)
txt_string = tk.Text(master=frm_1, height=10)

lbl_output = tk.Label(master=frm_2, text="MD5:", width=10)
ent_output = tk.Entry(master=frm_2, width=35)
# BUTTONS
but_encode = tk.Button(master=frm_2, text="Hash", width=8, height=1, command=but_hash_click)
but_decode = tk.Button(master=frm_2, text="Clear", width=8, height=1, command=but_clear_click)

# PACKING

lbl_string.pack(side=tk.LEFT)
txt_string.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill="both")

lbl_output.pack(side=tk.LEFT)
ent_output.pack(side=tk.LEFT, padx=10, pady=10)

but_encode.pack(side=tk.LEFT, padx=5)
but_decode.pack(side=tk.LEFT, padx=5)

frm_1.pack(fill="both", expand=True)
frm_2.pack(fill=tk.X, expand=False)

window.mainloop()
