from py2neo import Graph, Node, Relationship, NodeMatcher
from Relations import Relations

class DataBase():

	def __init__(self, uri, user, password):
		self.graph = Graph(uri, auth={user, password})

	def createUser(self, name, username, emial, password):
		self.graph.create(Node("Person", name=name, username=username, emial=emial, password=password))

	def create2WayRelationship(self, first_username, second_username):
		matcher = NodeMatcher(self.graph)
		first_user = matcher.match("Person", username=first_username).first()
		second_user = matcher.match("Person", username=second_username).first()
		self.graph.create(Relationship(first_user, Relations.isFriend, second_user))

	def getUserByPassword(self, username, password):
		matcher = NodeMatcher(self.graph)
		user = matcher.match("Person", username=username, password=password).first()
		return user

	def getUser(self, **kwargs):
		matcher = NodeMatcher(self.graph)
		name = kwargs.get('name', None)
		username = kwargs.get('username', None)
		email = kwargs.get('email', None)

		if email is not None:
			return matcher.match("Person", email=email).first()
		if username is not None:
			return matcher.match("Person", username=username).first()
		if name is not None:
			return matcher.match("Person", name=name).first()

