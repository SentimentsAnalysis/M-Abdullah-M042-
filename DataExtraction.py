"""Code used for scrapping tweets"""

import snscrape.modules.twitter as sntwitter
import pandas as pd
import DateTime

#After importing libraries, we write a query for fetching data from twitter by giving hastages & time duration.
query = "(#PrayersForTurkey OR #earthquakeinturkey OR #هزة_أرضية) lang:en since:2023-02-06"
tweets = []
limit = 10000 #here we define the limit of tweets we want to fetch.

#We define a loop for data extraction & we are extracting 4 columns(Date, time, username, tweet)
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        time = tweet.date.time()
        tweets.append([tweet.date, time, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'Time', 'username', 'Tweet'])

#Here we save our data in a excel file.
df.to_csv('ExtractedData.csv')
