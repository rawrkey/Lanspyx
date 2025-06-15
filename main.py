from scanner.arp_scanner import arp_scan
from scanner.passive_sniffer import passive_sniff
from scanner.os_fingerprinter import fingerprint_os
from analyzer.rogue_detector import detect_rogue_devices
from analyzer.spoof_detector import detect_spoof_arp
from utils.export import export_results
from utils.visualizer import generate_graph
from utils.cli_parser import parse_args
from alerts.discord import send_discord_alert

def main():
    args = parse_args()
    devices = []

    print("🛰️ LANSpyX v2 Starting...\n")

    if args.passive:
        print("[*] Running passive sniffing mode...")
        devices = passive_sniff(timeout=30)
    else:
        print("[*] Running active ARP scan...")
        devices = arp_scan(args.range)

    print(f"[*] {len(devices)} device(s) discovered.")

    for dev in devices:
        dev["os_guess"] = fingerprint_os(dev.get("ttl", 64))  # fallback TTL
        dev["vendor"] = "Unknown"  # filled later if matched

    print("[*] Detecting rogue devices...")
    rogue_alerts = detect_rogue_devices(devices)

    print("[*] Checking for ARP spoofing signs...")
    spoof_alerts = detect_spoof_arp(devices)

    alerts = rogue_alerts + spoof_alerts

    print("[*] Exporting results...")
    export_results(devices, alerts)

    if args.graph:
        print("[*] Generating visual map...")
        generate_graph(devices)

    for alert in alerts:
        print(alert)
        send_discord_alert(alert, "https://discord.com/api/webhooks/your_webhook_url")

    print("\n✅ Scan complete. Results saved in `output/`.")

if __name__ == "__main__":
    main()

