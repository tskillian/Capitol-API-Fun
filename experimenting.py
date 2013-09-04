import requests


query_params = { 'apikey': 'taken out for github :)',
				 'per_page': 3,
				 'sort': 'count desc',
				 'entity_type': 'state',
				 'entity_value': 'to_be_replaced'
		 		}

endpoint = 'http://capitolwords.org/api/phrases.json'

query_params['entity_value'] = raw_input("Enter state abbreviation: ")

response = requests.get(endpoint, params=query_params)
data = response.json()

text_to_print = """
%s's most frequently used word is '%s'

"""


print text_to_print %(query_params['entity_value'], data[0]['ngram'])


