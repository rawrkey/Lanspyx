from scapy.all import ARP, Ether, srp
import socket

def arp_scan(ip_range="192.168.1.0/24"):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "hostname": get_hostname(received.psrc),
            "ttl": 64  # default fallback, real TTL comes from ping if needed
        })

    return devices

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"

