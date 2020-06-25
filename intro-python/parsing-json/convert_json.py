

import json
from pprint import pprint

interfaces = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet2",
        "description": "Wide Area Network",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.0.2",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

x = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet2",
        "description": "Wide Area Network",
        "enabled": "true",
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.0.2",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

interfaces_text = str(x)
print("Interfaces es ", type(interfaces_text))
#print(interfaces)
print(interfaces_text)
print("/n") 
print(json.loads(interfaces_text))
#print("Interfaces es ", type(interfaces_json))