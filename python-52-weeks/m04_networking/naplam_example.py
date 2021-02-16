import json
import copy

import napalm
import urllib3

from connect import cisco_sandbox_device


# Disable insecure HTTPS request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


IOS = "ios"
NXOS = "nxos"
NXOS_SSH = "nxos_ssh"

devices = copy.deepcopy(cisco_sandbox_device)

# make a copy of NXOS, so we can do both SSH and NXAPI connections
devices[NXOS_SSH] = copy.deepcopy(devices[NXOS])


def func_call(obj):
    try:
        print(json.dumps(obj(), sort_keys=True, indent=4))
    
    except (IOError, KeyError, NameError, NotImplementedError) as e:
        print(f"oops, looks like there is a NAPALM exception, error: {e}")

    except:
        print(f"oops, looks like there is an exception")  


for device_type, device in devices.items():
    print(f"\n----- connecting to device {device_type}: {device['ip']} ----------")
    driver = napalm.get_network_driver(device_type)
    
    if device_type == NXOS:
        napalm_device = driver(
            hostname=device["ip"],
            username=device["username"],
            password=device["password"],
        )
    
    else:
        napalm_device = driver(
            hostname=device["ip"],
            username=device["username"],
            password=device["password"],
            optional_args={"port": device["port"]},
        )
    
    try:
        napalm_device.open()
    
    except napalm.base.exceptions.ConnectionException as e:
        print(f"oops, looks like there is a NAPALM exception, error: {e}")
        continue

    print("\n----- facts ----------")
    func_call(napalm_device.get_facts) 

    print("\n----- interfaces ----------")
    func_call(napalm_device.get_interfaces) 

    print("\n----- vlans ----------")
    func_call(napalm_device.get_vlans) 
    
    print("\n----- snmp ----------")
    func_call(napalm_device.get_snmp_information)

    print("\n----- interface counters ----------")
    func_call(napalm_device.get_interfaces_counters)

    print("\n----- environment ----------")
    func_call(napalm_device.get_environment)    

    napalm_device.close()
