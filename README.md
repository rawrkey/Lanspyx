# 🔍 LANSpyX

**LANSpyX** is a powerful and advanced LAN threat mapper and analysis tool built for Kali Linux and other pentesting environments.

## 🚀 Features

- 🔎 **Active ARP Scan** to detect live hosts on LAN
- 🕵️‍♂️ **Passive Sniffing** mode using ARP packets
- 🧠 **OS Fingerprinting** using TTL analysis
- ⚠️ **Rogue Device Detection** via MAC OUI
- 🕸️ **ARP Spoof Detection**
- 🌐 **Network Visualization Graph** (via `matplotlib` + `networkx`)
- 📤 **Discord Alert Integration**
- 📁 Exports results as `JSON`, `TXT`, and `PNG` map


## 🧪 Usage

```bash
# Clone it
git clone https://github.com/kalpiy/lanspyx.git
cd lanspyx

# Install dependencies
pip install -r requirements.txt

# Run a scan
sudo python3 main.py --range 192.168.1.0/24 --graph

# Passive mode
sudo python3 main.py --passive

#   --range	Set target subnet (e.g., 192.168.0.0/24)
    --passive	Use passive sniffing instead of ARP scan
    --graph	Generate network map image
    --iface	Specify network interface (optional)
# Lanspyx
