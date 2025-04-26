from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import json

app = Flask(__name__)
CORS(app)  # Allow requests from any domain

# Load the saved model
model = pickle.load(open('classification_model.pkl', 'rb'))

# Load the columns (optional, if you need)
with open('columns.json', 'r') as f:
    columns = json.load(f)['data_columns']

@app.route('/')
def home():
    return "Mental Health Prediction API is Running 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)  # force=True ensures JSON body even without content-type header
        features = np.array([data['features']])  # Expects 'features' key in JSON
        
        prediction = model.predict(features)
        
        response = {
            'prediction': prediction.tolist()
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
