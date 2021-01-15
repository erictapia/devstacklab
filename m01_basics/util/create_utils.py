from operator import itemgetter
from random import choice
import string

from tabulate import tabulate

import util.constants as CONST

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
    for subnet in range(num_subnets + 2):
        for octet in range(1, num_devices + 1):
            # Device IP
            ip = f'10.0.{subnet}.{octet}'
            
            device = random_device(ip)
            
            # Append device to list of devices
            devices.append(device)
    
    return devices

def create_networks(num_devices: int = 1, num_subnets: int=1) -> dict:

    devices = create_devices(num_devices, num_subnets)

    network = dict()
    network['subnets'] = dict()

    for device in devices:
        subnet_address_octets = device['ip'].split('.')
        subnet_address_octets[3] = '0'
        subnet_address = '.'.join(subnet_address_octets)

        if subnet_address not in network['subnets']:
            network['subnets'][subnet_address] = dict()
            network['subnets'][subnet_address]['devices'] = list()
        
        network['subnets'][subnet_address]['devices'].append(device)

        interfaces = list()
        for index in range( 0, choice([2, 4, 8]) ):
            interface = {
                'name': f'g0/0/{index}',
                'speed': choice(['10', '100', '1000'])
            }

            interfaces.append(interface)
    
        device['interfaces'] = interfaces
    
    return network

def print_devices_tabulated(devices: list, key: itemgetter) -> None:
    # Print table of devices
    print("\n----- SORTED DEVICES IN TABULAR FORMAT --------------------")
    ordered_devices = sorted(devices, key=key)
    print(tabulate(ordered_devices, headers='keys'))

