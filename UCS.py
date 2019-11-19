from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.graph = {  # cost, Parent, Node
            "A": [(146, ("A", "O")), (140, ("A", "S")), (494, ("A", "C"))],
            "C": [(494, ("C", "A")), (146, ("C", "R")), (138, ("C", "P"))],
            "S": [(80, ("S", "R")), (140, ("S", "A")), (99, ("S", "F")),(151, ("S", "O"))],
            "O": [(146, ("O", "A")), (151, ("O", "S"))],
            "R": [(97, ("R", "P")), (80, ("R", "S")), (146, ("R", "C"))],
            "F": [(99, ("F", "S")), (211, ("F", "B"))],
            "P": [(138, ("P", "C")), (97, ("P", "R")), (101, ("P", "B"))],
            "B": [(211, ("B", "F")), (101, ("B", "P"))]
        }
        self.edges = {}
        self.weights = {}
        self.populate_edges()
        self.populate_weight()

    def neighbours(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node, to_node)]

    # define functions for edges and weights
    def populate_edges(self):
        for key in self.graph:
            neighbours = []
            for each_tuple in self.graph[key]:
                neighbours.append(each_tuple[1][1])
            self.edges[key] = neighbours

    def populate_weight(self):
        for key in self.graph:
            neighbours = self.graph[key]
            for each_tuple in neighbours:
                self.weights[each_tuple[1]] = each_tuple[0]


def ucs(graph, start, goal):
    visited = []
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)

            if node == goal:
                break
            for i in graph.neighbours(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    print(total_cost, i)
                    queue.put((total_cost, i))
            print('_____________________')
    return visited


print("Path: ", ucs(Graph(), "A", "B"))
