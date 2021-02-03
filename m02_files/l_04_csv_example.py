import csv
from pprint import pprint

from tabulate import tabulate

from l_00_inventory import csv_inventory


##### CONVERT INVENTORY TO CSV AND WRITE TO FILE
with open("l_00_inventory.csv", "w") as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerows(csv_inventory)

##### READ CSV INVENTORY FROM FILE
with open("l_00_inventory.csv") as csv_in:
    csv_reader = csv.reader(csv_in)
    saved_csv_inventory = list()

    for device in csv_reader:
        saved_csv_inventory.append(device)

##### PRINT CSV INVENTORY STRING
print(f"l_00_inventory.csv file:\n\n{saved_csv_inventory}")
print()

##### PRETTY PRINT
print("csv pretty print")
pprint(saved_csv_inventory)
print()

##### COMPARE INVENTORY WE READ, WITH ORIGINAL INVENTORY, TO MAKE SURE THEY ARE EQUIVALENT
if saved_csv_inventory == csv_inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")

print()

##### TURN LIST OF LISTS INTO DICTIONARY
devices = list()

for row in range(1, len(csv_inventory)):
    device = dict()
    
    for column, header in enumerate(csv_inventory[0]):
        device[header] = csv_inventory[row][column]
    
    devices.append(device)

##### PRETTY PRINT DEVICES AS LIST OF DICTS
print("\n----- Devices as list of dicts --------------------")
pprint(devices)

print("\n----- tabulate output of devices from spreadsheet --------------------")
print("\n", tabulate(devices, headers="keys"))
print()

# CONVERT PYTHON DATA BACK INTO CSV
headers = devices[0].keys()
with open("l_00_inventory_back_to_csv.csv", "w") as csv_out:
    csv_writer = csv.DictWriter(csv_out, headers)
    csv_writer.writeheader()
    csv_writer.writerows(devices)
