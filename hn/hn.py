import json
import requests
import time

#Get your API Key from us (email anish)
API_KEY = ''

# Check README -- generated from external library
with open('links.json', 'r') as f:
    links = json.load(f)
links = links['links']

for d in links:
    
    #index comment
 #   data = {
 #       'link': d['comments_url'],
 #       'title': d['title'],
 #       'collection': 'anish@diva.so'
 #   }
 #   response = requests.post('https://mk1.diva.so:4242/addLink',
 #       json=data,
 #       headers={
 #           'Authorization': f"Bearer {API_KEY}",
 #           "Content-Type": "application/json",
 #           "Access-Control-Allow-Origin": "*"
 #       }
 #   )
 #   print(d['title'])
 #   print(response.status_code)
 #   print(response.text)
 #   time.sleep(1)

    #index actual
    if d['url'] != d['comments_url']:
        data = {
            'link': d['url'],
            'collection': 'anish@diva.so'
        }
        response = requests.post('https://mk1.diva.so:4242/addLink',
            json=data,
            headers={
                'Authorization': f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        )
        print(d['url'])
        print(response.status_code)
        print(response.text)


