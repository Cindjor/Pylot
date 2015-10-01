
from system.core.controller import *
import json
class Whats(Controller):
	def __init__(self, action):
		super(Whats, self).__init__(action)

	def index(self):  
		categories=self.getValueCategory()
		print categories
		return self.load_view('index.html',categories=categories)

	def getValueCategory(self):
		category=[]
		url = "http://api.eventful.com/json/categories/list?app_key=jk5zHMNmqkqjb6jS"
		res = json.loads(requests.get(url).content)

		for dictvalue in res["category"]:
			category.append({"id": dictvalue["id"], "name":dictvalue["name"].replace('&amp;','&')})
		
		return category
	def getallgeocode(self):
		url="http://api.eventful.com/json/events/search?app_key=jk5zHMNmqkqjb6jS&location=san%20jose,%20CA"
		res = requests.get(url).content
		return res

