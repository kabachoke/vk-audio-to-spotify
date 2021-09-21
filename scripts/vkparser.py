import scripts.jsonregex
from vk_api import audio
import vk_api, json


def VKAudioInit(login, password):
    vk_session = vk_api.VkApi(login=login, password=password)
    vk_session.auth()                   
    vk_audio = audio.VkAudio(vk_session)
    
    return vk_audio


def GroupTracks(path):
    with open(path, 'r', encoding='utf-8') as file:
        with open('config.json', 'r', encoding='utf-8') as cfg:
            data = json.load(cfg)
            countOfTracksToPlaylist = data['ValueAtWhichThePlaylistIsCreated']
        data = json.load(file)
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
            if (k >= countOfTracksToPlaylist):
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
    file.close()

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(groupedData, file, ensure_ascii=False, indent=4)


def ParseAudio(login, password, owner_id, count): 
    path = 'parsed/parsedmusic.json'

    vk_audio = VKAudioInit(login, password)
    print('Авторизация VK прошла успешно.')
    musicList = vk_audio.get_iter(owner_id=owner_id)
    serializeList = []
    k = 0

    for music in musicList:
        if (k < count):
            serializeList.append({
                'Artist' : music['artist'],
                'Title' : music['title']
                })
            k += 1
        else:
            break

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(serializeList, f, ensure_ascii=False, indent=4)
        f.close()
    
    print('Треки из VK получены успешно')

    scripts.jsonregex.FormatJson(path)
    GroupTracks(path)