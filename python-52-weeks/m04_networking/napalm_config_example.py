import copy
import urllib3

import napalm
from connect import cisco_sandbox_device


# Disabled request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


IOS = "ios"
NXOS = "nxos"
NXOS_SSH = "nxos_ssh"


devices = copy.deepcopy(cisco_sandbox_device)
devices[NXOS_SSH] = copy.deepcopy(devices[NXOS])

for device_type, device in devices.items():
    print(f"\n----- connecting to             device {device_type}: {device['ip']}")
    driver = napalm.get_network_driver(device_type)
    
    if device_type == NXOS:
        napalm_device = driver(
            hostname=device["ip"],
            username=device["username"],
            password=device["password"],
        )
        continue  # Causes exception, AttributeError: NXOSDriver object hat no attribute '_netmiko_device'
    else:
        napalm_device = driver(
            hostname=device["ip"],
            username=device["username"],
            password=device["password"],
            optional_args={"port": device["port"]},
        )

    try:
        print(f"----- connect to                device {device['ip']}, type: {device_type} ----------")
        napalm_device.open()
    
    except napalm.base.exceptions.ConnectionException as e:
        print(f"oops, looks like there is a NAPALM exception, error: {e}")
        continue

    print(f"----- get configuration for     device {device['ip']}, type: {device_type} ----------")  
    if device_type == NXOS or device_type == NXOS_SSH:
        config_for_compare = napalm_device._get_checkpoint_file()
    
    else:
        config_for_compare = napalm_device.get_config()["running"]

    with open(f"cisco.{device_type}.config", "w") as config_out:
        config_out.write(config_for_compare)
    
    print(f"----- load candiate config for  device {device['ip']}, type: {device_type} ----------")
    napalm_device.load_replace_candidate(filename=f"cisco.{device_type}.config")

    print(f"----- compare config for        device {device['ip']}, type: {device_type} ----------")
    diff = napalm_device.compare_config()

    print(f"----- diff output for           device {device['ip']}, type: {device_type} ----------")
    print(diff)

    napalm_device.close()

    print("=" * 80)
