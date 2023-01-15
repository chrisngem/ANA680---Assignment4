from flask import Flask, render_template, request
import numpy as np
import pickle
# import joblib
app = Flask(__name__)
filename = 'BCW.pkl'
model = pickle.load(open(filename, 'rb'))    # load the model
#model = joblib.load(filename)  # two ways to load the model, not using joblib here
#model = joblib.load('filename.pkl')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])  # The user input is processed here
def predict():
    Thickness = request.form['Thickness']
    Size = request.form['Size']
    Shape = request.form['Shape']
    Adhesion = request.form['Adhesion']
    pred = model.predict(np.array([[Thickness,Size,Shape,Adhesion]]))
    #print(pred)
    return render_template('index.html', predict=str(pred))
if __name__ == '__main__':
    app.run