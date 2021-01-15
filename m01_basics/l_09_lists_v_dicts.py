from operator import itemgetter
import time

from util.create_utils import create_devices, print_devices_tabulated


def print_found(print_header, device, time):
    print("=" * 80)
    print(f"{print_header}")
    print(f"    Found it: {device}")
    print(f"        in: {time:.4f} msec")
    print(f"        device id: { id(device) }")

def print_not_found(print_header, ip_to_find, time):
    print(f"{print_header}")
    print(f"    {ip_to_find} not found, try again")
    print(f"        Search time: {time:.4f} msec")

if __name__ == "__main__":

    devices = create_devices(254, 254)

#############################################################################
    # Creating a dict of pointers to a device in devices
    devices_dict = dict()

    for device in devices:
        devices_dict[ device["ip"] ] = device

    while True:
        ip_to_find = input("Enter IP address to find: ")

        if not ip_to_find:
            break

##############################################################################
        # Search list of devices
        start_time = time.time()

        for device in devices:
            if device["ip"] == ip_to_find:
                list_search_time = ( time.time() - start_time ) * 1000
                print_found("LIST SEARCH", device, list_search_time)
                break

        else:
            list_search_time = ( time.time() - start_time ) * 1000
            print_not_found("LIST SEARCH", ip_to_find, list_search_time)

##############################################################################
        # Search dict of devices
        start_time = time.time()

        if ip_to_find in devices_dict:
            dict_search_time = ( time.time() - start_time ) * 1000
            print_found("DICT SEARCH", device, dict_search_time)

        else:
            dict_search_time = ( time.time() - start_time ) * 1000
            print_not_found("DICT SEARCH", ip_to_find, dict_search_time)

##############################################################################
        # Access dict with key
        start_time = time.time()

        try:
            dict_access_time = ( time.time() - start_time ) * 1000
            print_found("DICT ACCESS", devices_dict[ip_to_find] , dict_access_time)

        except KeyError:
            dict_access_time = ( time.time() - start_time ) * 1000
            print_not_found("DICT ACCESS", ip_to_find, dict_access_time)

#############################################################################
        # Comparing durations between list vs dict
        print("=" * 80)
        print(f"List Search: {list_search_time:.4f} msec")
        print(f"Dict Search: {dict_search_time:.4f} msec")
        print(f"Dict Access: {dict_access_time:.4f} msec")
        print("=" * 80)

