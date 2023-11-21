import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_colwidth', 100)

data = pd.read_csv( 'C:/Users/rmalempa/Desktop/edu/594/Project/data_original/dataset_reduced.csv', index_col=0)

# visualizing fake and real data distribution
plt.figure(figsize=(8, 6))
data.label.value_counts().plot(kind='bar', color=['red','green'])
plt.xlabel("Fake news")
plt.title("Distribution of fake news labels")
plt.savefig('Visuals/FakeVsReal.png')
# plt.show()


plt.figure(figsize=(8, 6))
bins = np.linspace(0, 8000, 100) # start point, end point, no. of cut points

plt.hist(data[data['label']==True]['body_len'], bins, alpha=0.5, label=True)
plt.hist(data[data['label']==False]['body_len'], bins, alpha=0.5, label=False)
plt.legend(loc='upper right') # location for legend (which looks for 'label' in your data points)
#pyplot.show() # print the chart in your notebook
plt.xlabel('Length of text')
plt.savefig('Visuals/TextLengthFeature.png', dpi=300, bbox_inches='tight')



bins = np.linspace(0, 8, 40) # start point, end point, no. of cut points

plt.hist(data[data['label']==True]['punct%'], bins, alpha=0.5, label=True)
plt.hist(data[data['label']==False]['punct%'], bins, alpha=0.5, label=False)
plt.legend(loc='upper right') # location for legend (which looks for 'label' in your data points)
plt.xlabel('Percentage of text as punctuation')
# plt.savefig('Visuals/PercentPunctuation.png', dpi=300, bbox_inches='tight')

data = pd.read_csv('C:/Users/rmalempa/Desktop/edu/594/Project/data_original/dataset_reduced.csv')
# Calculate min, max, and avg for each attribute
attribute_stats = data[['body_len', 'word_count', 'avg_word_length', 'unique_word_count']].describe().loc[['min', 'max', 'mean']]

print("Attribute Statistics:")
print(attribute_stats)

# Pairwise Scatter Plot

plt.figure(figsize=(8, 6))
sns.pairplot(data[['body_len', 'word_count', 'avg_word_length', 'unique_word_count']])
plt.suptitle('Pairwise Scatter Plot', y=1.02)
plt.savefig('Visuals/PairwiseScatterPlot.png')
# plt.show()

# Calculate correlation coefficients
correlation = data[['body_len', 'word_count', 'avg_word_length', 'unique_word_count']].corr()

# Save the correlation matrix to a file
correlation.to_csv('data_processed/correlations.txt', sep='\t', float_format='%.4f')


# Plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.savefig('Visuals/correlation.png')
# plt.show()

# Histograms with a long tail and a number of outliers are best for transforming
# We do this as a model might focus too much on a long tail and be biased

# First histogram
plt.figure(figsize=(8, 6))

bins = np.linspace(0, 8000, 40)

plt.hist(data['body_len'], bins) # no label, normed or apha needed here as we aren't comparing two distributions together
plt.title("Body Length Distribution")
plt.savefig('Visuals/BodyLengthDist.png')
# plt.show()

# Second histogram
plt.figure(figsize=(8, 6))
bins = np.linspace(0, 10, 40)
plt.hist(data['punct%'], bins)
plt.title("Punctuation % Distribution")
plt.savefig('Visuals/PunctuationPerDist.png')
# plt.show()

data['Full_text_cleaned'] = data['text_nonstop'].apply(lambda x: "".join(x))

from collections import Counter ## for counting words 

## Get real and fake subsets 
fake_text = data[data.label == 1]["Full_text_cleaned"]
real_text = data[data.label == 0]["Full_text_cleaned"]
## Entire vocabulary 
vocab_set = set((" ".join(data.Full_text_cleaned)).split())
non_unique_set = (" ".join(data.Full_text_cleaned)).split()
## Get sizes of vocab, entire corpus, ratio 
print('Vocab size : ', len(vocab_set))
print('Entire word count : ', len(non_unique_set))
print('Ratio of word count to vocab size : ', len(non_unique_set)/len(vocab_set) )

## First, turn a list of lists into just one list -- i.e. join all documents together into
## one giant document/ string
fake_text_giant_string = " ".join(fake_text)
print(len(fake_text_giant_string))
real_text_giant_string = " ".join(real_text)
print(len(real_text_giant_string))


## Now, update to the Counter object to begin counting
## Rmb to split to only feed words
fake_words_counter = Counter(fake_text_giant_string.split())
real_words_counter = Counter(real_text_giant_string.split())

## Visualise the top words 

fake_top_10 = fake_words_counter.most_common(10)
x,y = zip(*fake_top_10)

true_top_10 = real_words_counter.most_common(10)
x2,y2 = zip(*true_top_10)

## Plot
# Plotting fake data
plt.subplot(1, 2, 1)  # (nrows, ncols, index)
plt.bar(x, y, color='red')
plt.title('Top 10 words in Fake Texts')
plt.xticks(rotation=70)
plt.ylabel('Counts')

# Plotting real data
plt.subplot(1, 2, 2)
plt.bar(x2, y2, color='blue')
plt.title('Top 10 words in Real Texts')
plt.xticks(rotation=70)
plt.ylabel('Counts')

plt.tight_layout()
plt.savefig('Visuals/Top10Words.png')
# plt.show()
def generate_statistics(processed_data):
    return None


def generate_visuals(processed_data):
    return None