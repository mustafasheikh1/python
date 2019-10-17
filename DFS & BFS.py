graph = {
	7: [5, 9],
	5: [2, 6],
	9: [8, 10],
	2: [],
	6: [],
	8: [],
	10: []
}

# graph = {
# 	7: [2,8,9],
# 	8: [2,5,6,7],
# 	2: [6,7,8,9],
# 	9: [2,3,7],
# 	5: [8],
# 	6: [2,3,8],
# 	3: [6,9]
# }

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
