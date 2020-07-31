# I am writing this program to get an understanding of how a hash funtion works

# CONSTANTS

s = [[7, 12, 17, 22],[5, 9, 14, 20],[4, 11, 16, 23],[6, 10, 15, 21]]

k = [3614090360, 3905402710, 606105819, 3250441966, 4118548399,
     1200080426, 2821735955, 4249261313, 1770035416, 2336552879,
     4294925233, 2304563134, 1804603682, 4254626195, 2792965006,
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

def swap_end(input):
    return (((input << 24) & 0xFF000000) |
            ((input << 8) & 0x00FF0000) |
            ((input >> 8) & 0x0000FF00) |
            ((input >> 24) & 0x000000FF))

def prep_message(msg):
    str2bin = lambda x: "".join([f"{i:08b}" for i in [ord(j2) for j2 in x]])
    result = str2bin(msg) + "1"
    while len(result) % 512 != 448: result += "0"
    result += f"{swap_end((len(msg) * 8) % (2 ** 64)):064b}"
    result = [result[i:i + 512] for i in range(0, len(result), 512)]
    result = [[swap_end(int(j[i:i+32],2)) for i in range(0, len(j), 32)] for j in result]
    result[-1].append(result[-1][-2]) # swap the end words
    result[-1].pop(-3) # theres probably a better way to do this
    return result

def rot_left(x, n):
    return int(f"{x:032b}"[n:] + f"{x:032b}"[:n], 2)

def mod_add(a, b):
    return (a + b) % (2 ** 32)

def compute_sum(message):

    mesg_32b = prep_message(message)
    a0, b0, c0, d0 = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476

    for item in range(len(mesg_32b)):
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
            f = mod_add(f, mesg_32b[item][g])
            f = mod_add(f, (k[i]))
            f = mod_add(f, a)
            f = rot_left(f, s[rnd][i % 4])
            f = mod_add(f, b)

            a, d, c, b = d, c, b, f

        a0, b0, c0, d0 = mod_add(a0, a), mod_add(b0, b), mod_add(c0, c), mod_add(d0, d)

    return f"{swap_end(a0):08x}{swap_end(b0):08x}{swap_end(c0):08x}{swap_end(d0):08x}"




# DEBUG / TESTING

print(compute_sum("The quick brown fox jumps over the lazy dog."))
print("e4d909c290d0fb1ca068ffaddf22cbd0")




