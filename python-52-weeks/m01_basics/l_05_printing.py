from datetime import datetime
from pprint import pprint
from operator import itemgetter
from random import choice
from time import sleep

import nmap
from tabulate import tabulate

from util.create_utils import create_devices

devices = create_devices(25, 1)

#########################################
print('='*80)

print('\n\nUsing Print')
print()
print(devices)

print('='*80)

#########################################

print('\n\nUsing Pretty Print')
print()
pprint(devices)

print('='*80)

#########################################

print('\n\nUsing For loop')
print()

for device in devices:
    sleep(0.1)
    device['last_heard'] = str( datetime.now() )
    print(device)

print('='*80)

#########################################

print('\n\nUsing Tabulate')
print()

itemkey = itemgetter('vendor', 'os', 'version')
print( tabulate( sorted(devices, key=itemkey), headers='keys') )

print('='*80)

#########################################

print('\n\nUsing for loop and f-string')
print()
for device in devices:
    print(
        f'{device["name"]:>30} {device["vendor"]:>10} : {device["os"]:<6} {device["ip"]:<15} {device["last_heard"][:-4]}')

print('='*80)

#########################################

print('\n\nUsing for loop, f-string, and sorted descending by last_heard')
print()
for device in sorted(devices, key=itemkey, reverse=True):
    print(
        f'{device["name"]:>30} {device["vendor"]:>10} : {device["os"]:<6} {device["ip"]:<15} {device["last_heard"][:-4]}')

print('='*80)

#########################################

print('\n\nUsing Multiple print statements, same line')
print()

print('Testing devices.')

for device in devices:
    print(f'--- testing device {device["name"]} ...', end='')
    sleep(choice([0.1, 0.2, 0.3, 0.4]))
    print('done')

print('Testing completed.')

print('='*80)

#########################################

# nm = nmap.PortScanner()

# while True:

#     ip = input('\nInput IP address to scan: ')
#     if not ip:
#         break
    
#     print(f'\n--- beginning scan of {ip}')
#     output = nm.scan(ip, '22-2024')
#     print(f'--- --- command: {nm.command_line()}')

#     print('----- nmap scan output ----------------------------------')
#     pprint(output)

# print('='*80)

#########################################


#########################################