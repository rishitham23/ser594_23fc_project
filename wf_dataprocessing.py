# import inline
import matplotlib
import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import string

pd.set_option('display.max_colwidth', 100)

data = pd.read_csv('/Users/apparilalith/Documents/rishitha/part2/Project/data_original/WELFake_Dataset (1).csv', index_col=0, encoding='ISO-8859-1', dtype=str)

data = data.fillna(' ')

data['Full_text'] = data['title'] + data['text']
data = data[['Full_text', 'label']]
data.rename(columns={'Full_text': 'text'}, inplace=True)

data = data.loc[data['text'].str.len() >= 300]
data = data.sample(frac=1).reset_index(drop=True)

data['text_lower'] = data['text'].str.lower()
data = data[['text','text_lower','label']] # organise columns in the order I want


data['text_clean'] = data['text_lower'].map(lambda x: re.sub('^.+?[(Reuters)]+[\s]+\-', "", x)) # removes everything before the first '-' symbol 
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('watch the full.+$', "", x))
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('featured image.+$', "", x))
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('writing by.+$', "", x))
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('via:.+$', "", x))
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('this artical originally.+$', "", x))
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('read more.+$', "", x))
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('wfb.+$', "", x))
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('this version of the story.+$', "", x))
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('photo by.+$', "", x))
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])', "", x)) # URLs
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('@([A-Za-z0-9_]+)', "", x)) # Twitter usernames
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('cnn politics.+$', "", x))
data['text_clean'] = data['text_clean'].map(lambda x: re.sub('daily mail.+$', "", x))



def clean_text(text):
    text = "".join([word for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    return text

data['text_clean'] = data['text_clean'].apply(lambda x: clean_text(x))

nltk.download("punkt")  # Downloads the tokenizer data
nltk.download("stopwords")  # Downloads the stopwords dataset (if needed)

data['text_clean'] = data['text_clean'].apply(word_tokenize)

print (stopwords.words('english'))

def remove_stop_word(tokens):
    tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
    return tokens 
data['text_nonstop'] = data['text_clean'].apply(remove_stop_word)

ps = nltk.PorterStemmer()

# dir(ps) # looks at the attributes of the PorterStemmer

def stemming(tokenized_text):
    text = [ps.stem(word) for word in tokenized_text] # returns the stemmed word in the list
    return text

data['text_stemmed'] = data['text_nonstop'].apply(lambda x: stemming(x))

data['Full_text_cleaned'] = data['text_stemmed'].apply(lambda x: ' '.join(x))


# Length of text (from texts with extras, including publication name, removed)
data['body_len'] = data['text_lower'].apply(lambda x: len(x) - x.count(" "))

# Percentage of text which is punctuation (from last step which still had punctuation)
def count_punct(text):
    count = sum([1 for char in text if char in string.punctuation])
    return round(count/(len(text) - text.count(" ")), 3)*100

data['punct%'] = data['text_lower'].apply(lambda x: count_punct(x))

# Create quantitative attributes
data['body_len'] = data['text'].apply(lambda x: len(x))
data['word_count'] = data['text'].apply(lambda x: len(x.split()))
data['avg_word_length'] = data['body_len'] / data['word_count']

# Function to count unique words
def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

data['unique_word_count'] = data['text'].apply(count_unique_words)
result_df = data[['text_stemmed', 'body_len' , 'punct%', 'word_count', 'avg_word_length', 'unique_word_count', 'label']]
result_df.to_csv("/Users/apparilalith/Documents/rishitha/part2/Project/data_processed/dataset_reduced.csv")


def process_data(raw_data):
    return None