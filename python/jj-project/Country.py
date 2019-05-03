class Country:
	def __init__(self,numeric_code,alpha_2_code,alpha_3_code,country_name):
		self.numeric_code = numeric_code
		self.alpha_2_code = alpha_2_code
		self.alpha_3_code = alpha_3_code
		self.country_name = country_name

	def toJson(self):
		s = {
			'numeric_code': self.numeric_code,
			'alpha_2_code': self.alpha_2_code,
			'alpha_3_code': self.alpha_3_code,
			'country_name': self.country_name
		}
		return s
				