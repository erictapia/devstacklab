
device_str ="  r3-L-n7, cisco, catalyst 2960, ios , extra stupid stuff "

############# USING A LIST #####################################################
device = list()

############# NON LIST COMPREHENSION WAY
for item in device_str.split(","):
    device.append( item.strip() )

print(f"\ndevice using for loop: \n\t\t{device}")


############# LIST COMPREHENSION WAY
device = [item.strip() for item in device_str.split(",")]

print(f"\ndevice using list comprehension: \n\t\t{device}")


############# SIMPLIER LIST COMPREHENSION aka REABABLE LIST COMPREHENSION
device_info_list = device_str.split(",")

device = [item.strip() for item in device_info_list]

print(f"\ndevice using simplier list comprehension: \n\t\t{device}")


############# LIST COMPREHENSION WITH CONDITIONAL
device = [item.strip() for item in device_str.split(",") if "stupid" not in item]

print(f"\ndevice using list comprehension with conditional: \n\t\t{device}")



############# USING A DICT #####################################################

############# DICT COMPREHENSION FROM LIST OF TUPLES
device_info = [
    ("name", "r3-L-n7"),
    ("vendor", "cisco"),
    ("model", "catalyst 2960"),
    ("os", "ios"),
]

device = {item[0]: item[1] for item in device_info}

print(f"\ndevice using dict comprehension from tuples: \n\t\t{device}")
print("\n    device nicely formatted:")

for key, value in device.items():
    print(f"{key:>16s} : {value}")


############# LIST THEN DICT COMPREHENSION FROM STRING
device_info_str = "name:r3-L-n7, vendor:cisco, model:catalyst 2960, os:ios, version:12.1(T)"

device_info_pair = [kv_pair.split(":") for kv_pair in device_info_str.split(",")]
device = {item[0]: item[1] for item in device_info_pair}

print(f"\ndevice using list and then dict comprehension from string: \n\t\t{device}")
print("\n    device nicely formatted:")

for key, value in device.items():
    print(f"{key:>16s} : {value}")


############# DICT COMPREHENSION FROM STRING
device = {item.split(":")[0]: item.split(":")[1] for item in device_info_str.split(",")}

print(f"\ndevice using dict comprehension from string: \n\t\t{device}")
print("\n    device nicely formatted:")

for key, value in device.items():
    print(f"{key:>16s} : {value}")