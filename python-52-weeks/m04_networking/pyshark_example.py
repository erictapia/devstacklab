import pyshark


def print_packet_summary(packet):
    print("     ", str(packet)[:120])


if __name__ == "__main__":
    ##### CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
    print("----- PACKET SUMMARIES -----")
    capture = pyshark.LiveCapture(interface="eth0", only_summaries=True)
    capture.sniff(packet_count=20)

    for packet in capture:
        print(f"     {packet}")

    ##### CAPTURE DNS AND PRINT PACKETS
    print()
    print("----- DNS PACKET SUMMARIES -----")
    capture = pyshark.LiveCapture(interface="eth0", only_summaries=True, bpf_filter="udp port 53")
    capture.sniff(packet_count=20)

    for packet in capture:
        print(f"     {packet}")

    ##### CAPTURE AND PRINT COMPLETE PACKETS
    print()
    print("----- COMPLETE PACKETS -----")
    capture = pyshark.LiveCapture(interface="eth0")
    capture.sniff(packet_count=20)

    for packet in capture:
        print(f"     {packet}")

    ##### CAPTURE AND HANDLE HTTPS PACKETS AS THEY ARRIVE
    print()
    print("----- PACKETS AS THEY ARRIVE -----")
    capture = pyshark.LiveCapture(interface="eth0", only_summaries=True, bpf_filter="tcp port https")
    capture.apply_on_packets(print_packet_summary, packet_count=10)

    ##### CAPTURE AND HANDLE PACKETS AS THEY ARRIVE USING LAMBDA
    print()
    print("----- PRINT PACKETS AS THEY ARRIVE VIA LAMBDA -----")
    capture = pyshark.LiveCapture(interface="eth0", only_summaries=True, bpf_filter="tcp port https")
    capture.apply_on_packets(lambda pkt: print("lambda   ", str(pkt)[:114]), packet_count=10)

    ##### USE SNIFF CONTINOUSLY TO CAPTURE PACKETS AND HANDLE AS THEY ARRIVE
    print()
    print("----- PRINT PACKETS AS THEY ARRIVE WITH SNIFF CONTINUOUSLY")
    capture = pyshark.LiveCapture(interface="eth0", only_summaries=True, bpf_filter="tcp port https")
    for packet in capture.sniff_continuously(packet_count=10):
        print_packet_summary(packet)

    ##### ALLOW USER TO ENTER BPF FILTER
    print()
    print("----- INPUT AND USE BPF FILTER FROM USER -----")

    while bpf_filter:= input("Enter BPF filter: "):
        print(f"\n----- Capturing packets with BPF filter: {bpf_filter}")

        capture = pyshark.LiveCapture(interface="eth0", only_summaries=True, bpf_filter=bpf_filter)

        try:
            capture.apply_on_packets(print_packet_summary, packet_count=10)
        except KeyboardInterrupt as e:
            continue
