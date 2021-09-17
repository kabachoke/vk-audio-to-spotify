from scripts.jsonregex import FormatJson
from vk_api import audio
import vk_api, json

def VKAudioInit(login, password):
    vk_session = vk_api.VkApi(login=login, password=password)
    vk_session.auth()
                                     
    vk_audio = audio.VkAudio(vk_session)
    return vk_audio

def ParseAudio(login, password, owner_id): 
    vk_audio = VKAudioInit(login, password)

    musicList = vk_audio.get(owner_id=owner_id)
    serializeList = []

    for music in musicList:
        serializeList.append({
            'Artist' : music['artist'],
            'Title' : music['title']
            })

    with open('parsedmusic.json', 'w', encoding='utf-8') as f:
        json.dump(serializeList, f, ensure_ascii=False, indent=4)

    FormatJson('parsed/parsedmusic.json')