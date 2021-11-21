from flask import Flask
import pyrebase


from main import Api_data
p1 = Api_data()
app = Flask(__name__)

#p1.update_db()


@app.route('/')
def index():
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

    data = db.child('province_data').get()
    return data.val()

if __name__ == "__main__":
    app.run(debug=True)
