import json
import requests

import sys

# if len(sys.argv) !=2:
#     sys.exit()
    
# response = requests.get('https://itunes.apple.com/search?entity=song&limit=50&term=' + sys.argv[1])
# # print(json.dumps(response.json(), indent=4))

# o = response.json()
# for result in o['results']:
#     print(result['trackName'])

response_1 = requests.get('https://dummyjson.com/products')
# print(json.dumps(response_1.json(), indent=4))
prod = response_1.json()
import csv
for p in prod['products']:
    title = p['title']
    price = p['price']
    
    with open('json_products.csv', 'a', newline='') as file:
        file.write(f'{title},{price}\n')