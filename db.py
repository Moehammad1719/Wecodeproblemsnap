import dataset
from user import User
from problem import Problem


db = dataset.connect('sqlite:///database')

def signup(user):
	table = db['users']
	print "ALL USERS"
	check_exest = table.find_one(Username=user.Username)	
	print check_exest
	if check_exest != None:
		print "check_exest is true"
		return False
	else:
		print "check_exest is false"
		table.insert(dict(Username=user.Username,Password=user.Password,Email=user.Email))
		return True

def post_prob(problem):
	table = db['problem']
	check_exest = table.find_one(problem_Rebly=problem.Rebly ,
	problem_Picture=problem.Picture,
	problem_Geolocation=problem.Geolocation)	
	print check_exest
	if check_exest != None:
		print "check_exest is true"
		return True
	else:
		print "check_exest is false"
		table.insert(dict(problem_Rebly=problem.Rebly ,
		problem_Picture=problem.Picture,
		problem_Geolocation=problem.Geolocation))
		return True

