from flask import Flask, request, jsonify
import joblib
import pandas as pd
from pycaret.classification import predict_model, load_model

app = Flask(__name__)

# Load the model
model = load_model('sleep_health_model')

@app.route('/')
def home():
    return 'Sleep Health Analysis API'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    data = pd.DataFrame(data)
    
    # Make predictions
    predictions = predict_model(model, data=data)
    
    # Extracting predictions
    predictions = predictions['Label'].values[0]
    
    return jsonify({'Prediction': predictions})

if __name__ == '__main__':
    app.run(debug=True)
