import json
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import re
import string
from nltk.corpus import stopwords

print("This tool is to be used in conjuction with the twint" + "\n")
print("output all twitter data into a json file" + "\n")
print("identify the path to the json file when prompted" + "\n")
print("This program will then return text frequency analysis of all tweets in the JSON" + "\n")
print("This program filters out stop words for better analysis" + "\n")


file_name = input("Path to file to be analyzed: ")
data = pd.read_json(file_name, lines=True)

frequency = {}

def extract_tweet():
	# removes all tweets from JSON and puts them in one big string
	tweets = ''
	for tweet in data['tweet']:
		tweets += tweet + ' '
	return tweets

def word_frequency():
	# returns a dictionary with each word and how often it was used as the key value pair
	match_pattern = re.findall(r'\b[a-z]{3,15}\b', extract_tweet())
	for word in match_pattern:
		count = frequency.get(word,0)
		frequency[word] = count + 1
	return frequency

def old_list():
	# extracts words from the dict frequency to be used in following methods
	old_words = []
	for words in frequency:
		old_words.append(words)
	return old_words

def remove_list():
	# builds a list of words to be removed
	stop_words = []
	stop_words = stopwords.words('english')
	stop_words.append('https')
	stop_words.append('amp')
	remove_words = []

	for word in old_list():
		for stop in stop_words:
			if word == stop:
				remove_words.append(word)
	return remove_words

def remove_stop():
	# removes stop words from frequency dictionary
	frequency = word_frequency()

	for word in remove_list():
		del frequency[word]
	return frequency

res = {key: val for key, val in sorted(remove_stop().items(), key = lambda ele: ele[1], reverse = True)}
res2 = dict(itertools.islice(res.items(), 30))

plt.barh(*zip(*res2.items()))
plt.gca().invert_yaxis()
plt.ylabel("Popular words")
plt.xlabel("Number of uses")
plt.title("Tweet Text Frequency Analysis")
plt.show()


