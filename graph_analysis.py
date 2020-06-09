import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('edgelist.gz')


def degree_distribution(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()
    
def page_rank(G):
    pr = nx.pagerank(G)
    subreddits = list(pr.keys())
    x_pos = [i for i, _ in enumerate(subreddits)]
    scores = list(pr.values())
    plt.bar(x_pos, scores, color='green')
    plt.show()
    
def closeness_centrality(G):
    cc = nx.closeness_centrality(G)
    subreddits = list(cc.keys())
    x_pos = [i for i, _ in enumerate(subreddits)]
    scores = list(cc.values())
    plt.bar(x_pos, scores, color='green')
    plt.show()
    
    
if __name__ == "__main__":
    degree_distribution(G)
    page_rank(G)
    closeness_centrality(G)