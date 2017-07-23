class Problem:
	Rebly= ""
	Picture= ""
	Geolocation= ""
	def __init__(self, Rebly , Picture , Geolocation):
		self.Rebly = problem
		self.Picture = picture
		self.Geolocation = geolocation

	def to_json(self):
		json = "{"
		json += "\"rebly\" :" + unicode(self.Rebly) + ","
		json += "\"picture\" :" + unicode(self.Picture) + ","
		json += "\"geolocation\" :" + unicode(self.Geolocation)
		json += "}"
		return json 