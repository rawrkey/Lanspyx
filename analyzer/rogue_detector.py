KNOWN_OUIS = {
    "00:1A:2B": "Cisco",
    "F8:27:93": "Apple",
    "3C:5A:B4": "TP-Link",
    "00:0C:29": "VMware",
    "00:50:56": "VMware",
    "40:8D:5C": "Realtek"
}

def detect_rogue_devices(devices):
    alerts = []

    for dev in devices:
        mac = dev["mac"].upper()
        oui = mac[:8]

        if oui not in KNOWN_OUIS:
            alerts.append(f"[ROGUE] Unknown MAC OUI: {mac} ({dev['ip']})")
        else:
            dev["vendor"] = KNOWN_OUIS[oui]

    return alerts

