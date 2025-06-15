from scapy.all import sniff, ARP

def passive_sniff(timeout=30):
    print(f"[*] Sniffing ARP packets for {timeout}s...")

    devices = {}

    def handle(pkt):
        if ARP in pkt and pkt[ARP].op in (1, 2):
            ip = pkt[ARP].psrc
            mac = pkt[ARP].hwsrc
            if ip not in devices:
                devices[ip] = mac

    sniff(filter="arp", prn=handle, timeout=timeout, store=False)

    return [{"ip": ip, "mac": mac, "hostname": "Unknown", "ttl": 64} for ip, mac in devices.items()]

