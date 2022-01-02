# Simple IP discloser for URL by Sean Lewis
# Uses Python's socket library

import socket
host = socket.gethostname()
ip = socket.gethostbyname(host)
print("Personal Host Name is:", host)
print("Personal IP Address is:", ip)
url = "github.com"
while url != "":
    url = input("Enter the website address: ")
    try:
        print(f"The IP address of {url} is: {socket.gethostbyname(url)}")
    except:
        print("Please enter a valid URL address")