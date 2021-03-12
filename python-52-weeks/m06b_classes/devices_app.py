from pprint import pprint

from device_netmiko import DeviceNetmiko
from device_napalm import DeviceNapalm
from device_ncclient import DeviceNcclient
from misc_types import DeviceType


def create_devices():
    created_devices = dict()
    created_devices["nxos-netmiko"] = DeviceNetmiko(
        name="nxos-netmiko",
        hostname="sbx-nxos-mgmt.cisco.com",
        device_type=DeviceType.CISCO_NXOS
    )
    created_devices["nxos-netmiko"].set_port(8181)
    created_devices["nxos-netmiko"].set_credentials(username="admin", password="Admin_1234!")

    created_devices["nxos-napalm"] = DeviceNapalm(
        name="nxos-napalm",
        hostname="sbx-nxos-mgmt.cisco.com",
        device_type=DeviceType.NXOS,
    )
    created_devices["nxos-napalm"].set_port(8181)
    created_devices["nxos-napalm"].set_credentials(username="admin", password="Admin_1234!")

    created_devices["nxos-ncclient"] = DeviceNcclient(
        name="nxos-ncclient",
        hostname="sbx-nxos-mgmt.cisco.com",
        device_type=DeviceType.NEXUS,
    )
    created_devices["nxos-ncclient"].set_port(10000)
    created_devices["nxos-ncclient"].set_credentials(username="admin", password="Admin_1234!")

    return created_devices


devices = create_devices()
for _, device in devices.items():

    if not device.connect():
        print(f"----- Connection failed: {device.name}")
        continue

    facts = device.get_facts()
    print(f"----- Facts for device: {device.name}")
    pprint(facts)
    device.disconnect()