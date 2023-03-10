table = {
    'A':[0,None],
    'B':[float('inf'),None],
    'C':[float('inf'),None],
    'D':[float('inf'),None],
    'E':[float('inf'),None],
    'F':[float('inf'),None],
}

Distance = 0
Previous_Node = 1
Infinity = float('inf')

def get_shortest_distance(table, vertex):
    shortest_distance = table[vertex][Distance]
    return shortest_distance

def set_shortest_distance(table, vertex, new_distance):
    table[vertex][Distance]=new_distance

def set_previous_node(table, vertex, previous_node):
    table[vertex][Previous_Node]=previous_node

def get_distance(graph, first_vertex, second_vertex):
    return graph[first_vertex][second_vertex]

def get_next_node(table, visited_node):
    unvisited_nodes = list(set(table.keys()).difference(set(visited_node)))
    assumed_min = table[unvisited_nodes[0]][Distance]
    min_vertex = unvisited_nodes[0]
    for node in unvisited_nodes:
        if table[node][Distance]<assumed_min:
            assumed_min=table[node][Distance]
            min_vertex=node

    return min_vertex