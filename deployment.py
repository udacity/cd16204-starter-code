from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
import os
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import json



################## Load config.json and correct path variable
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
prod_deployment_path = os.path.join(config['prod_deployment_path']) 


#################### Function for deployment
# Run from the CD16204 project root. Implement the function and a script entry
# point so `python deployment.py` deploys the configured candidate artifacts.
def store_model_into_pickle(model):
    # Copy the latest pickle file, the latestscore.txt value, 
    # and the ingestedfiles.txt file into the deployment directory.
    # The score must describe the model being copied, not an earlier model.
    raise NotImplementedError(
        "Implement store_model_into_pickle(model): deploy the candidate model with "
        "its matching score and ingestion record (Step 2)."
    )
if __name__ == '__main__':
    raise NotImplementedError(
        "Implement store_model_into_pickle() and connect this script entry point to "
        "the configured candidate artifacts (Step 2)."
    )

