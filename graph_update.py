import networkx as nx
import matplotlib.pyplot as plt
import string
import json
import glob
import os

G = nx.DiGraph()   #our graph

filenames= glob.glob("data/*.json") #getting all files from data

def add_node(name):
    G.add_node(f"r/{name}")

def add_edge(name_1, name_2, weight):
    G.add_edge(f"r/{name_1}", f"r/{name_2}", weight=weight)

def add_node_and_children(filename):
    base_name = os.path.basename(filename)
    base_node_name = os.path.splitext(base_name)[0]

    if not G.has_node(base_node_name):
        add_node(base_node_name)

    with open(filename, 'r') as f:
        child_nodes = json.load(f)
    for node_name, weight in child_nodes:

        if not G.has_node(node_name):
            add_node(node_name)
        add_edge(base_node_name, node_name, weight)


if __name__ == "__main__":
    for file in filenames:
        if file != "data/errors.json":
            add_node_and_children(file)

    nx.write_edgelist(G, "edgelist.gz")
    nx.draw(G,with_labels=False,node_size=20)
    plt.show()
