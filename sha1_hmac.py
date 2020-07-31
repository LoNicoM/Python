import tkinter as tk
from hashlib import sha1
import hmac
# FUNCTIONS
def sha1_hmac_url(string, key):
    hash = hmac.new(bytearray(key, "utf-8"), bytearray(string, "utf-8"), sha1)
    return "".join(format(x, '02x').lower() for x in hash.digest())

def but_go_click():
    txt_output.delete("0.0", tk.END)
    string_in, key_in = txt_string.get("0.0", tk.END).strip("\n"), txt_key.get("0.0", tk.END).strip("\n")
    if string_in and key_in:
        txt_output.insert("0.0", sha1_hmac_url(string_in,key_in))
    else:
        txt_output.insert("0.0", "Invalid Input.")

def but_clear_click():
    txt_string.delete("0.0", tk.END)
    txt_key.delete("0.0", tk.END)
    txt_output.delete("0.0", tk.END)
# MAIN WINDOW
window = tk.Tk()
window.title("SHA1 HMAC Hasher")
# FRAMES
frm_1 = tk.Frame()
frm_2 = tk.Frame()
frm_3 = tk.Frame()
frm_4 = tk.Frame()
# INPUT / OUTPUT BOXES
lbl_string =  tk.Label(master=frm_1, text="String to hash:", width=20)
txt_string = tk.Text(master=frm_1, height=10)

lbl_key =  tk.Label(master=frm_2, text="Key in UTF-8:", width=20)
txt_key = tk.Text(master=frm_2, height=3)

lbl_output =  tk.Label(master=frm_3, text="Output:", width=20)
txt_output = tk.Text(master=frm_3, height=10)
# BUTTONS
but_clear = tk.Button(master=frm_4, text="Clear", width=8, height=1, command=but_clear_click)
but_go = tk.Button(master=frm_4, text="Go!", width=8, height=1, command=but_go_click)

# PACKING
lbl_string.pack(side=tk.LEFT)
txt_string.pack(fill=tk.BOTH)

lbl_key.pack(side=tk.LEFT)
txt_key.pack(fill=tk.BOTH)

lbl_output.pack(side=tk.LEFT)
txt_output.pack(fill=tk.BOTH)

but_clear.pack(side=tk.LEFT)
but_go.pack(side=tk.LEFT)

frm_1.pack(fill=tk.X)
frm_2.pack(fill=tk.X)
frm_3.pack(fill=tk.X)
frm_4.pack(side=tk.RIGHT)

window.mainloop()

