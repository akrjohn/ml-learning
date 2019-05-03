class Movie(object):

	def __init__(self, name, image, url):
		self.name = name
		self.image = image
		self.url = url

	def toString(self):
		s = self.name , self.image, self.url
		return s

	def toJson(self):
			return {
				'name': self.name,
				'image': self.image,
				'url': self.url
			}	