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
import heartAttack

firebase = pyrebase.initialize_app(config)
db = firebase.database()

auth = firebase.auth()

#email="sample@gmail.com"
#password="sample12345"
password = input("Enter your Password : ")

user = auth.sign_in_with_email_and_password(heartAttack.temp3.email, password)


#results = db.child("users/"+user['localId']).push(data)



from datetime import datetime
times = datetime.timestamp(datetime.now())

# to get the key
child=db.child("users/"+user['localId']+"/data_test_1")
if(child.get().val()==None):
	db.child("users/"+user['localId']+"/data_test_1").push({"phone":heartAttack.temp3.phone, 
									"age":heartAttack.temp3.age,
									 "bmi":heartAttack.temp3.bmi,
									 "dbp":round(heartAttack.temp3.diaBP[0],2), 
									 "sbp":round(heartAttack.temp3.sysBp[0],2), 
									 "email":heartAttack.temp3.email,
									 "fname":heartAttack.temp3.fname,
									 "lname":heartAttack.temp3.lname, 
									 "glucose_level":round(heartAttack.temp3.gl,2),
									 "heart_rate":heartAttack.temp3.hr, 
									 "heart_attack":heartAttack.predicted,
									 "Time": times
									})
else:
	key=list(db.child("users/"+user['localId']+"/data_test_1").get().val().keys())[0]
	print(key)

	# to update data i the database
	db.child("users/"+user['localId']+"/data_test_1").push({"phone":heartAttack.temp3.phone, 
												"age":heartAttack.temp3.age,
												 "bmi":heartAttack.temp3.bmi,
												 "dbp":round(heartAttack.temp3.diaBP[0],2), 
												 "sbp":round(heartAttack.temp3.sysBp[0],2), 
												 "email":heartAttack.temp3.email,
												 "fname":heartAttack.temp3.fname,
												 "lname":heartAttack.temp3.lname, 
												 "glucose_level":round(heartAttack.temp3.gl,2),
												 "heart_rate":heartAttack.temp3.hr, 
												 "heart_attack":heartAttack.predicted,
												 "Time": times
												})


