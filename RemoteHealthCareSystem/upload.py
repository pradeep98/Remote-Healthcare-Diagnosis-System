import pyrebase
config = {
  "apiKey": "AIzaSyBOHdTKorMRZwLWqaXxnXPVFiQvIUBOXSU",
  "authDomain": "remotehealthcare-c1d18.firebaseapp.com",
  "databaseURL": "https://remotehealthcare-c1d18.firebaseio.com",
  "projectId": "remotehealthcare-c1d18",
  "storageBucket": "remotehealthcare-c1d18.appspot.com",
  "messagingSenderId": "295505897713",
  "appId": "1:295505897713:web:34fc17a8b1470cd59ae150",
  "measurementId": "G-GDGJN0SVYY"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

auth = firebase.auth()

email="lol100@lol.com"
password="lol100@lol.com"

user = auth.sign_in_with_email_and_password(email, password)

#results = db.child("users/"+user['localId']).push(data)



from datetime import datetime
times = datetime.timestamp(datetime.now())

# to get the key
child=db.child("users/"+user['localId']+"/data_test_1")
if(child.get().val()==None):
	db.child("users/"+user['localId']+"/data_test_1").push({"phone":"9050145521", 
									"age":"22",
									 "bmi":"20",
									 "dbp":"80", 
									 "sbp":"120", 
									 "email":"qwerty@gmail.com",
									 "fname":"Ashish",
									 "lname":"Patel", 
									 "glucose_level":"120" ,
									 "heart_rate":"80", 
									 "heart_attack":"NOOOOOOOOOOOOOOO",
									 "Time": times
									})
else:
	key=list(db.child("users/"+user['localId']+"/data_test_1").get().val().keys())[0]
	print(key)

	# to update data i the database
	db.child("users/"+user['localId']+"/data_test_1").push({"phone":"9050145521", 
												"age":22,
												 "bmi":19,
												 "dbp":72, 
												 "sbp":100, 
												 "email":"lol100@lol.com",
												 "fname":"Pradeep",
												 "lname":"Turan", 
												 "glucose_level":100 ,
												 "heart_rate":90, 
												 "heart_attack":"Nope",
												 "Time": times
												})


