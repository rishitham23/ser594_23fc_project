# Project ML Evaluation

## 1. Title
Navigating Misinformation: A Text Classification Approach to Fake News Detection

## 2. Author
Rishitha Malempati

## 3. Date
11/20/2023

## 4. Evaluation Metrics

### Metric 1: F1 Score
F1 Score is chosen as it provides a balanced measure of precision and recall. In fake news detection, it is crucial to strike a balance between identifying fake news and minimizing false positives and false negatives.

### Metric 2: Area Under the ROC Curve (AUC-ROC)
AUC-ROC is selected to evaluate the model's ability to distinguish between fake and real news across different threshold settings. It is well-suited for imbalanced datasets and provides insights into the model's discriminatory power.

## 5. Alternative Models

### Alternative 1: Random Forest Model 1
Construction:
- n_estimators: 150
  - This parameter represents the number of decision trees in the forest. A higher number can lead to better generalization but comes with increased computational cost.
- max_depth: None
  - The maximum depth of the individual decision trees. Setting it to `None` allows the trees to expand until they contain fewer than `min_samples_split` samples.
- min_samples_split: Default value
  - The minimum number of samples required to split an internal node. The default value is used, and its impact is dependent on the dataset.

Evaluation:
- The Random Forest Model 1 is evaluated against the baseline model to assess its impact on classification accuracy.

### Alternative 2: Random Forest Model 2 with Different Hyperparameters
Construction:
- n_estimators: 200
  - An increased number of decision trees compared to Model 1. This change can capture more complex patterns in the data but may increase training time.
- max_depth: 10
  - A limit on the maximum depth of the individual decision trees. This can help control overfitting and limit the complexity of each tree.
- min_samples_split: 2
  - The minimum number of samples required to split an internal node. Setting it to 2 means that a node will only be split if it contains more than one sample.

Evaluation:
- The Random Forest Model 2 is evaluated against the baseline model to assess its impact on classification accuracy.

### Alternative 3: XGBoost
Construction:
- learning_rate: 0.1
- n_estimators: 100
- max_depth: 3

Evaluation:
- The XGBoost model is evaluated to determine its effectiveness in comparison to the baseline model.

## 6. Best Model

### Best Model: XGBoost

After thorough evaluation using the selected metrics, XGBoost emerged as the best-performing model for fake news detection. The F1 Score and AUC-ROC metrics consistently demonstrated superior or almost equal performance compared to the Random Forest models. XGBoost's ability to handle complex relationships and capture subtle patterns in the data contributed to its effectiveness in distinguishing between fake and real news articles.

The evaluation results indicate that XGBoost provides a balanced trade-off between precision and recall, making it a robust choice for the task of fake news detection in the context of this dataset.
