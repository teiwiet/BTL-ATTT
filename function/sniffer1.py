import scapy.all as scapy
from scapy.layers.http import HTTPRequest
from colorama import init,Fore
init()
GREEN = Fore.GREEN
RED= Fore.RED
RESET = Fore.RESET

def sniffer(iface):
    scapy.sniff(filter="port 80",iface=iface,store=False,prn=process_packet)
def process_packet(packet):
    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].path.decode()
        ip = packet[ip].src
        method = packet[HTTPRequest].Method.decode()

        print (f" \n { GREEN } [+] { ip } Requested { url } with {method }{ RESET } " )


if __name__== "__main__" :
    import argparse
    parser = argparse.ArgumentParser ( description = "HTTP Packet Sniffer, this is useful when you're a man in the middle.")
    parser.add_argument ( "-i" , "--iface" , help = "Interface touse, default is scapy's default interface" )
    parser.add_argument ( "--show-raw" , dest = "show_raw" ,action = "store_true" , help = "Whether to print POST raw data,such as passwords, search queries, etc." )

    args = parser.parse_args()
    print(args)
    iface = args.iface
    show_raw = args.show_raw

    sniffer(iface=iface)