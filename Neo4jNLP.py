from py2neo import Graph, Node, Relationship, NodeMatcher
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk

# Input Sentence
sentence = "Mahmood is friend of Ali."

# Tokenize sentence to words
words = word_tokenize(sentence)

# Convert words to POS_TAGS
tagged_words = pos_tag(words)
print(tagged_words)

# List for proper nouns, nouns, prepositions
proper_nouns = []
nouns = []
prepositions = []

# Traverse through tagged words to find proper nouns, nouns, prepositions
for each_tuple in tagged_words:
    if each_tuple[1] == "NNP":
        proper_nouns.append(each_tuple[0])
    elif each_tuple[1] == "NN":
        nouns.append(each_tuple[0])
    elif each_tuple[1] == "IN":
        prepositions.append(each_tuple[0])

print("Proper Nouns: ", proper_nouns)
print("Nouns: ", nouns)
print("Prepositions: ", prepositions)

# Command for Integration of Neo4j in Python
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))

# Delete all existing data in graph
graph.delete_all()

# Creating nodes using proper nouns list
for name in proper_nouns:
    node = Node("Person", name=name)
    graph.create(node)

# List of nodes
nodes = []

# Creating Node matcher object
matcher = NodeMatcher(graph)

# Matching Nodes from graph using proper nouns
for name in proper_nouns:
    node = matcher.match("Person", name=name).first()
    nodes.append(node)

# Creating relationship name in String form
relation = f"{nouns[0]}_{prepositions[0]}"

# Creating Relationship
relationship = Relationship(nodes[0], relation, nodes[1])
graph.create(relationship)
