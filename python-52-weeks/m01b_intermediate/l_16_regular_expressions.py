from random import choice
import re

# Sample MAC addresses
# 00:00:00:00:00:00
# 00-00-00-00-00-00
# 000000.000000
REGEX_MAC = r"^([0-9A-Fa-f]{2}[:-]?){5}([0-9A-Fa-f]{2})$|^[0-9A-Fa-f]{6}\.[0-9A-Fa-f]{6}$"

# IPv4 IP address
# 0.0.0.0 - 255.255.255.255       # IPv4 address space
# 10.0.0.0 - 10.255.255.255       # Private Address Space
# 172.16.0.0 - 172.31.255.255     # Private Address Space
# 192.168.0.0 - 192.168.255.255   # Private Address Space
#
# IANA IPv4 Address Space Registry
# https://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xhtml

REGEX_IP = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

REGEX_HOSTNAME = r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"
REGEX_EMAIL = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

MAC_ADDRESS = "mac address"
IP_ADDRESS = "ip address"
HOSTNAME = "hostname"
EMAIL = "email"

VALIDATION_LIST = [MAC_ADDRESS, IP_ADDRESS, HOSTNAME, EMAIL]
VALIDATION_PATTERN = {
    MAC_ADDRESS: REGEX_MAC,
    IP_ADDRESS: REGEX_IP,
    HOSTNAME: REGEX_HOSTNAME,
    EMAIL: REGEX_EMAIL
}

def rude_remark():
    return choice(["No way, Jose", "Give me a break, Jake", "Nice try, McFly"])


for validation_type in VALIDATION_LIST:

    print(f"\n----- {validation_type} verification --------------------")
    while True:

        input_to_validate = input(f"Enter {validation_type} or <cr> to quit:  ")
        if not input_to_validate:
            break

        match = re.search(VALIDATION_PATTERN[validation_type], input_to_validate.strip())
        if match is not None:
            print(f"---> valid {validation_type}: {match.group(0)} at index {match.start()}")
        else:
            print(f"---> {input_to_validate}?! ", end="")
            print(rude_remark())