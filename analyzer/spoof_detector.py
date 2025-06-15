from collections import defaultdict

def detect_spoof_arp(devices):
    ip_mac_map = defaultdict(set)

    for dev in devices:
        ip = dev["ip"]
        mac = dev["mac"]
        ip_mac_map[ip].add(mac)

    alerts = []
    for ip, macs in ip_mac_map.items():
        if len(macs) > 1:
            alerts.append(f"[SPOOF ALERT] {ip} maps to multiple MACs: {macs}")

    return alerts

