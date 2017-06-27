from pprint import pprint
import shodan

from utilities import load_api_key

API_KEY = load_api_key('shodan')
query = 'Quanta'


api = shodan.Shodan(API_KEY)
count_result = api.count(query)
pprint(count_result)

search_result = api.search(query, 1)

for entry in search_result['matches']:
    print('{}:{}'.format(entry['ip_str'], entry['port']))

