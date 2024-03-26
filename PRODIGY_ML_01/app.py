from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Charger le modèle entraîné à partir du fichier Pickle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Route pour la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    # Obtenir les données de la requête POST
    data = request.get_json(force=True)


    # Convertir les données en un tableau numpy
    input_data = np.array(data['features'])
    print(input_data)

    # Faire la prédiction avec le modèle
    prediction_log  = model.predict(input_data)
    prediction = np.exp(prediction_log)
    
    sale_prices = loadPrices()

    # Renvoyer la prédiction au format JSON
    return jsonify({'prediction': prediction.tolist(), 'sale_prices': sale_prices.tolist()})


def loadPrices():
    # Load the entire 'SalePrice' column
    df = pd.read_csv('./data/train.csv', usecols=['SalePrice'])
    
    # Generate 30 random elements
    random_df = df['SalePrice'].sample(n=50)
    
    return random_df
    
if __name__ == '__main__':
    app.run(debug=True)
