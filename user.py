class User:
	Username= ""
	Password= ""
	Email= ""
	def __init__(self, Username , Password , Email):
		self.Username = Username 
		self.Password = Password
		self.Email = Email 

	def to_json(self):
		json = "{"
		json += "\"username\" :\"" + unicode(self.Username) + "\","
		json += "\"password\" :\"" + unicode(self.Password) + "\","
		json += "\"email\" :\"" + unicode(self.Email) + "\""
		json += "}"
		return json 