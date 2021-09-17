import json, re

def FormatJson(path):
    with open(path, 'r', encoding='utf-8') as s:
        my_regex = "\[.*\]|\(.*\)"
        data = json.load(s)
    
        for i in data:
            i['Artist'] = re.sub(my_regex, "", i['Artist']).strip(' ')
            i['Title'] = re.sub(my_regex, "", i['Title']).strip(' ')
                     
        with open(path, 'w', encoding='utf-8') as f:
            f.write(json.dump(data, f, ensure_ascii=False, indent=4))