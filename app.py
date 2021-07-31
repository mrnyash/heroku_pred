from flask import Flask, render_template
import numpy as np
from flask.globals import request
import joblib
app = Flask(__name__) # Behind the scene it is converted to main.py


# load a model
model = joblib.load('hiring_model.pkl')

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/predict', methods = ['POST'])
def predict():

    exp = request.form.get('experience')
    score = request.form.get('test_score')
    interview_score = request.form.get('Interview_score')

    prediciton = model.predict([[exp, score, interview_score]])

    output = round(prediciton[0], 2)
 
 

    return render_template('base.html', prediction_text = f"Employee Salary will be $ {output}")


# @app.route('/welcome')
# def welcome():
#     return 'Welcome my Friend'

if __name__ == '__main__':
    app.run(debug=True) # debug = true will reload the server