import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="LANSpyX v2 Advanced LAN Threat Mapper")
    parser.add_argument("--range", help="IP range (default: 192.168.1.0/24)", default="192.168.1.0/24")
    parser.add_argument("--passive", help="Enable passive mode", action="store_true")
    parser.add_argument("--graph", help="Generate visual network map", action="store_true")
    return parser.parse_args()

