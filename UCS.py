from queue import PriorityQueue

graph = {
	"/": [0, "A"],
	"A": [(494, "C"), (146, "O"), (140, "S")],
	"C": [(494, "A"), (146, "R"), (138, "P")],
	"O": [(146, "A"), (151, "S")],
	"S": [(99, "F"), (80, "R"), (140, "A"), (151, "O")],
	"R": [(80, "S"), (146, "C"), (97, "P")],
	"P": [(138, "C"), (97, "R"), (101, "B")],
	"F": [(99, "S"), (211, "R")],
	"B": [(211, "F"), (101, "P")]

}
print(graph)


def UCS(graph, start, goal):
	explored = []
	queue = PriorityQueue()
	queue.put(start)

	while not queue.empty():
		print("Stack : ", queue)
		t = queue.get()

		node = (t[0],t[1],t[2])
		print('test',node)
		print("Explored : ", explored)

		if node not in explored:
			explored.append(node)
			# print(node[1], goal)
			if node[2] is goal:
				break
			neighbours = graph[node[2]]
			for neighbour in neighbours:
				# print(neighbour[0])
				n = (neighbour[0],node[2], neighbour[1])
				queue.put(n)

	return explored

print("Final Output : ", (UCS(graph, ( 0, '/', "A"), "B")))