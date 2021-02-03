from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint
from random import randint, uniform

from util.create_utils import create_devices

def format_title(heading: str) -> str:
    chars = len(heading)
    pad_chars_num = 80 - chars

    # If even number, pre and post padding is eqaul
    # else post is pre padding + 1
    if pad_chars_num % 2: # odd case
        pre_pad = int(pad_chars_num / 2)
        post_pad = pre_pad + 1
    
    else:  # Even case
        pre_pad = post_pad = int(pad_chars_num / 2)

    return ( 
        ('=' * 80) + '\n' +
        (' ' * pre_pad) + heading.upper() + (' ' * post_pad) + '\n' +
        ('=' * 80) + '\n'
    ) 


# Creating random devices
devices = create_devices(num_subnets=2, num_devices=25)

##################################################
# Printing all devices
print( format_title('printing all devices') )

for device in devices:
    print(
        f'{device["name"]:>30} {device["vendor"]:>10} : {device["os"]:<6} {device["ip"]:<15} {device["version"]}'
    )



##################################################
# Printing Cisco devices
print( format_title('printing cisco devices') )

for device in devices:
    if device['vendor'].lower() == 'cisco':
        print(
            f'{device["name"]:>30} {device["vendor"]:>10} : {device["os"]:<6} {device["ip"]:<15} {device["version"]}'
        )



##################################################
# Printing duplicate device names
print( format_title('finding duplicate device names') )

# For each device, search if name exists deeper into devices list
for index, searched_device in enumerate(devices):

    # Search for duplicate name starting at index + 1 thru the end of the list
    for compared_device in devices[index + 1:]:
        if searched_device['name'] == compared_device['name']:
            print(f'Found match! {searched_device["name"]} for both {searched_device["ip"]} and {compared_device["ip"]}')        



##################################################
# Printing device table
print( format_title('Create table of arbitrary "standard" vendor:os version') )

standard_versions = dict()

for device in devices:
    vendor_os = device['vendor'] + ':' + device['os']

    if vendor_os not in standard_versions:
        standard_versions[vendor_os] = device['version']

# Pretty print devices
pprint(standard_versions)



##################################################
# Print a list of non-compliant device OS versions
print( format_title('non-compliant devices') )

non_compliant_devices = dict()

# Initialize an empty list for each vendor os
for vendor_os, _ in standard_versions.items():
    non_compliant_devices[vendor_os] = list()

# Build non-compliant list
for device in devices:
    vendor_os = device['vendor'] + ':' + device['os']
    if device['version'] != standard_versions[vendor_os]:
        non_compliant_devices[vendor_os].append(f'{device["ip"]} version: {device["version"]}')

# Pretty print non-compliant devices
pprint(non_compliant_devices)



##################################################
# Assignment, copy, and deep copy
print( format_title('Assignment, copy, and deep copy') )

#---------------------------
devices2 = devices
print(f'(ASSIGNMENT) Variable IDs - {id(devices)} : {id(devices2)}')

if devices2 == devices:
    print('Assignment and modification: devices2 still equals devices')
    print('---> Moral: Assignment is NOT the same as copy!')
    print()
else:
    print('Huh?')


#---------------------------
devices2 = copy(devices)
print(f'(COPY) Variable IDs - {id(devices)} : {id(devices2)}')

devices2[0]['name'] = 'This is a dumb device filler'

if devices2 == devices:
    print('Shallow copy and modification: devices2 still equals devices')
    print('---> Moral: copy() only does a SHALLOW (1st level) copy!')
    print('---> Result: Uh-oh - I just screwed up the original version!!')
    print()

    # Print ids - each copy of the objects in the list continue to be the same
    for device1, device2 in zip(devices, devices2):
        print(f'Objects in list IDs - ObjA: {id(device1)} ObjB: {id(device2)}')
    
    print()

else:
    print('Huh?')

#---------------------------
devices2 = deepcopy(devices)
print(f'(DEEP COPY) Variable IDs - {id(devices)} : {id(devices2)}')

devices2[0]['name'] = 'This is another dumb device filler'

if devices2 == devices:
    print('Huh?')
else:
    print('Deep copy and modification: devices2 no longer equals devices')
    print('---> Moral: deepcopy() gives you a complete copy of the original!')
    print('---> Result: I can do whatever I want with my copy, without touching the original!!')
    print()

    # Print ids - each copy of the objects in the list no longer continue to be the same
    for device1, device2 in zip(devices, devices2):
        print(f'Objects in list IDs - ObjA: {id(device1)} ObjB: {id(device2)}')
    
    print()

#---------------------------
print( format_title('comparing two random list of devices') )

new_list_of_devices = create_devices(num_subnets=2, num_devices=25)

if new_list_of_devices == devices:
    print('Huh?')
else:
    print('Comparisons of complex, deep data is easy in Python')
    print('---> Moral: you can compare any two data structures, no matter how deeply nested')



##################################################
# Comparisons for implementing SLAs
print( format_title('Comparisons for implementing SLAs') )

SLA_AVAILABILITY = 96
SLA_RESPONSE_TIME = 1.0

devices = create_devices(num_subnets=2, num_devices=25)

for device in devices:
    device['availability'] = randint(94, 100)
    device['response_time'] = uniform(0.5, 1.1)

    if device['availability'] < SLA_AVAILABILITY:
        print(f'{datetime.now()}: {device["name"]:30} - Availability {device["availability"]} < {SLA_AVAILABILITY}')
    
    if device['response_time'] > SLA_RESPONSE_TIME:
        print(f'{datetime.now()}: {device["name"]:30} - Response Time {device["response_time"]} < {SLA_RESPONSE_TIME}')



##################################################
# Comparing classes
print( format_title('Comparing classes - with __eq__') )

class DeviceWithEq:

    def __init__(self, name, ip):
        self.name = name
        self.ip_address = ip
    
    def __eq__(self, other):
        if not isinstance(other, DeviceWithEq):
            return False

        return self.name == other.name and self.ip_address == other.ip_address

d1 = DeviceWithEq('device 1', '10.10.10.1')
d1_equal = DeviceWithEq('device 1', '10.10.10.1')
d1_different = DeviceWithEq('device 2', '10.10.10.2')


if d1 == d1_equal:
    print(f'!!! using __eq__ : success: {d1} equals {d1_equal}')
    
else:
    print(f'--> using __eq__ method to handle evaluation')


if d1 == d1_different:
    print(f'--> using __eq__ method to handle evaluation')

else:
    print(f'!!! using __eq__ : success: {d1} equals {d1_different}')

#-----------------------
print( format_title('Comparing classes - with no __eq__') )

class DeviceWithNoEq:

    def __init__(self, name, ip):
        self.name = name
        self.ip_address = ip


d1 = DeviceWithNoEq('device 1', '10.10.10.1')
d1_equal = DeviceWithNoEq('device 1', '10.10.10.1')
d1_same = d1


if d1 == d1_equal:
    print(f'!!! with no __eq__ : oops, didn\'t expect this')
else:
    print(f'--> with no __eq__ : success: not equal, as expected')

if d1 == d1_same:
    print(f'--> with no __eq__ : success: {d1} points to same object instance as {d1_same}')
else:
    print(f'!!! with no __eq__ : oops, didn\'t expect this')
