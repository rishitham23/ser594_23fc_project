#### SERX94: Exploratory Data Munging and Visualization
#### Title: Fake News Classification
#### Author: Rishitha Malempati
#### Date: 10/18/2023

## Basic Questions
Dataset Author(s): Pawan Kumar Verma, Prateek Agrawal, Ivone Amorim, Radu Prodan.

Dataset Construction Date: April 2021 (Updated 10 days ago.i.e.,10/08/2023)

Dataset Record Count: 78097

Dataset Field Meanings: 
1)Index - Serial Numbers starting from 0
2)Title - Headings of the news published
3)Text - Content published under the news article
4)Label - Representation of whether the news is fake or real. It is represented in 0's and 1's. 0=fake and 1=real.

Dataset File Hash(es): 73c9675a4b3d09f86a6933d0b8d7d908

## Interpretable Records
### Record 1
Raw Data: 
Index: 5
Title: About Time! Christian Group Sues Amazon and SPLC for Designation as Hate Group.
Text: All we can say on this one is it s about time someone sued the Southern Poverty Law Center!On Tuesday, D. James Kennedy Ministries (DJKM) filed a lawsuit against the Southern Poverty Law Center (SPLC), the charity navigation organization GuideStar, and Amazon, for defamation, religious discrimination, and trafficking in falsehood. The SPLC listed DJKM as a  hate group,  while GuideStar also categorized it in those terms, and Amazon kept the ministry off of its charity donation program, Amazon Smile. We embarked today on a journey to right a terrible wrong,  Dr. Frank Wright, president and CEO at DJKM, said in a statement Tuesday.  Those who knowingly label Christian ministries as  hate  groups, solely for subscribing to the historic Christian faith, are either woefully uninformed or willfully deceitful. In the case of the Southern Poverty Law Center, our lawsuit alleges the latter. The SPLC has labeled DJKM an  anti-LGBT hate group  for its opposition to same-sex marriage and transgenderism.  These false and illegal characterizations have a chilling effect on the free exercise of religion and on religious free speech for all people of faith,  Wright declared. After having given the SPLC an opportunity to retract, we have undertaken this legal action, seeking a trial by a jury of our peers, to preserve our own rights under the law and to defend the religious free speech rights of all Americans,  the DJKM president concluded.The lawsuit laid out charges against the SPLC, GuideStar, and Amazon.Read more: PJM
Label: 1

Interpretation:
Index: Represents the serial number of the row in the dataset.
Title: Represents title published in a news article. 
Text: The text appears to be a news article discussing a lawsuit filed by D. James Kennedy Ministries (DJKM) against the Southern Poverty Law Center (SPLC), GuideStar, and Amazon. The lawsuit is based on allegations of defamation, religious discrimination, and the spread of falsehood. The article highlights that DJKM was labeled as a 'hate group' by the SPLC and faced consequences such as exclusion from Amazon's charity donation program, Amazon Smile. The DJKM president, Dr. Frank Wright, is quoted expressing the motive behind the lawsuit and the impact of such labeling on religious free speech rights. The article ends by mentioning that the lawsuit has been filed against the SPLC, GuideStar, and Amazon.
Label: It indicates the information is classified as real

Based on the information, it appears that the text represents a genuine news article discussing a lawsuit filed by the mentioned Christian group against several entities. The content includes quotes from the president of DJKM, outlining the reasons behind the legal action and the perceived consequences of being labeled a 'hate group.'
It seems plausible within the context of a news dataset that includes articles related to legal actions, controversies, and societal issues. However, without further context or additional information, it's essential to conduct thorough fact-checking to verify the claims made in the article and to ensure the reliability and accuracy of the information. As the label indicates that the information is classified as "real," it suggests that the provided text is considered to be factual and not fabricated or misleading within the scope of the dataset's categorization.

### Record 2
Raw Data: 
Index: 11
Title: May Brexit offer would hurt, cost EU citizens - EU parliament
Text: BRUSSELS (Reuters) - British Prime Minister Theresa May s offer of  settled status  for EU residents is flawed and will leave them with fewer rights after Brexit, the European Parliament s Brexit coordinator said on Tuesday. A family of five could face a bill of 360 pounds to acquire the new status, Guy Verhofstadt told May s Brexit Secretary David Davis in a letter seen by Reuters    a very significant amount for a family on low income . Listing three other concerns for the EU legislature, which must approve any treaty on the March 2019 exit, Verhofstadt told Davis:  Under your proposals, EU citizens will definitely notice a deterioration of their status as a result of Brexit. And the Parliament s aim all along has been that EU citizens, and UK citizens in the EU-27, should notice no difference.  Verhofstadt, a former Belgian prime minister, wrote in response to Davis, who had written to him after Parliament complained last week that there remained  major issues  to be settled on the rights of the 3 million EU citizens in Britain. On Tuesday, he told reporters that Parliament was determined that expatriates should not become  victims of Brexit . May had unveiled more details last week of a system aimed at giving people already in Britain a quick and cheap way of asserting their rights to stay there indefinitely. The issue, along with how much Britain owes and the new EU-UK border across Ireland, is one on which the EU wants an outline agreement before opening talks on the future of trade. Verhofstadt said lawmakers were not dismissing British efforts to streamline applications but saw flaws in the nature of  settled status  itself. As well as the cost, which is similar to that of acquiring a British passport, he cited three others: - Europeans should simply  declare  a whole household resident, without needing an  application  process; the burden of proof should be on the British authorities to deny them rights. - more stringent conditions on criminal records could mean some EU residents, including some now with permanent resident status, being deported for failing to gain  settled status . - EU residents would lose some rights to bring relatives to Britain as the new status would give them the same rights as British people, who now have fewer rights than EU citizens.   
Label: 0

