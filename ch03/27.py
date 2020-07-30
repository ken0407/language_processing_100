import json
import re

with open('../data/jawiki-country.json', mode='r') as f:
    for line in f:
        country_info = json.loads(line)
        if country_info['title'] == 'イギリス':
            england_text = country_info['text']
            break

informations = re.findall(r"(?<=\|).+ =.+", england_text)
info_dict = {}
for information in informations:
    tmp = information.split('=')
    key, value = tmp[0].replace(' ', ''), tmp[1]
    if value[0] == ' ':
        value = value[1:]
        value = value.replace("'''", '').replace("'''''", '').replace('[[', '').replace(']]', '')
    info_dict.update({key: value})

print(info_dict)
