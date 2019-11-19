import aiml

class Bot:
	def __init__(self):
		self.kernel = aiml.Kernel()
		self.kernel.learn("./aimlFiles/about.aiml")
		self.kernel.learn("./aimlFiles/anime.aiml")
		self.kernel.learn("./aimlFiles/botmaster.aiml")
		self.kernel.learn("./aimlFiles/common.aiml")
		self.kernel.learn("./aimlFiles/game.aiml")
		self.kernel.learn("./aimlFiles/greeting.aiml")
		self.kernel.learn("./aimlFiles/quries.aiml")
		self.kernel.learn("./aimlFiles/welcome.aiml")