Interpretation:
Index: Represents the serial number of the row in the dataset.
Title: Represents title published in a news article. 
Text: The text describes criticisms from the European Parliament's Brexit coordinator, Guy Verhofstadt, regarding British Prime Minister Theresa May's offer of "settled status" for EU residents. Verhofstadt's concerns include potential financial implications for families seeking the new status, as well as implications on the rights and status of EU citizens in the UK post-Brexit. He also highlights specific issues with the proposed "settled status" system, such as the burden of proof on authorities and potential limitations on the rights of EU residents compared to British citizens.
Label: This indicates the information is classified as fake.

Based on the information provided, the text seems to present a critical perspective on the Brexit offer and its potential implications for EU citizens residing in the UK. The statements attributed to Guy Verhofstadt appear to be plausible within the context of a political debate surrounding Brexit negotiations and the concerns of the European Parliament. However, the label classifies the information as "fake," suggesting that within the dataset's categorization, this information is not considered to be genuine or factually accurate.
In terms of the "reasonableness" of the data, it is crucial to conduct further fact-checking to verify the claims made within the text and to understand the context in which these statements were made. As the label indicates the information is "fake," it implies that the provided text is considered to be fabricated or misleading within the scope of the dataset's classification criteria. It is essential to critically evaluate the credibility and reliability of the information before drawing any definitive conclusions.

## Background Domain Knowledge
Introduction to the domain of the project: Fake News Detection.

In today's world, with so much information available online, it's becoming increasingly tricky to figure out what's true and what's not. 
You've probably come across stories that just didn't seem right or seemed designed to mislead. We call these stories "fake news." 
Fake news can be dangerous because it can influence our thoughts and decisions, and it can create a lot of confusion.

To tackle this problem, researchers and experts are using computer programs to help spot fake news. 
These programs use technology to study the words and patterns in news stories. 
They look for clues that might suggest a story isn't true. 
By using a lot of examples of both real and fake news, these programs learn to tell the difference between them.

This field combines computer science with how people use language and information. 
It's not just about the technology; it's also about understanding how fake news can affect our lives and our society. 
By creating better tools to identify fake news, we can help people know which information to trust and which to be cautious about. 
This can protect us from being misled and help us make better-informed decisions based on reliable information. 
As technology continues to advance, it's crucial to keep improving these tools to make sure we can trust what we read and see online.


## Data Transformation
### Transformation 1: Smoothing
Description: Smoothing is a technique used to remove noise from data by averaging out fluctuations.

Soundness Justification:Smoothing helps in reducing the impact of random variations, making underlying patterns more visible without distorting the general trends. It can help in identifying significant trends while minimizing the impact of noisy data points.

### Transformation 2: Imputation
Description: Imputation is the process of replacing missing data points with substituted values.

Soundness Justification:Imputation is commonly used when dealing with incomplete datasets. By carefully selecting appropriate substitute values based on the characteristics of the data, it ensures that the overall statistical properties of the dataset are preserved and that the analysis is not skewed by missing values.

### Transformation 3: Stop Words Removal
Description: Deleting stop words refers to the elimination of commonly occurring words, such as 'the,' 'and,' 'is,' and 'in,' which do not contribute significantly to the overall meaning of the text.

Soundness Justification:Stop words are frequently occurring words that typically do not carry much semantic meaning and can potentially add noise to natural language processing tasks such as sentiment analysis or text classification. Removing stop words helps to improve the efficiency of text processing algorithms and enhances the focus on the essential content and context of the text.


## Visualization
### Visual 1: Distribution of news label
Analysis: The bar graph effectively categorizes the dataset into two distinct groups, one representing fake news and the other real news. The significantly higher bar for real news compared to fake news suggests that the dataset contains a larger proportion of real news instances. This clear differentiation between the two categories indicates the potential balance or distribution of different types of news within the dataset, providing an initial understanding of the prevalence of real and fake news in the analyzed context.

### Visual 2: Top 10 Fake and Real texts
Analysis: 
1) Bar Graph for Top 10 Fake Texts: The bar graph highlights the frequency of occurrence of different fake texts. 
2) Bar Graph for Top 10 Real Texts: The bar graph presents the distribution of the top 10 real texts.

### Visual 3: Pairwise Scatter Plot
Analysis: The pairwise scatter plot for unique word count, average word length, word count, and body length demonstrates several notable trends. There appears to be a positive linear relationship between unique word count and word count, while a slight negative correlation is observed between average word length and unique word count. Additionally, the plot indicates a positive linear trend between word count and body length, suggesting that as the body length increases, the word count also tends to increase, highlighting potential associations among these quantitative features.

### Visual 4: Correlation matrix
Analysis: The correlation matrix reveals the pairwise correlations between multiple variables in the dataset. The values range between -1 and 1, where 1 indicates a perfect positive correlation, -1 indicates a perfect negative correlation, and 0 implies no correlation. By examining the matrix, we can identify which variables are strongly related, which ones have weaker connections, and which pairs might exhibit potential dependencies or interactions, providing insights into the underlying patterns and associations within the data.

### Visual 5: Length of text for fake and real news
Analysis: This is a histogram plot which demonstrates the distribution of the length of text for both true and false news articles. The x-axis represents the range of text lengths, while the y-axis indicates the frequency or count of articles falling within each length range.

### Visual 6: Percentage of text which is punctuation
Analysis: The histogram representing the percentage of text that consists of punctuation reveals that the majority of the text samples contain a relatively low proportion of punctuation marks, with the highest frequency of samples falling within the 10% to 20% range. 