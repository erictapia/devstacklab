from netmiko import Netmiko


cisco_sandbox_device = {
    "ios": {
        "ip": "ios-xe-mgmt.cisco.com",
        "port": 8181,
        "username": "developer",
        "password": "C1sco12345",
        "device_type": "cisco_ios"
    },
    "nxos": {
        "ip": "sbx-nxos-mgmt.cisco.com",
        "port": 8181,
        "username": "admin",
        "password": "Admin_1234!",
        "device_type": "cisco_nxos"
    }
}


def netmiko_connect(device_type):

    print(
        f"\n\nConnecting to {cisco_sandbox_device[device_type]['ip']}:{cisco_sandbox_device[device_type]['port']}"
    )
    print("... this may take a little while.")

    connection = Netmiko(**cisco_sandbox_device[device_type])

    return connection
