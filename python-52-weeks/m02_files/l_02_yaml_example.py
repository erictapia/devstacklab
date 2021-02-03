import yaml

from l_00_inventory import inventory


##### CONVERT INVENTORY TO YAML AND WRITE TO FILE
with open("l_00_inventory.yaml", "w") as yaml_out:
    yaml_out.write(yaml.dump(inventory))

##### READ YAML INVENTORY FROM FILE
with open("l_00_inventory.yaml", "r") as yaml_in:
    yaml_inventory = yaml_in.read()

##### PRINT YAML INVENTORY STRING
print(f"l_00_inventory.yaml file: \n\n{yaml_inventory}")

##### PRINT YAML INVENTORY USING YAML.DUMP( YAML.SAFE_LOAD )
print("\nYAML Pretty version:\n")
print(yaml.dump(yaml.safe_load(yaml_inventory), indent=4))

##### COMPARE INVENTORY WE READ, WITH ORIGINAL INVENTORY, TO MAKE SURE THEY
##### ARE EQUIVALENT
print("\n----- compare saved inventory with original --------------------")
saved_inventory = yaml.safe_load(yaml_inventory)
if saved_inventory == inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")


##### READ THE ALT-FORMATTED YAML FILE
with open("l_00_inventory_formatted.yaml", "r") as yaml_in:
    yaml_inventory_alt = yaml_in.read()

##### PRING ALT-FORMATTED YAML INVENTORY STRING
print("\n\nl_00_formatted.yaml file:\n")
print(yaml_inventory_alt)

##### COMPARE INVENTORY WE READ, WITH ORIGINAL INVENTORY, TO MAKE SURE THEY
##### ARE EQUIVALENT
print("\n----- compare saved inventory with original --------------------")
saved_inventory_alt = yaml.safe_load(yaml_inventory_alt)
if saved_inventory_alt == inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")