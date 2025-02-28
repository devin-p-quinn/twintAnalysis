import json
import pandas as pd
import matplotlib.pyplot as plt
import itertools


print("This tool is to be used in conjuction with the twint" + "\n")
print("output all twitter data into a json file" + "\n")
print("identify the path to the json file when prompted" + "\n")
print("This program returns the most common users in the json file" + "\n")
print("This can help identify key influencer on the subject you are analyzing" + "\n")

file_path = input("Enter file path to be analyzed: ")
num_top_u = int(input("Enter the number of top users to display: "))
graph_title = input("Enter the name of your table: ")

data = pd.read_json(file_path, lines=True)


def extract_users():
	# extracts the users from the twint JSON file
	users = []
	for username in data['username']:
		users.append(username)

	print(len(users))
	return users

def user_frequency():
	# counts how many times each user's name appears and elminates duplicates
	u_counts = {}
	users = extract_users()
	for u in users:
		if u in u_counts:
			u_counts[u] += 1
		else:
			u_counts[u] = 1
	return u_counts

def sort_users():
	# sorts the u_counts list into highest to lowest frequency
	res = {key: val for key, val in sorted(user_frequency().items(), key = lambda ele: ele[1], reverse = True)}
	return res

def truncate_sorted_users(top_users):
	# truncates the sorted list of users to the number specified when calling the method
	res2 = dict(itertools.islice(sort_users().items(), top_users))
	return res2

plt.barh(*zip(*truncate_sorted_users(num_top_u).items()))
plt.gca().invert_yaxis()
plt.ylabel("Key influncers")
plt.xlabel("Number of tweets")
plt.title(graph_title)
plt.show()

