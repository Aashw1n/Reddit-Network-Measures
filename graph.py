
import networkx as nx
import matplotlib.pyplot as plt
import string
import json
import glob

g = nx.Graph()   #our graph
g.add_node("r/funny")  #root node representing r/funny

filenames= glob.glob("data/*.json") #getting all files from data

if __name__ == "__main__":
    for files in filenames:
        g.add_node(files)
        g.add_edge("r/funny",files)                        #adding nodes and edges
        subreddits = []                                    #Networkx automatically takes care of repeating nodes
        with open(files,'r') as f:
            subreddits=json.load(f)
        for contents in subreddits:
            try:
                g.add_node(contents[0])
                g.add_edge(files,contents[0])
            except IndexError:
                print('')
    


    nx.draw(g,with_labels=False,node_size=20)
    plt.show()


