import pandas as pd
from wf_training import train_model
from wf_prediction import predict_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, median_absolute_error, accuracy_score, f1_score, roc_auc_score

from sklearn.feature_extraction.text import TfidfVectorizer
import joblib



def vectorize_data(X_train, X_test):
    tfidf_vect = TfidfVectorizer()
    tfidf_vect_fit = tfidf_vect.fit(X_train['text_stemmed']) # this just fits the vectorizer it doesn't create the values yet, we use the transform function for that

    # Here (above & below) we're splitting the training and transorming steps to keep the training and test data separate

    # These two below will have the same number of columns as they're both being transformed using the 'tfidf_vect_fit' which was fit to the training data only
    tfidf_train = tfidf_vect_fit.transform(X_train['text_stemmed'])

    tfidf_test = tfidf_vect_fit.transform(X_test['text_stemmed'])

    X_train_vect = pd.concat([X_train[['body_len' ]].reset_index(drop=True), 
            pd.DataFrame(tfidf_train.toarray())], axis=1) 

    # 'axis=1' stacks them side by side (when concatenated)
    X_test_vect = pd.concat([X_test[['body_len']].reset_index(drop=True), 
            pd.DataFrame(tfidf_test.toarray())], axis=1)
    X_train_vect.columns = X_train_vect.columns.astype(str)
    X_test_vect.columns = X_test_vect.columns.astype(str)

    return X_train_vect, X_test_vect

def run_evaluations(X_test_vect, y_test):
    rf1 = joblib.load('/Users/apparilalith/Documents/rishitha/part2/Project/models/rf_model1.pkl')
    rf2 = joblib.load('/Users/apparilalith/Documents/rishitha/part2/Project/models/rf_model2.pkl')
    xgb_model = joblib.load('/Users/apparilalith/Documents/rishitha/part2/Project/models/xgb_model.pkl')

    # Perform prediction on the test set for each model
    y_pred_rf1 = predict_model(rf1, X_test_vect)
    y_pred_rf2 = predict_model(rf2, X_test_vect)
    y_pred_xgb = predict_model(xgb_model, X_test_vect)

    # Evaluate the models
    mae_rf1 = mean_absolute_error(y_test, y_pred_rf1)
    medae_rf1 = median_absolute_error(y_test, y_pred_rf1)
    accuracy_rf1 = accuracy_score(y_test, y_pred_rf1)
    f1_rf1 = f1_score(y_test, y_pred_rf1)
    auc_roc_rf1 = roc_auc_score(y_test, y_pred_rf1)

    mae_rf2 = mean_absolute_error(y_test, y_pred_rf2)
    medae_rf2 = median_absolute_error(y_test, y_pred_rf2)
    accuracy_rf2 = accuracy_score(y_test, y_pred_rf2)
    f1_rf2 = f1_score(y_test, y_pred_rf2)
    auc_roc_rf2 = roc_auc_score(y_test, y_pred_rf2)

    mae_xgb = mean_absolute_error(y_test, y_pred_xgb)
    medae_xgb = median_absolute_error(y_test, y_pred_xgb)
    accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
    f1_xgb = f1_score(y_test, y_pred_xgb)
    auc_roc_xgb = roc_auc_score(y_test, y_pred_xgb)

    # Write the results to a CSV file
    output_path = '/Users/apparilalith/Documents/rishitha/part2/Project/evaluation/summary.txt'
    df = pd.DataFrame({
        'Method': ['randomforest1', 'randomforest2', 'xgboost'],
        'MAE': [mae_rf1, mae_rf2, mae_xgb],
        'MedAE': [medae_rf1, medae_rf2, medae_xgb],
        'Accuracy': [accuracy_rf1, accuracy_rf2, accuracy_xgb],
        'F1 Score': [f1_rf1, f1_rf2, f1_xgb],
        'AUC-ROC': [auc_roc_rf1, auc_roc_rf2, auc_roc_xgb]
    })
    df.to_csv(output_path, index=False)

    # print(f"Results written to {output_path}")

