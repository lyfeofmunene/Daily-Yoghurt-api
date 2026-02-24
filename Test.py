# flask
import flask
from flask import *

# create flask application
app = Flask(__name__)

@app.route('/api/home')

def home():
    return jsonify({"message":"Welcome to the home api"})

@app.route('/api/services')
def services():
    return jsonify({"Message":"Welcome to the services api"})

@app.route('/api/products')
def products():
    return jsonify({"message":"Welcome to the services api"})

@app.route('/api/calc',method=['POST'])
def calc():
    if request.method =='POST':
        num1 = request.form['num1']
        num2 = request.form['num2']

        answer = int(num1) + int(num2)
        return jsonify()
if __name__ == '__main__':
    app.run(debug=True)

