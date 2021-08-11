#!/bin/env python3

from bs4 import BeautifulSoup
import requests
import argparse

banner = """\
             _            _                                
            | |          | |                               
  ___  _ __ | |_     ___ | |__    ___   __ _  _ __   _ __  
 / __|| '__|| __|   / __|| '_ \  / __| / _` || '_ \ | '_ \ 
| (__ | |   | |_  _ \__ \| | | || (__ | (_| || | | || | | |
 \___||_|    \__|(_)|___/|_| |_| \___| \__,_||_| |_||_| |_|
                                                          
"""

class CertShcann:
    def __init__(self, args) -> None:
        self.args = args
        self.html = self.get_certs(self.args.domain)
        self.results = self.parse_html()
        self.print_results()
        if self.args.o:
            self.save_to_file(self.args.o)

    def get_certs(self, domain):
        print("[*] Connecting, please wait.")
        req = requests.get(f"http://crt.sh/?q={domain}")
        return req.text
    
    def parse_html(self):
        domains = []
        soup = BeautifulSoup(self.html, "html.parser")
        for row in soup.find_all("tr")[2:]:
            keys = row.find_all_next("td")[4]
            if args.r and "*" in keys.text:
                pass
            else:
                domains.append(keys.text)
        domains = list(set(domains))  # Remove Duplicates 
        return domains

    def print_results(self):
        print("\n")
        for result in self.results:
            print(result)

    def save_to_file(self, file_name):
        with open(file_name, "wt") as out_file:
            for result in self.results:
                out_file.write(result + "\n")

print(banner)
parser = argparse.ArgumentParser()
parser.add_argument("domain", help="The domain you wish to scan")
parser.add_argument("-r", action="store_true", help="Remove wildcards")
parser.add_argument("-o", metavar="filename", help="Output to file")
args = parser.parse_args()

scan = CertShcann(args)


