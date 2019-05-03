import json
from json import JSONEncoder

class News(object):
	"""docstring for ClassName"""
	def __init__(self, title, image, url, article_type, source):
		self.title = title
		self.image = image
		self.url = url
		self.article_type = article_type
		self.source = source
		self.description = ''

	def setDescription(self, description):
		self.description = description
		
	def toJson(self):
			return json.dumps(self.__dict__)


class MyEncoder(JSONEncoder):
				"""docstring for ClassName"""
				def default(self, o):
					return o.__dict__  
								
		