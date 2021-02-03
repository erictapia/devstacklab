import time

from util.create_utils import random_device, create_devices, create_devices_generator

if __name__ == "__main__":

    devices = create_devices(num_devices=254, num_subnets=254)

    devices_dict = dict()
    for device in devices:
        devices_dict[device["ip"]] = device

    devices_generator = create_devices_generator(num_devices=254, num_subnets=254)

    while True:

        ip_to_find = input("\nEnter IP address to find: ")

        if not ip_to_find:
            break

        start = time.time()

        for device in devices_generator:
            if device["ip"] == ip_to_find:
                print(f"--> found it (generator): {device}")
                generator_search_time = (time.time() - start) * 1000
                print(f"--- ---> {generator_search_time:.4f} msec")
                print(f"--- ---> id fo device: {id(device)}")
                break

        else:
            print(f"---! IP address not found, try again")

        print()
        start = time.time()
        for ip_to_find in devices_dict:
                print(f"--> found it (dict): {devices_dict[ip_to_find]}")
                dict_search_time = (time.time() - start) * 1000
                print(f"--- ---> {dict_search_time:.4f} msec")
                print(f"--- ---> id fo device: {id(device)}")
                break


    ######### SIMPLE GENERATOR COMPREHENSION
    print("\n\n____ DEVICE INFO PARSING USING GENERATOR COMPREHENSION_______________________\n")

    device_str = "  r3-L-n7, cisco, catalyst 2960, ios , extra stupid stuff "

    device = [item.strip() for item in device_str.split(",")]
    print(f"--- device type: {type(device)}")
    print(f"--- device using list comprehension:\n\t\t{device}")

    print()

    device = [(item.strip() for item in device_str.split(","))]
    print(f"--- device type: {type(device)}")
    print(f"--- device using generator comprehension:\n\t\t{device}")



    ######### MORE INTERESTING GENERATOR COMPREHENSION
    print("\n\n____ DEVICE CREATION USING GENERATOR COMPREHENSION___________________________\n")

    devices_gen = (random_device(f"10.0.1.{i}") for i in range(1, 25))

    print(f"--- devices_gen type: {type(devices_gen)}")
    print("--- devices_gen:\n")

    for device in devices_gen:
        print(device)
