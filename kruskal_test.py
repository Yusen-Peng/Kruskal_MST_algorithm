import networkx as nx
from utils import draw_the_graph
from utils import draw_the_MST
from kruskal import kruskal_MST

#a global variable that keeps track of the number of test cases
test_case = 1

#a global variable that keeps track of the number of figures
figure_num = 1

"""
    graph for Problem 1.
"""
def graph_problem_1() -> nx.graph.Graph:
    graph = nx.Graph()
    
    #add all nodes
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')

    #add all edges
    graph.add_edge('A', 'B', weight=7)
    graph.add_edge('A', 'C', weight=6)
    graph.add_edge('A', 'E', weight=3)
    graph.add_edge('A', 'F', weight=1)

    graph.add_edge('B', 'C', weight=4)
    graph.add_edge('B', 'E', weight=5)
    
    graph.add_edge('C', 'D', weight=2)
    graph.add_edge('C', 'E', weight=5)

    graph.add_edge('D', 'E', weight=8)
    graph.add_edge('D', 'F', weight=5)

    graph.add_edge('E', 'F', weight=4)

    return graph

"""
    graph for problem 2.
"""
def graph_problem_2() -> nx.graph.Graph:
    graph = nx.Graph()
    
    #add all nodes
    graph.add_node('v1')
    graph.add_node('v2')
    graph.add_node('v3')
    graph.add_node('v4')
    graph.add_node('v5')
    graph.add_node('v6')

    #add all edges
    graph.add_edge('v1', 'v2', weight=1)
    graph.add_edge('v1', 'v3', weight=4)
    
    graph.add_edge('v2', 'v3', weight=6)
    graph.add_edge('v2', 'v4', weight=8)

    graph.add_edge('v3', 'v4', weight=2)
    graph.add_edge('v3', 'v5', weight=4)
    
    graph.add_edge('v4', 'v6', weight=3)
    graph.add_edge('v4', 'v5', weight=9)

    graph.add_edge('v5', 'v6', weight=5)

    return graph


"""
    graph for problem 3.
"""
def graph_problem_3() -> nx.graph.Graph:
    graph = nx.Graph()
    
    #add all nodes
    graph.add_node('v1')
    graph.add_node('v2')
    graph.add_node('v3')
    graph.add_node('v4')
    graph.add_node('v5')
    graph.add_node('v6')
    graph.add_node('v7')
    graph.add_node('v8')
    graph.add_node('v9')
    
    #add all edges
    graph.add_edge('v1', 'v2', weight=2)
    graph.add_edge('v1', 'v6', weight=3)
    
    graph.add_edge('v2', 'v3', weight=7)
    graph.add_edge('v2', 'v4', weight=5)

    graph.add_edge('v3', 'v5', weight=9)
    graph.add_edge('v3', 'v9', weight=6)
    
    graph.add_edge('v4', 'v5', weight=5)
    graph.add_edge('v4', 'v7', weight=3)
    graph.add_edge('v4', 'v6', weight=4)

    graph.add_edge('v5', 'v8', weight=6)
    graph.add_edge('v5', 'v9', weight=8)
    
    graph.add_edge('v6', 'v7', weight=1)

    graph.add_edge('v7', 'v8', weight=4)

    graph.add_edge('v8', 'v9', weight=9)

    return graph


if __name__ == "__main__":

    """
        first test case (from homework 24, Problem 5)
    """
    original_graph = graph_problem_1()
    draw_the_graph(original_graph, test_case, figure_num)
    
    #update the figure number
    figure_num += 1

    our_MST = kruskal_MST(original_graph)
    draw_the_MST(our_MST, test_case, figure_num)

    #update the figure number
    figure_num += 1

    test_case += 1

    """        
        second test case (from homework 26 problem 4)
    """
    original_graph = graph_problem_2()
    draw_the_graph(original_graph, test_case, figure_num)
    
    #update the figure number
    figure_num += 1

    our_MST = kruskal_MST(original_graph)
    draw_the_MST(our_MST, test_case, figure_num)

    #update the figure number
    figure_num += 1

    test_case += 1

    """        
        third test case (from lecture notes )
    """
    original_graph = graph_problem_3()
    draw_the_graph(original_graph, test_case, figure_num)
    
    #update the figure number
    figure_num += 1

    our_MST = kruskal_MST(original_graph)
    draw_the_MST(our_MST, test_case, figure_num)

    #update the figure number
    figure_num += 1

    test_case += 1
