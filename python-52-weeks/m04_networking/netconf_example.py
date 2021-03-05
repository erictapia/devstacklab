from pprint import pprint
from xml.dom.minidom import parseString

from lxml import etree
from ncclient import manager
import xmltodict


if __name__ == "__main__":
    csr_device = {
        "host": "ios-xe-mgmt.cisco.com",
        "port": 10000,
        "username": "developer",
        "password": "C1sco12345",
        "device_params": {"name": "csr"},
    }
    nxos_device = {
        "host": "sbx-nxos-mgmt.cisco.com",
        "port": 10000,
        "username": "admin",
        "password": "Admin_1234!",
        "device_params": {"name": "nexus"},
    }

    for device in [nxos_device, csr_device]:
        print(f"----- Connecting to: {device['host']} ------")
        nc_connection = manager.connect(**device, hostkey_verify=False)

        print(f"----- Connected -----\n")

        if device["device_params"]["name"] == "nexus":
            serial_number_xml_nxos = "<System xmlns='http://cisco.com/ns/yang/cisco-nx-os-device'><serial/></System>"

            response = nc_connection.get(("subtree", serial_number_xml_nxos))

            print(f"\n----- XML get() serial number subtree from: {device['host']}")
            print(str(etree.tostring(response.data_ele, pretty_print=True).decode()))

        else: # csr
            # GET THE WHOLE CONFIG, AND THEN PARSE IT
            config = nc_connection.get_config("running")
            print(f"\n----- XML get_config() output from: {device['host']}")
            print(str(etree.tostring(config.data_ele, pretty_print=True).decode()))

            xml_doc = parseString(str(config))
            version = xml_doc.getElementsByTagName("version")
            print(f"\n----- Device OS version, hostname, email from: {device['host']}")
            if len(version) > 0:
                print(f"        version: {version[0].firstChild.nodeValue}")
            else:
                print(f"        Unable to retrieve version!")

            hostname = xml_doc.getElementsByTagName("hostname")
            if len(hostname) > 0:
                print(f"        hostname: {hostname[0].firstChild.nodeValue}")
            else:
                print(f"        Unable to retrieve hostname!")

            email = xml_doc.getElementsByTagName("contact-email-addr")
            if len(email) > 0:
                print(f"        email: {email[0].firstChild.nodeValue}")
            else:
                print(f"        Unable to retrieve email!")

            usernames = xml_doc.getElementsByTagName("username")
            for username in usernames:
                name = username.getElementsByTagName("name")
                if len(name) > 0:
                    print(f"        name: {name[0].firstChild.nodeValue}")
                else:
                    print(f"        Unable to retrieve name from username!")

            version_filter = """
                                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                                    <version></version>
                                </native>
            """
            rsp = nc_connection.get(("subtree", version_filter))
            print(f"\n----- XML get() version subtree from: {device['host']}")
            print(str(etree.tostring(rsp.data_ele, pretty_print=True).decode()))

            cpu_filter = """
                              <filter>
                                <cpu-usage xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-process-cpu-oper">
                                </cpu-usage>
                              </filter>
                            """

            rsp = nc_connection.get(cpu_filter)
            print(f"\n----- XML get() cpu subtree from: {device['host']}")
            print(str(etree.tostring(rsp.data_ele, pretty_print=True).decode()))

            memory_filter = """
                              <filter>
                                <memory-statistics xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-memory-oper">
                                </memory-statistics>
                              </filter>
                            """

            rsp = nc_connection.get(memory_filter)
            print(f"\n----- XML get() memory subtree from: {device['host']}")
            print(str(etree.tostring(rsp.data_ele, pretty_print=True).decode()))

            memory_statistics = xmltodict.parse(
                str(etree.tostring(rsp.data_ele, pretty_print=True).decode()),
                dict_constructor=dict,
            )
            print("\n----- Memory statistics --------------------\n")
            pprint(memory_statistics)
