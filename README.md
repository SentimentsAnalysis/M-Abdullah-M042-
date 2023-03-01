My Project is Twitter Sentiment Analysis. In which we find out the emotions of the people through their tweets on Twitter.
Project has 2 phases. In first phase, i extracted data & in second phase, i perform sentiment Analysis.

{1st Phase - Data Extraction}
1. First of all i extracted tweets from twitter through snscraper. For this purpose we required snscrape, DateTime & Pandas libraries which we install using pip command
   & imported them in the porject.
2. Wrote a query for data extraction in which hashtags are included for data extraction & time duration is added.
3. After this, i specify the limit of No. of tweets i want to extract.
4. A loop is defined for data extraction & 4 columns(Date, time, username, tweet) are made.
5. After this, an Excel file is created for saving that data data.

{2nd Phase - Sentiment Analysis}
After collecting dataset, I created a python file to perform analysis on data because I am performing sentiment Analysis using python language. Before this I took certain steps to clean the data to discard unwanted text from the data discribed below:
 1. In first step, i converted text into lower case by using lower() function. I did this because I have to match this text data with the data in emotion.txt file which     is in lower case.
 2. After this I removed links from my data using re library. for this, I defined a pattern. When the pattern is matched in the data, i will remove that url from the         text.
 3. In 3rd step, I Removed Punctuation from the text. For this, I imported string library because I have to apply for loop & have to check every single word.
 4. In 4th step, I imported word_tokenize from nltk library for dividing text into separate words for analysis.
 5. In 5th step, I removed stopwords from text. Stopwords are those words which gives no emotion like he, she, is, are, there, them etc. For this, i imported stopwords       function from nltk library for removing them from text.
 6. In 6th step, I imported Emotion.txt file and made some changes in the format of the file to make it easily compareable with the text & find the emotion list from the     text.
 6. After this, i simply count the total number of emotions exist in the data. For this, I imported Counter Library for counting the emotions in the data.
 7. At the end of the Analysis, i make the graph of the emotion. For making the graph, I imported a library which is matplotlib which is used for making graphs in python.