def explorations(X_test, y_test):
    # Load your dataset
    # Assuming your dataset is in a CSV file named 'your_dataset.csv'

    # Assuming your features of interest are 'feature_A' and 'feature_B'
    feature_A = 'body_len'
    feature_B = 'word_count'
    target_column = 'label'

    # Load the pre-trained XGBoost model
    xgb_model = joblib.load('/Users/apparilalith/Documents/rishitha/part2/Project/models/xgb_model.pkl')

    # Experiment with varying feature A
    feature_A_values = [300, 1000, 5000, 10000, 20000, 50000]
    accuracy_A = []
    f1_A = []

    for value in feature_A_values:
        X_exp_A = X_test.copy()
        X_exp_A[feature_A] = value
        y_exp_A = xgb_model.predict(X_exp_A)
        accuracy_A.append((value, accuracy_score(y_test, y_exp_A)))
        f1_A.append((value, f1_score(y_test, y_exp_A)))

    # Experiment with varying feature B
    feature_B_values = [50, 100, 500, 1000, 2000, 5000]
    accuracy_B = []
    f1_B = []
    for value in feature_B_values:
        X_exp_B = X_test.copy()
        X_exp_B[feature_B] = value
        y_exp_B = xgb_model.predict(X_exp_B)
        accuracy_B.append((value, accuracy_score(y_test, y_exp_B)))
        f1_B.append((value, f1_score(y_test, y_exp_B)))

    # Experiment with varying A and B together: correlated
    correlated_values = [(1000, 100), (2000, 200), (5000, 500), (10000, 1000)]
    accuracy_correlated = []
    f1_correlated = []

    for value_A, value_B in correlated_values:
        X_exp_A_B = X_test.copy()
        X_exp_A_B[feature_A] = value_A
        X_exp_A_B[feature_B] = value_B
        y_exp_A_B = xgb_model.predict(X_exp_A_B)
        accuracy_correlated.append(((value_A, value_B), accuracy_score(y_test, y_exp_A_B)))
        f1_correlated.append(((value_A, value_B), f1_score(y_test, y_exp_A_B)))

    # Experiment with varying A and B together: inversely correlated
    inversely_correlated_values = [(1000, 5000), (2000, 2000), (5000, 1000), (10000, 500)]
    accuracy_inversely_correlated = []
    f1_inversely_correlated = []

    for value_A, value_B in inversely_correlated_values:
        X_exp_A_B = X_test.copy()
        X_exp_A_B[feature_A] = value_A
        X_exp_A_B[feature_B] = value_B
        y_exp_A_B = xgb_model.predict(X_exp_A_B)
        accuracy_inversely_correlated.append(((value_A, value_B), accuracy_score(y_test, y_exp_A_B)))
        f1_inversely_correlated.append(((value_A, value_B), f1_score(y_test, y_exp_A_B)))

    # print the trends
    print("## Experiments \n")

    # Varying A
    print("### Varying A")
    print("*Prediction Trend Seen:*")
    for (value, acc, f1) in zip(feature_A_values, accuracy_A, f1_A):
        print(f"feature_A: , Accuracy: {acc[1]:.2f}, F1 Score: {f1[1]:.2f}")
    print("\n")

    # Varying B
    # print("### Varying B")
    print("*Prediction Trend Seen:*")
    for (value, acc, f1) in zip(feature_B_values, accuracy_B, f1_B):
        print(f"feature_B, Accuracy: {acc[1]:.2f}, F1 Score: {f1[1]:.2f}")
    print("\n")

    # Varying A and B together: correlated
    print("### Varying A and B together (Correlated)")
    print("*Prediction Trend Seen:*")
    for (values, acc, f1) in zip(correlated_values, accuracy_correlated, f1_correlated):
        print(f"feature_A, feature_B, Accuracy: {acc[1]:.2f}, F1 Score: {f1[1]:.2f}")
    print("\n")

    # Varying A and B together: inversely correlated
    print("### Varying A and B together (Inversely Correlated)")
    print("*Prediction Trend Seen:*")
    for (values, acc, f1) in zip(inversely_correlated_values, accuracy_inversely_correlated, f1_inversely_correlated):
        print(f"feature_A, feature_B, Accuracy: {acc[1]:.2f}, F1 Score: {f1[1]:.2f}")
    print("\n")



def main():
    # Load the processed data
    processed_data_path = '/Users/apparilalith/Documents/rishitha/part2/Project/data_processed/dataset_reduced.csv'
    print('Read data')
    data = pd.read_csv(processed_data_path)
    data = data[:5000]
    data = data[(data['label'] == '0') | (data['label'] == '1')]
    data.label = data.label.astype(int)

    print('Split.')
    X_train, X_test, y_train, y_test = train_test_split(data[['text_stemmed', 'body_len' , 'punct%', 'word_count', 'avg_word_length', 'unique_word_count']], data['label'], test_size=0.2, random_state=42) # columns to train & test on with test size as proportion of dataset

    print('Vectorize.')
    X_train_vect, X_test_vect = vectorize_data(X_train, X_test)
    # print(X_test_vect.dtypes)

    print('Training Started.')
    # Train the machine learning model
    
    rf1, rf2, xgb_model = train_model(X_train_vect, y_train)

    run_evaluations(X_test_vect, y_test)
    # explorations(X_test_vect, y_test)

if __name__ == "__main__":
    main()
    
