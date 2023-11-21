#### SER594: Experimentation
#### Title: "Navigating Misinformation: A Text Classification Approach to Fake News Detection"
#### Author: Rishitha Malempati
#### Date: 11/20/2023

## Explainable Records
### Record 1
Raw Data: `data_processed/explainable_record_1.csv`

Prediction Explanation: This record represents a news article with an exceptionally high word count and average word length. The model tends to associate such characteristics with a higher likelihood of real news due to the presence of more detailed and nuanced information.

### Record 2
Raw Data: `data_processed/explainable_record_0.csv`

Prediction Explanation: This record showcases a news article with a relatively short body length and lower average word length. The model might interpret these features as indicative of fake news, possibly considering brevity and simplicity as characteristics of misinformation.

## Interesting Features
### Feature A
Features: 'body_len', 'punct%', 'word_count', 'avg_word_length', 'unique_word_count'

Justification: The word count is interesting because longer news articles may contain more nuanced information and context, potentially aiding the model in distinguishing between real and fake news.

### Feature B
Features: 'body_len', 'punct%', 'word_count', 'avg_word_length', 'unique_word_count', 'Text Stemmed'

Justification: The inclusion of the 'Text Stemmed' feature is intriguing as it reflects the complexity of language used in news articles. The model might learn that real news tends to have longer and more sophisticated language compared to fake news. Additionally, other linguistic features such as average word length, punctuation percentage, and unique word count contribute to the understanding of language complexity and can aid the model in distinguishing between real and fake news.

## Experiments 
### Varying A
Prediction Trend Seen:
When varying Feature A ('body_len', 'punct%', 'word_count', 'avg_word_length', 'unique_word_count') alone, the model exhibited a prediction trend. However, it is important to note that the accuracy observed in this experiment was approximately 0.7, which is lower than the overall accuracy of 0.9 achieved with the entire dataset. Hence it can be noted that using only derived quantitative features to predict fake news does a decent job.

Summary: `evaluation/summary_extracted_features.txt`

### Varying B
Prediction Trend Seen:
Similarly, when varying Feature B ( 'Text Stemmed') alone, the model displayed a prediction trend. However, the accuracy observed in this experiment was approximately 0.902, which is slightly higher the overall accuracy of 0.903 achieved with the entire dataset. Hence it can be noted that using only text stemmed to predict fake news does a very good job at predicting the fake news.

Summary: `evaluation/summary_wholedata.txt`

### Varying A and B together
Prediction Trend Seen: 'body_len', 'punct%', 'word_count', 'avg_word_length', 'unique_word_count', 'Text Stemmed'
Further experiments were conducted by varying Feature A and Feature B together. The combined variation exhibited a prediction trend, the accuracy remained around 0.902, which is lower than the overall accuracy of 0.903 achieved with the stemmed dataset. Adding the derived quantitative features almost remains same. It can be noted that using only text can be used to predict fake news with a good accuracy.

Summary: `evaluation/summary.txt`


### Varying A and B inversely
Prediction Trend Seen:
There is no varying A and B inversely as this experiment was only done using a set of features and upon doing some explorations we couldn't see any feature that might stand out to explore independently as text embedings play an important role in the predictions for fake news.
