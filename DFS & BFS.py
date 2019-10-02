graph = {
	7: [5, 9],
	5: [2, 6],
	9: [8, 10],
	2: [],
	6: [],
	8: [],
	10: []
}


def BFS(graph, start):
	explored = []
	queue = [start]

	while queue:
		node = queue.pop(0)
		if node not in explored:
			explored.append(node)
			neighbours = graph[node]

			for neighbour in neighbours:
				queue.append(neighbour)

	return explored


def DFS(graph, start):
	explored = []
	stack = [start]

	while stack:
		node = stack.pop()
		if node not in explored:
			explored.append(node)
			neighbours = graph[node]
			#important
			neighbours.reverse()

			for neighbour in neighbours:
				stack.append(neighbour)

	return explored


print("Final Result (BFS) :", BFS(graph, 7))
print("Final Result (DFS) :", DFS(graph, 7))
