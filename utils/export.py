import json
import os

def export_results(devices, alerts):
    os.makedirs("output", exist_ok=True)

    with open("output/devices.json", "w") as f:
        json.dump(devices, f, indent=4)

    with open("output/alerts.txt", "w") as f:
        for alert in alerts:
            f.write(alert + "\n")

