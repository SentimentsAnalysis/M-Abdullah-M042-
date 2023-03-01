My Project is Twitter Sentiment Analysis. In which we find out the emotions of the people through their tweets on Twitter.
Project has 2 phases. In first phase, i extracted data & in second phase, i perform sentiment Analysis.

1. First of all i extracted tweets from twitter through snscraper. For this purpose we required snscrape, DateTime & Pandas libraries which we install using pip command
   & imported them in the porject.
2. Wrote a query for data extraction in which hashtages are included for data extraction & time duration is added.
3. After this, i specify the limit of No. of tweets i want to extract.
4. A loop is defined for data extraction & 4 columns(Date, time, username, tweet) are made.
5. After this, an Excel file is created for saving that data data.

Sentiment Analysis:
7. After collecting dataset, we perform analysis on data in different ways.
I perform analysis in certain steps:
 1. Extracting tweets.
 2. Converting text into lowercase
 3. Removing links
 4. Removing hastags
 5. Removing punctuations
 6. Separating data for analysis
 7. Removing stop words.
 8. Match the emotions
 9. Counting emotion values
 10. Build the chart.
