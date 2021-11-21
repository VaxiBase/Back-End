from flask import Flask
import pyrebase
from main import Api_data

p1 = Api_data()
app = Flask(__name__)

firebaseconfig = {
    "apiKey": "AIzaSyB-5Z1fz9rsfVhxCLcSQ1n4hfFdBhYmW1c",
    "authDomain": "vaxibase.firebaseapp.com",
    "databaseURL": "https://vaxibase-default-rtdb.firebaseio.com",
    "projectId": "vaxibase",
    "storageBucket": "vaxibase.appspot.com",
    "messagingSenderId": "725075045659",
    "appId": "1:725075045659:web:459aa09befdc1ae2f5b7be"}

firebase = pyrebase.initialize_app(firebaseconfig)
db = firebase.database()

@app.route('/')
def index():

    data = db.child('province_data').get()
    return data.val()

@app.route('/ab/')
def ab():

    data = db.child('province_data').child('AB').get()
    return data.val()

@app.route('/bc/')
def bc():

    data = db.child('province_data').child('BC').get()
    return data.val()

@app.route('/mb/')
def mb():

    data = db.child('province_data').child('MB').get()
    return data.val()

@app.route('/nb/')
def nb():

    data = db.child('province_data').child('NB').get()
    return data.val()

@app.route('/nl/')
def nl():

    data = db.child('province_data').child('NL').get()
    return data.val()

@app.route('/ns/')
def ns():

    data = db.child('province_data').child('NS').get()
    return data.val()

@app.route('/nt/')
def nt():

    data = db.child('province_data').child('NT').get()
    return data.val()

@app.route('/nu/')
def nu():

    data = db.child('province_data').child('NU').get()
    return data.val()

@app.route('/on/')
def on():

    data = db.child('province_data').child('ON').get()
    return data.val()

@app.route('/qc/')
def qc():

    data = db.child('province_data').child('QC').get()
    return data.val()

@app.route('/pe/')
def pe():

    data = db.child('province_data').child('PE').get()
    return data.val()

@app.route('/sk/')
def sk():

    data = db.child('province_data').child('SK').get()
    return data.val()

@app.route('/yt/')
def yt():

    data = db.child('province_data').child('YT').get()
    return data.val()

if __name__ == "__main__":
    app.run(debug=True)
