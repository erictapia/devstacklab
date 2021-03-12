from netmiko import Netmiko

from device import Device
from util import get_version_from_show, get_uptime_from_show


class DeviceNetmiko(Device):

    def connect(self):
        print(f"\n\n----- Connecting to {self.hostname}:{self.port}")
        try:
            self.connection = Netmiko(
                self.hostname,
                port=self.port,
                username=self.username,
                password=self.password,
                device_type=self.device_type,
            )
        except:
            self.connection = None
            print("----- Could not connect --------------------")
            return False

        print(f"----- Connected! --------------------")
        return True

    def get_facts(self):
        if self.connection:
            show_hostname_output = self.connection.send_command("show hostname")
            show_version_output = self.connection.send_command("show version")
            show_serial_output = self.connection.send_command("show license host-id")
            show_uptime_output = self.connection.send_command("show system uptime")

            facts = dict()
            facts["os_version"] = get_version_from_show(show_version_output)
            facts["hostname"] = show_hostname_output.strip()
            facts["serial_number"] = show_serial_output.strip()[20:]  # Don't do this :-)
            facts["uptime"] = get_uptime_from_show(show_uptime_output)

            return facts

    def disconnect(self):
        if self.connection:
            self.connection.disconnect()
            print(f"----- Disconnected! --------------------")

        return True
