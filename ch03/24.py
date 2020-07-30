import json
import re

with open('../data/jawiki-country.json', mode='r') as f:
    for line in f:
        country_info = json.loads(line)
        if country_info['title'] == 'イギリス':
            england_text = country_info['text']
            break

media_files = re.findall(r'(?<=\[\[ファイル:).*?(?=\|)', england_text)
print(media_files)
