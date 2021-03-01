import scapy.all as scapy
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, ICMP, TCP


# SNIFF TRAFFIC
print("SNIFFING 10 FRAMES")
print("=" * 80)
capture = scapy.sniff(iface="eth0", count=10)
print(capture.nsummary(), end="\n\n")

# SNIFF DNS TRAFFIC
print("SNIFFING 10 DNS FRAMES")
print("=" * 80)
capture = scapy.sniff(iface="eth0", filter="udp port 53", count=10)
print(capture.nsummary(), end="\n\n")

# SNIFF DNS AND PRINT PACKET DATA
print("SNIFFING 10 DNS FRAMES AND PRINTING PACKET DATA")
print("=" * 80)
capture = scapy.sniff(iface="eth0", filter="udp port 53", count=10)

for packet in capture:
    print(packet.show())

print()

# SNIFF AND HANDLE PACKETS AS THEY ARRIVE

# -- CALLBACK FUNCTION
def print_packet(packet):
    print(f"     {packet.summary()}")


print("SNIFFING 10 HTTPS FRAMES AND PRINTING AS THEY ARRIVE")
print("=" * 80)
scapy.sniff(iface="eth0", prn=print_packet, filter="tcp port https", count=10)
print()

# SNIFF AND HANDLE PACKETS AS THEY ARRIVE USING LAMBDA
print("SNIFFING 10 HTTPS FRAMES AND PRINTING AS THEY ARRIVE USING LAMBDA")
print("=" * 80)
scapy.sniff(iface="eth0", prn=lambda pkt: print(f"lambda     {pkt.summary()}"), filter="tcp port https", count=10)
print()

# DISCOVER HOSTS ON SUBNET USING MANUAL ARP
print("DISCOVERING HOSTS VIA ARP USING SCAPY.SRP")
print("=" * 80)
subnet = input("Enter subnet x.x.x.x/xx: ")
ans, unans = scapy.srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=subnet), timeout=2)
ans.summary()
print()

# DISCOVERING HOSTS ON SUBNET USING ARPING FUNCTION
print("DISCOVERING HOSTS VIA ARP USING SCAPY.ARPING")
print("=" * 80)
ans, unans = scapy.arping(subnet)

for result in ans.res:
    print(f"---> IP addrss discovered: {result[0].payload.pdst}")

print()

# # DISCOVERING HOSTS ON SUBNET USING ICMP PING
# print("DISCOVERING HOSTS VIA ICMP USING SCAPY.SR")
# print("=" * 80)
# ips = input("Enter IP range x.x.x.x-x: ")
# ans, unans = scapy.sr(IP(dst=ips)/ICMP(), timeout=2)
# ans.summary()
# print()

# TCP PORT SCAN
print("RUNNING A TCP PORT SCAN")
print("=" * 80)
while True:
    ip = input("Enter IP address: ")

    if not ip:
        print("Exiting")
        break

    ans, unans = scapy.sr(IP(dst=ip)/TCP(flags="S", sport=666, dport=(1, 1024)), timeout=10)

    for answer in ans:
        print(f"---> open port: {answer[0].summary()}")

    print()

    print(f"----- Open port totals: {len(ans)}/1024")
