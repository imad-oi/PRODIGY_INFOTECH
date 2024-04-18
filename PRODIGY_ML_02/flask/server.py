import joblib

from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    input_data = pd.DataFrame(data, index=[0])
    input_data = pd.get_dummies(input_data)
    
    predictions = model.predict(input_data)
    
    return jsonify({'predictions': predictions.tolist()})


if __name__ == '__main__':
    app.run(debug=True)
