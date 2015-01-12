
import os
from pymongo import MongoClient

class MongoConnector:

	"""
	Class to handle MongoDB conneciton
	Should be initiated every time you want to insert into or pull from MongoDB
	"""


	def __init__(self):
		"""
		Pulling mongo URL from Enviormental vars
		Connecting to default database
		"""
		client 	 = MongoClient(os.environ["MONGOURL"]) 
		self.db  = client.get_default_database()

	def insertIntoMongo(self, collection, insertDict):
		"""
		Method to insert a given dictionary into a collection
		"""
		self.db[collection].insert(insertDict)

	def pullFromMongo(self, collection, paramDict):
		"""
		method to query a given collection with specified paramaters and return the result
		"""
		return self.db[collection].find(paramDict)
