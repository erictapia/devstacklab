from operator import itemgetter
from pprint import pprint
from random import choice
import string

from tabulate import tabulate

import constants as CONST



def random_device(vendors, sites, frames, ip, device):
    try:
        vendor     = choice( [*vendors.keys()] )
        os         = choice([ *vendors[vendor].keys() ])
        version    = choice([ *vendors[vendor][os] ])
        site       = choice(sites)
        dist_frame = choice(frames)
        suffix     = choice(string.ascii_letters)

        device['vendor']  = vendor
        device['os']      = os
        device['version'] = version
        device['name']    = f'{site}.{dist_frame}.{vendor}.{os}.{suffix}'
        device['ip']      = ip

    except: 
        raise Exception(f'\n\nFailed to create random devices. Params passed: \n\n' 
                        + f'vendors: {vendors}\n'
                        + f'sites: {sites}\n' 
                        + f'frames: {frames}\n'
                        + f'ip: {ip}\n'
                        + f'device: {device}'
        )

def run():
    devices = list()    # Create empty list of devices

    # Create random devices
    for index in range(CONST.TOTAL_DEVICES):
        device = dict()

        # Device IP
        ip = f'10.0.0.{index + 1}'
        
        random_device(CONST.VENDORS, CONST.SITES, CONST.DISTRIBUTION_FRAMES, ip, device)

        # Print device
        # Pretty print devices
        print("\n----- DEViCE DICT --------------------")
        for key, value in device.items():
            print(f'{key:>16s} : {value}')
        
        # Append device to list of devices
        devices.append(device)

    # Pretty print devices
    print("\n----- DEViCES AS LIST OF DICTS --------------------")
    pprint(devices)

    # Print table of devices
    print("\n----- SORTED DEVICES IN TABULAR FORMAT --------------------")
    key = itemgetter('vendor', 'os', 'version')
    ordered_devices = sorted(devices, key=key)
    print(tabulate(ordered_devices, headers='keys'))
    

if __name__ == '__main__':
    run()

