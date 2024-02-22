import pandas as pd
import numpy as np
from scipy import stats
import joblib


def preprocess_data(input_df):
    outlier_columns = ['citric acid', 'residual sugar', 'free sulfur dioxide', 'density']
    for col in outlier_columns:
        col_mean = input_df[col].mean()
        col_std = input_df[col].std()
        z_scores = stats.zscore(input_df[col])
        outliers = np.abs(z_scores) > 4
        input_df.loc[outliers, col] = col_mean
    
    return input_df

def predict(input_features):
    
    with open('lm_model_prediction.sav', 'rb') as file:
        model = joblib.load(file)

    preprocessed_features = preprocess_data(input_features)
    prediction = model.predict(preprocessed_features)
    return prediction
