from pprint import pprint

from util.create_utils import create_networks

networks = create_networks(10, 5)

pprint(networks)

for subnet_addr, subnet in networks['subnets'].items():
    print('='*80)
    print(f'subnet: {subnet_addr}')
    print('='*80)

    for device in subnet['devices']:
        print(f'  device: {device["name"]:30} {device["ip"]:10} {device["vendor"]: >10} : {device["os"]} ')