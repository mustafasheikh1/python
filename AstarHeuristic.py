from math import floor, sqrt
from queue import PriorityQueue

# A Star Algorithm with calculating Heuristic values using node coordinates


class Graph:
    def __init__(self):

        # Graph data structure from GeeksforGeeks A star video
        self.graph = {  # cost, Parent, Node
            "A": [(6, ("A", "B")), (3, ("A", "F"))],
            "B": [(3, ("B", "C")), (2, ("B", "D")), (6, ("B", "A"))],
            "F": [(1, ("F", "G")), (7, ("F", "H")), (3, ("F", "A"))],
            "C": [(1, ("C", "D")), (5, ("C", "E")), (3, ("C", "B"))],
            "D": [(1, ("D", "C")), (8, ("D", "E")), (2, ("D", "B"))],
            "G": [(3, ("G", "I")), (1, ("G", "F"))],
            "H": [(2, ("H", "I")), (7, ("H", "F"))],
            "E": [(5, ("E", "C")), (8, ("E", "D")), (5, ("E", "I")), (5, ("E", "J"))],
            "I": [(3, ("I", "G")), (2, ("I", "H")), (5, ("I", "E")), (3, ("I", "J"))],
            "J": [(5, ("J", "E")), (3, ("J", "I"))],
        }

        # Coordinates for each node
        self.coordinates = {
            "A": (3, 10),
            "B": (0, 8),
            "F": (8, 9),
            "C": (1, 5),
            "D": (4, 7),
            "G": (6, 7),
            "H": (10, 7),
            "E": (4, 3),
            "I": (6, 2),
            "J": (5, 0)
        }

        self.edges = {}
        self.weights = {}
        self.populate_edges()
        self.populate_weight()

    # Method to find neighbours of a node
    def neighbours(self, node):
        return self.edges[node]

    # Method to calculate cost from one node to another
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
            for each_tuple in self.graph[key]:
                self.weights[each_tuple[1]] = each_tuple[0]

    # Method to calculate heuristic using current node and goal coordinates
    def calculate_heuristic(self, node, goal):

        # Node x1 and y1
        x1, y1 = self.coordinates[node]
        # Goal x2 and y2
        x2, y2 = self.coordinates[goal]

        # Using Euclidean Distance formula
        # h = square root((x2-x1)^2 + (y2-y1)^2)
        heuristic_value = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return floor(heuristic_value)


def a_star(graph, start, goal):
    visited = []
    queue = PriorityQueue()
    queue.put((0, start))

    # Run loop until queue is empty
    while queue:
        # Get Value from queue
        # cost = g(cost) of node
        # node = name of node
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)

            # If node is goal then break loop
            if node == goal:
                break
            # Second Queue to check which node has lowest f value
            f_queue = PriorityQueue()

            # Traverse through all neighbours of node
            for neighbour in graph.neighbours(node):
                # If neighbour already visited then
                if neighbour not in visited:
                    # Calculate g(cost)
                    g = cost + graph.get_cost(node, neighbour)
                    # Calculate h using calculate_heuristic
                    h = graph.calculate_heuristic(neighbour, goal)

                    # Calculate f which is f = g + h
                    f = g+h

                    # enqueue value of f with its respective node in f_queue
                    f_queue.put((f, neighbour))

            # get lowest value from f_queue and place it in queue
            queue.put(f_queue.get())
    return visited


print("Path: ", a_star(Graph(), "A", "J"))
