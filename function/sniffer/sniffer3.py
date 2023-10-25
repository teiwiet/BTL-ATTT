import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface,promiscuous=True)

sniff("eth0")