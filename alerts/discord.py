import requests

def send_discord_alert(message, webhook_url):
    data = {"content": message}
    try:
        requests.post(webhook_url, json=data)
    except Exception as e:
        print(f"[!] Discord alert failed: {e}")

