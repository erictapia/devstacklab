import asyncio
from datetime import datetime
import subprocess
from time import time


from hosts_common import discovery, get_hosts

async def ping_host_async(host):
    try:
        ping_cmd = ["ping", "-c3", "-n", "-i0.5", "-W2", host["ip_address"]]
        process = await asyncio.create_subprocess_exec(*ping_cmd, stdout=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()

        if "0 received" in stdout.decode():
            host["availability"] = False
            host["last_heard"] = str(datetime.now())[:-3]
            print(f" Host ping successful: {host['hostname']}")

        else:
            host["availability"] = True
            host["last_heard"] = str(datetime.now())[:-3]
            print(f" Host ping successful: {host['hostname']}")

    except subprocess.CalledProcessError:
        host["availability"] = False
        print(f" !!!  Host ping failed: {host['hostname']}")


async def run():
    hosts = get_hosts()
    print(f"\n---> Starting to ping {len(hosts)} hosts using asyncio")

    time_start = time()

    ping_hosts = [ping_host_async(host) for host in hosts.values()]
    await asyncio.gather(*ping_hosts)

    ping_with_asyncio_time = time() - time_start
    print(f"---> Completed pinging {len(hosts)} hosts using asyncio, time: {ping_with_asyncio_time:3f}")


if __name__ == "__main__":
    try:
        discovery()
        asyncio.run(run())

    except KeyboardInterrupt:
        print("\n\nExiting host-monitor")
        exit()