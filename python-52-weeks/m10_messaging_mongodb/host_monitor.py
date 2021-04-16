import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import socket
import subprocess
from time import time

import requests
import scapy.all as scapy


BASEURL = "http://127.0.0.1:5000"
# DISCOVERY_INTERVAL = 300
DISCOVERY_SUBNET = input("Enter subnet to be discovered x.x.x.x/xx: ")
# MONITOR_INTERVAL = 15
# PORTSCAN_INTERVAL = 3600

parser = argparse.ArgumentParser(description="Threadpool example")
parser.add_argument("-poolsize", default=10, help="Size of the threadpool")
args = parser.parse_args()
threadpool_size = int(args.poolsize)


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


def get_hosts():
    print("\n\n----> Retrieving hosts ...", end="")

    response = requests.get(f"{BASEURL}/hosts")

    if response.status_code != 200:
        print(f" !!! Failed to retrieve hosts from server: {response.reason}")
        return {}

    print(" Hosts successfully retrieve")
    return response.json()


def ping_host(host):

    try:
        subprocess.check_output(
            ["ping", "-c3", "-n", "-i0.5", "-W2", host["ip_address"]]
        )
        host["availability"] = True
        host["last_heard"] = str(datetime.now())[:-3]
        print(f" Host ping successful: {host['hostname']}")

    except subprocess.CalledProcessError:
        host["availability"] = False
        print(f" !!!  Host ping failed: {host['hostname']}")


def run():
    discovery()

    hosts = get_hosts()
    print(f"\n---> Starting to ping {len(hosts)} hosts using threadpool")

    time_start = time()
    
    with ThreadPoolExecutor(max_workers=threadpool_size) as executor:
        executor.map(ping_host, hosts.values())
    
    ping_with_threadpool_time = time() - time_start
    print(f"---> Completed pinging {len(hosts)} hosts using threadpool, time:", ping_with_threadpool_time)


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


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\nExiting host-monitor")
        exit()
