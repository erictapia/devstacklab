from pprint import pprint

import nmap


def discovered_host(found_host, scan_result):
    if scan_result["nmap"]["scanstats"]["uphosts"] == "1":
        print(f"--- --- found host: {found_host} scan: {scan_result['nmap']['scanstats']}")


if __name__ == "__main__":
    # Reference: nmap.org/book/man.html
    nm = nmap.PortScanner()
    while ip := input("Input IP address to scan: "):

        print(f"\n--- Beginning scan of {ip}")
        # 22-1024 are the ports
        output = nm.scan(ip, "22-1024", arguments="-sS -sU -O --host-time 600")
        print(f"--- --- command: {nm.command_line()}")

        print("----- nmap scan output -----")
        pprint(output)

        try:
            pprint(nm[ip].all_tcp())
            pprint(nm[ip].all_udp())
            pprint(nm[ip].all_ip())

        except KeyError as e:
            print(f"   ---> failed to get scan results for {ip}")

        print(f"--- end scan of {ip}")

    print("\nExiting nmap scanner\n\n")

    print("Scanning all hosts in subnet using port 22")

    if( subnet := input("Enter subnet to scan, x.x.x.x/x: ")):
        nm.scan(subnet, arguments="-p 22 --open")

        for host in nm.all_hosts():
            print(f"--- --- {host}")

        print("\nScanning all hosts in subnet using port 80")
        nm.scan(subnet, arguments="-p 80 --open")

        for host in nm.all_hosts():
            print(f"--- --- {host}")

        print("\nScanning all hosts in subnet using ICMP")
        nm.scan(subnet, arguments="-p 80 -PE")

        for host in nm.all_hosts():
            print(f"--- --- {host}")

    nma = nmap.PortScannerAsync()
    print("\nScanning all hosts in subnet using ICMP with callback")
    nma.scan(subnet, arguments="-PE --host-timeout 50ms", callback=discovered_host)

    while nma.still_scanning():
        nma.wait(5)
