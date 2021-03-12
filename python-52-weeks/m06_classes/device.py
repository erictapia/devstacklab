from facts import get_facts_netmiko, get_facts_napalm, get_facts_ncclient

from connect import (
    connect_netmiko,
    connect_napalm,
    connect_ncclient,
    disconnect_netmiko,
    disconnect_napalm,
    disconnect_ncclient,
)
from misc_types import TransportType


class Device:
    def __init__(self, name, device_type, hostname, transport):
        self.name = name
        self.device_type = device_type
        self.hostname = hostname
        self.transport = transport

        self.mac = None
        self.ip = None
        self.connection = None

        self.username = None
        self.password = None
        self.port = None

    def connect(self):
        try:
            if self.transport == TransportType.NAPALM:
                self.connection = connect_napalm(
                    self.hostname, self.username, self.password, self.port, self.device_type
                )
            elif self.transport == TransportType.NCCLIENT:
                self.connection = connect_ncclient(
                    self.hostname, self.username, self.password, self.port, self.device_type
                )
            elif self.transport == TransportType.NETMIKO:
                self.connection = connect_netmiko(
                    self.hostname, self.username, self.password, self.port, self.device_type
                )
        except:
            return False

        return True

    def disconnect(self):
        if self.transport == TransportType.NAPALM:
            disconnect_napalm(self.connection)
        elif self.transport == TransportType.NCCLIENT:
            disconnect_ncclient(self.connection)
        elif self.transport == TransportType.NETMIKO:
            disconnect_netmiko(self.connection)

    def get_facts(self):

        if self.transport == TransportType.NAPALM:
            return get_facts_napalm(self.connection)
        elif self.transport == TransportType.NCCLIENT:
            return get_facts_ncclient(self.connection)
        elif self.transport == TransportType.NETMIKO:
            return get_facts_netmiko(self.connection)

    def set_credentials(self, username, password):
        self.username = username
        self.password = password

    def set_port(self, port):
        self.port = port
