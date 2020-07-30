import json
import re

with open('../data/jawiki-country.json', mode='r') as f:
    for line in f:
        country_info = json.loads(line)
        if country_info['title'] == 'イギリス':
            england_text = country_info['text']
            break

infomations = re.findall(r"(?<=\|).+ =.+", england_text)
info_dict = {}
for infomation in infomations:
    tmp = infomation.split('=')
    key, value = tmp[0].replace(' ', ''), tmp[1]
    if value[0] == ' ':
        value = value[1:]
    value = value.replace('[[', '')\
                 .replace(']]', '')\
                 .replace('{{', '')\
                 .replace('}}', '')\
                 .replace('<ref name', '')\
                 .replace("'''", '')\
                 .replace("'''''", '')
    find = re.findall(r'.+\|.*', value)
    if find:
        value = find[0].split('|')[-1]
    info_dict.update({key: value})

print(info_dict)
