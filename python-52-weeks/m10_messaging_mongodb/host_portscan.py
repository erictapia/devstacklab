from datetime import datetime
from time import sleep

import nmap
import requests


MONITOR_INTERVAL = 60
BASEURL = "http://127.0.0.1:5000"

def get_hosts():

    print("\n\n----> Retrieving hosts ...", end="")
    response = requests.get(f"{BASEURL}/hosts")
    if response.status_code != 200:
        print(f" !!!  Failed to retrieve hosts from server: {response.reason}")
        return {}

    print(" Hosts successfully retrieved")
    return response.json()


def portscan_hosts(hosts):

    for host in hosts.values():

        if "availability" not in host or not host["availability"]:
            continue

        ip = host["ip_address"]
        print(f"====> Scanning host: {host['hostname']} at IP: {ip}")
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


def run():

    while True:

        hosts = get_hosts()
        portscan_hosts(hosts)

        sleep(MONITOR_INTERVAL)


def update_host(host):

    print(f"----> Updating host status via REST API: {host['hostname']}", end="")
    rsp = requests.put(f"{BASEURL}/hosts", params={"hostname": host["hostname"]}, json=host)
    if rsp.status_code != 204:
        print(
            f"{str(datetime.now())[:-3]}: Error posting to /hosts, response: {rsp.status_code}, {rsp.content}"
        )
        print(f" !!!  Unsuccessful attempt to update host status via REST API: {host['hostname']}")
    else:
        print(f" Successfully updated host status via REST API: {host['hostname']}")


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\nExiting host-portscan")
        exit()