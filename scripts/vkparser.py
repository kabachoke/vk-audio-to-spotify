import scripts.jsonregex
from vk_api import audio
import vk_api, json


def GroupTracks(path):
    with open(path, 'r', encoding='utf-8') as s:
        data = json.load(s)
        groupedData = []
        for i in data:
            isContinue = False
            for m in groupedData:
                if m['IsPlaylist'] == True and m['Artist'] == i['Artist']:
                    isContinue = True
                    break
            if isContinue:
                continue
            artist = i['Artist']
            k = 0
            Tracks = []
            for j in data:
                if artist == j['Artist']:
                    k += 1
                    Tracks.append({
                        'Title' :  j['Title'],
                        'Id' : ''
                    })
            if (k > 2):
                groupedData.append({
                    'IsPlaylist' : True,
                    'Artist' : artist,
                    'Id' : '',
                    'Tracks' : Tracks
                })
            else:
                groupedData.append({
                    'IsPlaylist' : False,
                    'Artist' : i['Artist'],
                    'Title': i['Title'],
                    'Id' : ''
                })
    with open ('parsed/groupedtracksnew.json', 'w', encoding='utf-8') as f:
        json.dump(groupedData, f, ensure_ascii=False, indent=4)


def VKAudioInit(login, password):
    vk_session = vk_api.VkApi(login=login, password=password)
    vk_session.auth()
                                     
    vk_audio = audio.VkAudio(vk_session)
    return vk_audio

def ParseAudio(login, password, owner_id): 
    path = 'parsed/parsedmusic.json'
    vk_audio = VKAudioInit(login, password)

    musicList = vk_audio.get(owner_id=owner_id)
    serializeList = []

    for music in musicList:
        serializeList.append({
            'Artist' : music['artist'],
            'Title' : music['title']
            })

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(serializeList, f, ensure_ascii=False, indent=4)

    scripts.jsonregex.FormatJson(path)
    GroupTracks(path)