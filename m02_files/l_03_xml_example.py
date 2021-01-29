from pprint import pprint

import xmltodict

from l_00_inventory import xml_inventory


##### CONVERT PYTHON DATA TO XML AND WRITE TO FILE
with open("l_00_inventory.xml", "w") as xml_out:
    xml_out.write(xmltodict.unparse(xml_inventory, pretty=True))

# READ IN XML FROM FILE AND CONVERT TO PYTHON DATA
with open("l_00_inventory.xml") as xml_in:
    saved_inventory = xmltodict.parse(xml_in.read())

print("=" * 80)
print(f"XML PPRINT version of type: {type(saved_inventory)}")
print("=" * 80)

pprint(saved_inventory)

print("=" * 80)


#####  READ IN XML FROM FILE AND CONVERT TO PYTHON DATA
with open("l_00_inventory.xml") as xml_in:
    saved_inventory = xmltodict.parse(xml_in.read(), dict_constructor=dict)

print("=" * 80)
print(f"XML PPRINT version of type: {type(saved_inventory)}")
print("=" * 80)

pprint(saved_inventory)

print("=" * 80)


##### PRINTING WITH XMLTODICT.UNPARSE
print("=" * 80)
print(f"Print using xmltodict.unparse version of type: {type(saved_inventory)}")
print("=" * 80)

print(xmltodict.unparse(saved_inventory, pretty=True))

print("=" * 80)


##### COMPARE ORIGINAL WITH CONVERTED AND SAVED DATA
print("=" * 80)
print("Compare saved inventory with original")
print("=" * 80)

if saved_inventory == xml_inventory:
    print("-- worked: saved inventory equals original")

else:
    print("-- failed: saved inventory different from original")

print("=" * 80)
