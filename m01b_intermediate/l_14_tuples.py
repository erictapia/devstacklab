from pprint import pprint

from util.create_utils import create_devices

if __name__ == "__main__":

    devices_list = create_devices(num_devices=4, num_subnets=1)
    devices_tuple = tuple( create_devices(num_devices=4, num_subnets=1) )

    pprint(devices_list)
    print()
    pprint(devices_tuple)