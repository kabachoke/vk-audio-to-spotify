import json, re

def FormatJson(path):
    with open(path, 'r+', encoding='utf-8') as file:
        my_regex = "\[.*\]|\(.*\)"
        data = json.load(file)
    
        for i in data:
            i['Artist'] = re.sub(my_regex, "", i['Artist']).strip(' ')
            i['Title'] = re.sub(my_regex, "", i['Title']).strip(' ')
                     
        json.dump(data, file, ensure_ascii=False, indent=4)