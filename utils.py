import networkx as nx
import matplotlib.pyplot as plt

"""
    draw the original graph.
"""
def draw_the_graph(graph: nx.graph.Graph, index: int, figure_num: int): 

    #adjust the graph with shell layout
    pos = nx.shell_layout(graph)
    
    #grab weights of all edges
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    
    #specify the figure number
    plt.figure(figure_num)

    #draw the graph itself
    nx.draw_networkx(graph, pos=pos, with_labels=True, font_color='red', node_color='yellow')

    #add weights of edges onto the graph
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels)
    
    plt.title(f'problem {index} original graph')
    #save the graph picture
    plt.savefig(f'test_graphs/problem_{index}/graph.png')

"""
    draw the minimum spanning tree.
"""
def draw_the_MST(MST: nx.graph.Graph, index: int, figure_num: int): 

    #adjust the graph with shell layout
    pos = nx.shell_layout(MST)
    
    #grab weights of all edges 
    edge_labels = nx.get_edge_attributes(MST, 'weight')
    
    #specify the figure number
    plt.figure(figure_num)

    #draw the tree itself
    nx.draw_networkx(MST, pos=pos, with_labels=True, font_color='red', node_color='yellow')
    
    #add weights of edges onto the tree
    nx.draw_networkx_edge_labels(MST, pos=pos, edge_labels=edge_labels)

    plt.title(f'problem {index} Kruskal MST solution')
    
    #save the graph picture
    plt.savefig(f'test_graphs/problem_{index}/MST.png')
