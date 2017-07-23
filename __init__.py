from flask import Flask, request
from user import User
from problem import Problem
import db

app = Flask(__name__)
@app.route("/task_login",methods=['POST','GET'])
def login():
	print "inside login"
	if request.method=='GET':
		return "dosnt support this platform"
	if request.method=='POST':
		if request.is_json:
			Username=request.get_json()['Username']
			Password = request.get_json()['Password']
			Email= request.get_json()['Email']
			user = User (Username = Username , Password=Password , Email=Email)
			result = db.signup(user)
			if result==False:
				reply = user.to_json()
			else:
				reply = "[ \"dosnt exist\"]"
		else:
			reply = "only supports json"
	print reply
	return reply

@app.route("/", methods=['POST', 'GET'])
def signUp():
	print "inside sign up"

	if request.method == 'GET':
		return "doesnt support this platform "
	if request.method == 'POST':
		if request.is_json:
			Username = request.get_json()['username']
			Password = request.get_json()['password']
			Email = request.get_json()['email']
			
			user = User (Username = Username, Password=Password ,Email=Email)
			
			result = db.signup(user)
			
			if result==True:
				reply = user.to_json()
			else:
				reply = "[ \"already taken\"]"

		else:
			reply = "only supports json"
	print reply
	return reply

@app.route("/post_prob",methods=['POST','GET'])
def post_prob():
	if request.method == 'GET':
		return "dosnt support this platform "
	if request.method == 'POST':
		if request.is_json:
			problem_rebly = request.get_json()['prob_rebly']
			problem_picture = request.get_json()['prob_picture']
			problem_geolocation = request.get_json()['prob_geolocation']

			problem = Problem (problem_rebly=problem_rebly , problem_picture=probelm_picture ,
			problem_geolocation=probelm_geolocation)
			
			result = db.post_problem(problem)

			if result==True:
				reply = problem.to_posts()
			else:
				reply = "[ \"alredy taken\"]"

		else:
			reply = "only supports json"
	print reply
	return reply

if __name__ == '__main__':
	app.run(host="0.0.0.0")