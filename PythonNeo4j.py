from py2neo import Graph, Node, Relationship, NodeMatcher

# Command for Integration of Neo4j in Python
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))

# Delete all existing data in graph
graph.delete_all()

# Using py2neo built in methods
# Creating Nodes
node1 = Node("Animal", name="Cat")
graph.create(node1)
node2 = Node("Object", name="Mat")
graph.create(node2)

# Creating Relationship
relationship = Relationship(node1, "IS_SITTING_ON", node2)
graph.create(relationship)

# Creating Node matcher object
matcher = NodeMatcher(graph)
# Find Node with name Mat and display it
node = matcher.match("Object", name="Mat").first()
print(node)

# Using neo4j cypher in python with py2neo Version 4
# Creating Nodes
graph.run("CREATE (n:Person {name: 'Mahmood'})")
graph.run("CREATE (n:Person {name: 'Ali'})")

# Creating Relationship
graph.run("MATCH (p1:Person {name: 'Mahmood'})"
          "MATCH (p2:Person {name: 'Ali'})"
          "CREATE (p1)-[:IS_FRIENDS_WITH]->(p2)")

# Creating Nodes and Relationship in single cypher
graph.run("CREATE (p1:Person {name: 'Fahad', age: 20}),"
          "(p2:Person {name: 'Mahad', age: 18}),"
          "(p1)-[:BROTHER_OF]->(p2)")

# Find All nodes and display them in Table form
print("All Nodes in Graph")
print(graph.run("MATCH(n) RETURN n").to_table())
