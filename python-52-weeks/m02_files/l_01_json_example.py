import json

from l_00_inventory import inventory

##### CONVERT INVENTORY TO JSON AND WRITE TO FILE
with open("l_00_inventory.json", "w") as json_out:
    json_out.write(json.dumps(inventory, indent=4))


##### READ JSON INVENTORY FROM FILE AS STRING
with open("l_00_inventory.json", "r") as json_in:
    json_inventory = json_in.read()

##### PRINT JSON INVENTORY AS STRING
print("\njson as string version:")
print("=" * 79)
print(f"l_00_inventory.json file: {json_inventory}")

##### CONVERT JSON INVENTORY TO PYTHON DICT AND PRINT
print("\njson -> dict version:")
print("=" * 79)
print(json.loads(json_inventory))

##### AGAIN, CONVERTT BACK TO STRING W/INDENTING, AND PRINT
print("\njson pretty version:")
print("=" * 79)
print( json.dumps( json.loads(json_inventory), indent=4 ) )

##### COMPARE INVENTORY WE READ WITH ORIGINAL INVENTORY,
##### MAKE SURE THEY ARE EQUIVALENT
print("\ncompare saved inventory with original")
print("=" * 79)
saved_inventory = json.loads(json_inventory)

if saved_inventory == inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory does not equal original")