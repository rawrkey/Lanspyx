import networkx as nx
import matplotlib.pyplot as plt
import os

def generate_graph(devices):
    G = nx.Graph()

    for dev in devices:
        label = f"{dev['ip']}\n{dev['mac']}"
        G.add_node(label)

    nx.draw(G, with_labels=True, node_size=1600, node_color='skyblue', font_size=8)
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/network_map.png", bbox_inches="tight")
    print("[✓] Network map saved as output/network_map.png")

