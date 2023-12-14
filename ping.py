# ping.py

# Core functions reside here.

from http.client import HTTPConnection  
from urllib.parse import urlparse

def getStatus(url):
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    port = [80,443]
    conn = HTTPConnection(host=host,port=443,timeout=5)
    conn.request("HEAD", "/")

    response = conn.getresponse()
    responseMessage = [response.status, response.reason]

    return responseMessage

input = "www.reddit.com"
print(getStatus(input))
