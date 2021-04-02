import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import subprocess
from time import time

from hosts_common import discovery, get_hosts


parser = argparse.ArgumentParser(description="Threadpool example")
parser.add_argument("-poolsize", default=10, help="Size of the threadpool")
args = parser.parse_args()
threadpool_size = int(args.poolsize)


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


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\nExiting host-monitor")
        exit()
