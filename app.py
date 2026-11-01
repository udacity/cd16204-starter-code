from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
import json
import os



###################### Set up variables for use in our script
app = Flask(__name__)
app.secret_key = '1652d576-484a-49fd-913a-6879acfa6ba4'

with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 

prediction_model = None


####################### Prediction Endpoint
@app.route("/prediction", methods=['POST','OPTIONS'])
def predict():        
    # Read the local CSV path from the JSON field dataset_path into a DataFrame,
    # then pass it to the Step 3 model_predictions function (deployed model).
    raise NotImplementedError(
        "Implement POST /prediction: load the caller's dataset_path and return "
        "deployed-model predictions (Step 4)."
    )

####################### Scoring Endpoint
@app.route("/scoring", methods=['GET','OPTIONS'])
def scoring_endpoint():
    # Score the deployed model on test_data_path/testdata.csv using score_model.
    # Do not overwrite the deployed baseline score.
    raise NotImplementedError(
        "Implement GET /scoring: return deployed-model test F1 without changing its "
        "baseline (Step 4)."
    )

####################### Summary Statistics Endpoint
@app.route("/summarystats", methods=['GET','OPTIONS'])
def summarystats_endpoint():
    # Return means, medians, and standard deviations for numeric columns.
    raise NotImplementedError(
        "Implement GET /summarystats: return ingested-data numeric summary "
        "statistics (Step 4)."
    )

####################### Diagnostics Endpoint
@app.route("/diagnostics", methods=['GET','OPTIONS'])
def diagnostics_endpoint():
    # Return ingestion/training timings, missing-value percentages for all columns,
    # and the dependency version table. Do not replace the deployed model.
    raise NotImplementedError(
        "Implement GET /diagnostics: return timing, missing-data and offline "
        "dependency diagnostics (Step 4)."
    )

if __name__ == "__main__":    
    app.run(host='127.0.0.1', port=8000, debug=True, threaded=True)
