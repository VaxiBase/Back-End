from flask import Flask

from main import Api_data
p1 = Api_data()
app = Flask(__name__)

@app.route('/')
def index():
    return p1.data_all_api()

if __name__ == "__main__":
    app.run(debug=True)
