#There are some holes in how I'm getting
#to the total sentiment score (plus so many words used aren't in
#the sentiment dictionary!), but it's a work in progress and
#all just for good fun/learning!

import requests
import pprint

#Print user Menu and ask user what they want to do
print "What would you like to do?"
print "1: Search sentiment score by a state"
print "2: List total sentiment score for all states"

user_choice = raw_input("What would you like to do? Enter number code: ")

#To create word sentiment dictionary
sentiment_dict = {}
with open('AFINN-111.txt', 'r') as afinn:
	for line in afinn:
		word, score = line.strip().split("\t")
		sentiment_dict[word] = score


# Sentiment score by state
if int(user_choice) == 1:
	#General paramaters and API calling
	query_params = { 'apikey': 'Replace with your own API key! :)',
				 	'per_page': 75,
				 	'sort': 'count desc',
				 	'entity_type': 'state',
				 	'entity_value': 'to_be_replaced'
		 			}

	endpoint = 'http://capitolwords.org/api/phrases.json'
	query_params['entity_value'] = raw_input("Enter state abbreviation: ")

	response = requests.get(endpoint, params=query_params)
	data = response.json()

	

	sentiment_score = 0
	for i in data:
		if i['ngram'] in sentiment_dict:
			sentiment_score += int(sentiment_dict[i['ngram']])

	text_to_print = """
	The total sentiment score for %s's top 75 most used words is %i
	""" 

	print text_to_print %(query_params['entity_value'], sentiment_score)


# List all states' sentiment scores
elif int(user_choice) == 2:
	#General paramaters and API calling
	query_params = { 'apikey': '9aee1f7c1dbe4cda8066111b55935de8',
				 	'sort': 'count desc',
				 	'entity_type': 'state',
				 	'entity_value': 'to_be_replaced'
		 			}

	endpoint = 'http://capitolwords.org/api/phrases.json'
	states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC',
			'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
			'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT',
			'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH',
			'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
			'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


	states_dict = {}
	for state in states:
		sentiment_score = 0
		query_params['entity_value'] = state
		response = requests.get(endpoint, params=query_params)
		data = response.json()
		for i in data:
			if i['ngram'] in sentiment_dict:
				sentiment_score += int(sentiment_dict[i['ngram']])
		states_dict[state] = sentiment_score

	pprint.pprint(states_dict)


#User input not applicable
else:
	print "Input not applicable"