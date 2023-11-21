import pandas as pd
from sklearn.ensemble import RandomForestClassifier  # Replace with the model of your choice
import joblib
import chardet  # For detecting file encoding
from sklearn.feature_extraction.text import TfidfVectorizer
import xgboost as xgb
import time

def train_model(X_train, y_train):
    # Random Forest Model 1
    rf1 = RandomForestClassifier(n_estimators=100, max_depth=None, n_jobs=-1, random_state=42)
    rf_model1 = rf1.fit(X_train, y_train)

    model_path1 = '/Users/apparilalith/Documents/rishitha/part2/Project/models/rf_model1.pkl'
    joblib.dump(rf1, model_path1)
    # print(f"Random Forest Model 1 saved to {model_path1}")

    # Random Forest Model 2 with different hyperparameters
    rf2 = RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_split=2, n_jobs=-1, random_state=42)
    rf_model2 = rf2.fit(X_train, y_train)

    model_path2 = '/Users/apparilalith/Documents/rishitha/part2/Project/models/rf_model2.pkl'
    joblib.dump(rf2, model_path2)
    # print(f"Random Forest Model 2 saved to {model_path2}")

    # XGBoost Model 3
    xgb_model = xgb.XGBClassifier(learning_rate=0.1, n_estimators=100, max_depth=3, random_state=42)
    xgb_model = xgb_model.fit(X_train, y_train)

    model_path3 = '/Users/apparilalith/Documents/rishitha/part2/Project/models/xgb_model.pkl'
    joblib.dump(xgb_model, model_path3)
    # print(f"XGBoost Model 3 saved to {model_path3}")

    return rf_model1, rf_model2, xgb_model


if __name__ == "__main__":
    # Load your training data
    # (Assuming you have a CSV file with processed features and target variable)
    # Adjust the path and loading method accordingly
    train_data_path = 'C:/Users/rmalempa/Desktop/edu/594/Project/data_original/WELFake_Dataset (1).csv'

    # # Detect the encoding of the file
    # with open(train_data_path, 'rb') as f:
    #     result = chardet.detect(f.read())

    # # Load the data using the detected encoding
    # train_data = pd.read_csv(train_data_path, encoding=result['encoding'])

    # # # print the columns in the DataFrame
    # # print("Columns in the DataFrame:", train_data.columns)

    # # Assuming the target variable is in the 'label' column
    # try:
    #     X_train = train_data[['Title', 'Text']]  # Adjust the columns based on your features
    #     y_train = train_data['Label']  # Define the target variable
    # except KeyError as e:
    #     # print(f"KeyError: {e}")

    # # Train the model
    # train_model(X_train, y_train)
