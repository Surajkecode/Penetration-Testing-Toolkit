import scapy.all as scapy

def sniff_packets(interface):
    scapy.sniff(iface=interface, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        print(f"Packet: {ip_src} -> {ip_dst}")

if __name__ == "__main__":
    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    print("Starting packet sniffing...")
    sniff_packets(interface)
