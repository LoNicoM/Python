# ipV4 Calculator, by LeonM

class Ipv4Calc:
    """ Calculates the ipv4, Network, hosts, broadcast address etc"""
    def __init__(self):
        self.ip_address = 0
        self.subnet_mask = 0
        self.network_id = 0
        self.broadcast = 0
        self.first_host = 0
        self.last_host = 0

    def set_ip_address(self, x):  # TODO used for GUI
        self.ip_address = x

    def set_subnet_mask(self, x):  # TODO used for GUI
        self.subnet_mask = x

    def set_network_id(self):
        self.network_id = self.ip_address & self.subnet_mask

    def set_first_host(self):
        self.first_host = self.network_id + 1

    def set_last_host(self):
        self.last_host = self.network_id + (0xffffffff ^ self.subnet_mask) - 1

    def set_broadcast(self):
        self.broadcast = self.network_id + (0xffffffff ^ self.subnet_mask)

    def get_ip(self, d=0):
        data = list(int.to_bytes(self.ip_address, 4, "big"))
        if d == 1:
            return f"{data[0]}.{data[1]}.{data[2]}.{data[3]}"

        if d == 2:
            return f"{data[0]:08b}.{data[1]:08b}.{data[2]:08b}.{data[3]:08b}"

        else:
            return self.ip_address

    def get_subnet(self, d=0):
        data = list(int.to_bytes(self.subnet_mask, 4, "big"))
        if d == 1:
            return f"{data[0]}.{data[1]}.{data[2]}.{data[3]}"

        if d == 2:
            return f"{data[0]:08b}.{data[1]:08b}.{data[2]:08b}.{data[3]:08b}"

        if d == 3:
            return f"{self.subnet_mask:032b}".count("1")  # fix when i work out a better way

        else:
            return self.subnet_mask

    def get_network(self, d=0):
        self.set_network_id()  # update if called
        data = list(int.to_bytes(self.network_id, 4, "big"))
        if d == 1:  # Decimal output
            return f"{data[0]}.{data[1]}.{data[2]}.{data[3]}"

        if d == 2:  # Binary output
            return f"{data[0]:08b}.{data[1]:08b}.{data[2]:08b}.{data[3]:08b}"

        else:  # default, list output.
            return self.network_id

    def get_first_host(self, d=0):
        self.set_first_host()  # update if called
        data = list(int.to_bytes(self.first_host, 4, "big"))
        if d == 1:  # Decimal output
            return f"{data[0]}.{data[1]}.{data[2]}.{data[3]}"

        if d == 2:  # Binary output
            return f"{data[0]:08b}.{data[1]:08b}.{data[2]:08b}.{data[3]:08b}"

        else:  # default, list output.
            return data

    def get_last_host(self, d=0):
        self.set_last_host()  # update if called
        data = list(int.to_bytes(self.last_host, 4, "big"))
        if d == 1:  # Decimal output
            return f"{data[0]}.{data[1]}.{data[2]}.{data[3]}"

        if d == 2:  # Binary output
            return f"{data[0]:08b}.{data[1]:08b}.{data[2]:08b}.{data[3]:08b}"

        else:  # default, list output.
            return data

    def get_broadcast(self, d=0):
        self.set_broadcast()  # update if called
        data = list(int.to_bytes(self.broadcast, 4, "big"))
        if d == 1:  # Decimal output
            return f"{data[0]}.{data[1]}.{data[2]}.{data[3]}"

        if d == 2:  # Binary output
            return f"{data[0]:08b}.{data[1]:08b}.{data[2]:08b}.{data[3]:08b}"

        else:  # default, list output.
            return data

    def console_input(self):
        valid_subs = {255, 254, 252, 248, 240, 224, 192, 128, 0}

        def str_2_int(ip_list, sub=0):
            for i in range(4):
                ip_list[i] = int(ip_list[i])  # convert strings to integers
                if sub and ip_list[i] not in valid_subs:
                    raise ValueError
            return ip_list

        while True:  # loop until valid input is provided.
            print("Enter IP address  ", end="")
            try:
                user_input = input("-->:").split(".")  # get console input
                if len(user_input) != 4 or type(user_input) != list:  # catch invalid input
                    raise ValueError
                user_input = str_2_int(user_input)
                if 0 < max(user_input) > 254:  # catches not numerical as ValueError, nice!
                    raise ValueError
            except ValueError:  # ask the user to try again
                print(f"Invalid, ", end="")
                continue

            self.ip_address = int.from_bytes(user_input, "big")  # store input as integer.
            break

        while True:
            print("Enter Subnet Mask ", end="")
            try:
                user_input = input("-->:")  # get console input
                if user_input.find(".") == -1 and user_input.isdigit():
                    user_input = int(user_input)
                    if 0 < user_input < 32:
                        self.subnet_mask = 2**32 - 2**(32 - user_input)
                        break
                else:
                    user_input = user_input.split(".")
                    if len(user_input) != 4:
                        raise ValueError
                    else:
                        user_input = str_2_int(user_input, 1)
                        self.subnet_mask = int.from_bytes(user_input, "big")
                        if f"{self.subnet_mask:032b}".strip("0").count("0") != 0: # check for contiguous 1's
                            raise ValueError
                        break
            except ValueError:
                print(f"Invalid, ", end="")
                continue

    def console_print(self):
        print(f"""\
        ╔════════════════╤═════════════════╤═════════════════════════════════════╗
        ║                │     DECIMAL     │               BINARY                ║
        ╠════════════════╪═════════════════╪═════════════════════════════════════╣
        ║ IPv4 Address:  │ {self.get_ip(d=1):^15} │ {self.get_ip(d=2)} ║
        ║ Subnet Mask:   │ {self.get_subnet(d=1):^15} │ {self.get_subnet(d=2)} ║
        ║ Mask bits:     │ {self.get_subnet(d=3):^15} │                                     ║
        ║ Network ID:    │ {self.get_network(d=1):^15} │ {self.get_network(d=2)} ║
        ║ First Host:    │ {self.get_first_host(d=1):^15} │ {self.get_first_host(d=2)} ║
        ║ Last Host:     │ {self.get_last_host(d=1):^15} │ {self.get_last_host(d=2)} ║
        ║ Broadcast Add: │ {self.get_broadcast(d=1):^15} │ {self.get_broadcast(d=2)} ║
        ║ Max Hosts:     │ {self.last_host - self.first_host + 1:^15} │                                     ║
        ╚════════════════╧═════════════════╧═════════════════════════════════════╝
        """)

    def __and__(self, x, y):
        return x & y

    def __add__(self, x, y):
        return x + y


ip_bits = Ipv4Calc()
ip_bits.console_input()
ip_bits.console_print()
