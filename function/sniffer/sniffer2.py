from scapy.all import *
from scapy.layers.http import HTTPRequest 
def sniff_packets(iface):
    sniff(filter="port 80", prn=process_packet, iface=iface, store=False)
def process_packet(packet):
    print(packet.summary)
    # if packet.haslayer(HTTPRequest):
    #     url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
    #     ip = packet[IP].src
    #     method = packet[HTTPRequest].Method.decode()
    #     print(f"\n[+] {ip} Requested {url} with {method}")
    #     if show_raw and packet.haslayer(Raw) and method == "GET":
    #         print(f"\n[*] Some useful Raw data: {packet[Raw].load}")
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="HTTP Packet Sniffer, this is useful when you're a man in the middle." \
                                                 + "It is suggested that you run arp spoof before you use this script, otherwise it'll sniff your personal packets")
    parser.add_argument("-i", "--iface", help="Interface to use, default is scapy's default interface")
    parser.add_argument("--show-raw", dest="show_raw", action="store_true", help="Whether to print POST raw data, such as passwords, search queries, etc.")
    args = parser.parse_args()
    iface = args.iface
    show_raw = args.show_raw
    sniff_packets("wlan0")