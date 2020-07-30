import json
import re

with open('../data/jawiki-country.json', mode='r') as f:
    for line in f:
        country_info = json.loads(line)
        if country_info['title'] == 'イギリス':
            england_text = country_info['text']
            break

sections = re.findall(r'=+\w+=+', england_text)
for section in sections:
    print(f"{section.replace('=', '')}: {int(section.count('=')//2)-1}")
