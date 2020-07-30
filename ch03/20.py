import json

with open('../data/jawiki-country.json', mode='r') as f:
    for line in f:
        country_info = json.loads(line)
        if country_info['title'] == 'イギリス':
            print(country_info['text'])
            break
