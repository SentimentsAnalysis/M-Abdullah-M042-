import string
from collections import Counter
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

#Importing extracted data for analysis
text = open('tweet.csv', encoding='utf=8').read()

#Converting uppercase latters into lowercase for analysis.
lower_case = text.lower()

#removing links from data
import re
pattern = "http\S+"
new_text = re.sub(pattern, "", lower_case)

#removing Hashtags
pattern = "http\S+"
cleaned_text = re.sub(pattern, "", new_text)
cleaned_text

#Removing Punctuations
clean_text = ""
for i in cleaned_text:
    if i.isalnum():
        clean_text+=i
print(clean_text)

#Separating data for analysis
tokenized_words = word_tokenize(cleaned_text)

#Removing Stopwords from data.
st = set(stopwords.words('english'))
final_words = []
for word in tokenized_words:
    if word not in st:
        final_words.append(word)
print(final_words)

#Importing Emotion list.
emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').replace(' ', '')
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)

#Counting the Total number of emotions
w = Counter(emotion_list)
print(w)

#Making the char of analysis.
plt.bar(w.keys(), w.values())
plt.show()