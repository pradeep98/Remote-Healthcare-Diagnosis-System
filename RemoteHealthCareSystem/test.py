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

db = firebase.database()

data = {
    "name": "Mortimer 'Morty' Smith"
}

results = db.child("users/"+user['localId']).push(data)
