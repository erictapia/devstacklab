from datetime import datetime
import socket

import requests
import scapy.all as scapy


BASEURL = "http://127.0.0.1:5000"
# DISCOVERY_INTERVAL = 300
DISCOVERY_SUBNET = input("Enter subnet to be discovered x.x.x.x/xx: ")
# MONITOR_INTERVAL = 15
# PORTSCAN_INTERVAL = 3600


def get_hosts():
    print("\n\n----> Retrieving hosts ...", end="")

    response = requests.get(f"{BASEURL}/hosts")

    if response.status_code != 200:
        print(f" !!! Failed to retrieve hosts from server: {response.reason}")
        return {}

    print(" Hosts successfully retrieve")
    return response.json()


def discovery():
    # DISCOVER HOSTS ON NETWORK USING ARPING FUNCTION
    print(
        "\n\n----- Discovery hosts on network using arping() function ---------------------"
    )

    ans, unans = scapy.arping(DISCOVERY_SUBNET)
    ans.summary()

    for res in ans.res:

        ip_addr = res[1].payload.psrc
        mac_addr = res[1].payload.hwsrc

        try:
            hostname = socket.gethostbyaddr(str(ip_addr))
        except (socket.error, socket.gaierror):
            hostname = str(ip_addr), [], [str(ip_addr)]

        last_heard = str(datetime.now())[:-3]

        host = {
            "ip_address": ip_addr,
            "mac_address": mac_addr,
            "hostname": hostname[0],
            "last_heard": last_heard,
            "availability": True,
            #"open_tcp_ports": list()
        }

        update_host(host)


def portscan_hosts(hosts):
    for host in hosts.values():
        if "availability" not in host or not host["availability"]:
            continue

        ip = host["ip_address"]

        print(f"====> Scanning host: {host['hostname']} at IP: {host['ip']}")
        nm = nmap.PortScanner()
        nm.scan(ip, '22-1024')

        try:
            nm[ip]
        except KeyError as e:
            print(f" !!!  Scan failed: {e}")
            continue

        print(f"===> Scan results: {nm[ip].all_tcp()}")
        host["open_tcp_ports"] = nm[ip].all_tcp()
        update_host(host)


def update_host(host):
    print(f"----> Updating host status via REST API: {host['hostname']}", end="")

    response = requests.put(f"{BASEURL}/hosts", params={"hostname": host['hostname']}, json=host)

    if response.status_code != 204:
        print(
            f"{str(datetime.now())[:-3]}: Error posting to /hosts, response: {response.status_code}, {response.content}"
        )
        print(f" !!!  Unsuccessful attempt to update host status via REST API: {host['hostname']}")
    else:
        print(f" Successfully updated host status via REST API: {host['hostname']}")
