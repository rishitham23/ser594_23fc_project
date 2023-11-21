import joblib  # For model loading
import pandas as pd
import time

def predict_model(trained_model, X):
    # Use the trained model to make predictions on the test data
    # Perform prediction
    start = time.time()
    rf_y_pred = trained_model.predict(X)
    end = time.time()
    pred_time = (end - start)

    return rf_y_pred


if __name__ == "__main__":
    # Load the trained model from the "models" folder
    model_path = '/Users/apparilalith/Documents/rishitha/part2/Project/models/model.pkl'  # Replace 'your_model' with the model name used in wf_training.py
    trained_model = joblib.load(model_path)

    # Load your test data
    # (Assuming you have a CSV file with processed features)
    # Adjust the path and loading method accordingly
    test_data_path = '/Users/apparilalith/Documents/rishitha/part2/Project/data_processed/dataset_reduced.csv'
    test_data = pd.read_csv(test_data_path)

    # Make predictions using the trained model
    predictions = predict_model(trained_model, test_data)

    # Print or save predictions as needed
    print("Predictions:", predictions)
