"""
Some lines are commented out.
You may or may not want to use the ipaddress library
but you will still need to check for a valid IPv4 adddress.

The 'with open('JSONdata') as f:' line will read the data file
AS LONG AS IT IS IN THE SAME DIRECTORY :)

The next line should get you started with a method you will need
from the json library to change the JSON text into something 
you can call from Python
"""

import json
import ipaddress

with open('JSONdata') as f:
    data = json.load(f)

for each in data:
    address = each['lanIp']
    serial = each['serial']

    try:
        ipaddress.IPv4Address(address)
        print(address, 'is a valid IP for serial:', serial)
    except ValueError:
        print(address, 'is an invalid IP for serial:', serial)