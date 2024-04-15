import networkx as nx
import matplotlib.pyplot as plt

######################## Kernel Kruskal's MST algorithm ########################

"""
    kruskal's minimum spanning tree algorithm.
"""
def kruskal_MST(graph: nx.graph.Graph) -> nx.graph.Graph:
    #initialize the minimum spanning tree
    our_MST = nx.Graph()
     
    #intialize all independent sets
    independent_sets = _sets_init(graph)

    #sorted all edges by weights
    sorted_edges = _edge_sort(graph)

    #iterate through all edges
    while len(sorted_edges) > 0:
        #retrieve one edge with the minimum weight
        edge = sorted_edges.pop(0)

        #unpack the edge information
        node_1, node_2, _ = edge
        weight = _retrieve_weight(edge) 

        #if two nodes are in two disjoint sets, we add the edge ot our MST
        if(_in_disjoint_sets(node_1, node_2, independent_sets)):
            set1 = _retrieve_set(node_1, independent_sets)
            set2 = _retrieve_set(node_2, independent_sets)

            #do set union work
            union_set = set1.union(set2)
            independent_sets.append(union_set)
            independent_sets.remove(set1)
            independent_sets.remove(set2)

            #keep building our MST 
            if not node_1 in our_MST:
                our_MST.add_node(node_1)
            if not node_2 in our_MST:
                our_MST.add_node(node_2)
            our_MST.add_edge(node_1, node_2, weight=weight)
    
    return our_MST

######################## a list of helper methods ##############################

"""
    initialize all independent sets.
"""
def _sets_init(graph: nx.graph.Graph) -> list:

    independent_sets = []

    for node in graph:
        single_set = set()
        single_set.add(node)   
        independent_sets.append(single_set)

    return independent_sets


"""
    retrieve the edge's weight (the sorting criteria function). 
"""
def _retrieve_weight(edge):

    #unpack edge information
    _, _, data = edge
    
    #return the edge's weight
    return data['weight']

"""
    sort all edges by weights in the ascending order.
"""
def _edge_sort(graph: nx.graph.Graph) -> list:

    #sort edges by weights in the ascending order
    # data=True: ensure that weights are also packed
    #key: a function of the sorting criteria 
    sorted_edges = sorted(graph.edges(data=True), key=_retrieve_weight) 
     
    return sorted_edges

"""
    check if two nodes are in disjoint sets.
"""
def _in_disjoint_sets(n1: str, n2: str, independent_sets: list[set]) -> bool:
    for independent_set in independent_sets:    
        #when we find node 1, we look up n2 in this particular set
        if n1 in independent_set:
            for element in independent_set:
                if n2 == element:
                    return False   #they are not disjoint
    return True

"""
    retrieve the independent set based on the given element
"""
def _retrieve_set(node: str, independent_sets: list[set]) -> set:
    for independent_set in independent_sets:
        #retrieve the set that contains the node we are looking for
        if node in independent_set: 
            return independent_set
    return set()
