from operator import itemgetter
from random import choice
import string

from tabulate import tabulate

import constants as CONST

def random_device(ip: int) -> dict:
    device = dict()

    vendor     = choice( [*CONST.VENDORS.keys()] )
    os         = choice([ *CONST.VENDORS[vendor].keys() ])
    version    = choice([ *CONST.VENDORS[vendor][os] ])
    site       = choice(CONST.SITES)
    dist_frame = choice(CONST.DISTRIBUTION_FRAMES)
    suffix     = choice(string.ascii_letters)

    device['vendor']  = vendor
    device['os']      = os
    device['version'] = version
    device['name']    = f'{site}.{dist_frame}.{vendor}.{os}.{suffix}'
    device['ip']      = ip

    return device

def create_devices(num_devices: int = 10, num_subnets: int = 2) -> list:
    devices = list()    # Create empty list of devices

    # Create random devices
    for subnet in range(num_subnets):
        for index in range(num_devices):
            # Device IP
            ip = f'10.0.{subnet + 1}.{index + 1}'
            
            device = random_device(ip)
            
            # Append device to list of devices
            devices.append(device)
    
    return devices

def print_devices_tabulated(devices: list, key: itemgetter) -> None:
    # Print table of devices
    print("\n----- SORTED DEVICES IN TABULAR FORMAT --------------------")
    ordered_devices = sorted(devices, key=key)
    print(tabulate(ordered_devices, headers='keys'))