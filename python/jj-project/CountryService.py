import csv
import json
from Country import Country

class CountryService(object):

	country_list = []
	json_list = []

	def __init__(self):
		self.__file2Map()
		self.__jsonCountryList()

	# private method to load the contry list once.
	def __file2Map(self):
		with open('countries.csv','r') as f:
			reader = csv.reader(f)
			for row in reader:
				self.country_list.append(Country(row[0],row[1],row[2],row[3]))


	def __jsonCountryList(self):
		i = 0
		#self.json_list = '{'
		for i in range(len(self.country_list)):
			print(self.country_list[i].toJson())
			#self.json_list = self.json_list + self.country_list[i].toJson()
			self.json_list.append(json.dumps(self.country_list[i].__dict__, sort_keys=True, indent=4))
		
		#self.json_list = self.json_list + '}'	

	def getJson(self):
		return json.dumps(self.json_list, sort_keys=True, indent=4)


	



