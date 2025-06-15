def fingerprint_os(ttl):
    if ttl >= 128:
        return "Windows"
    elif ttl >= 64:
        return "Linux/Unix"
    elif ttl >= 255:
        return "Cisco/Network Device"
    else:
        return "Unknown"

