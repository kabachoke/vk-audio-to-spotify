import scripts.vkparser, scripts.spotify, json


def main():
    with open('config.json', 'r', encoding='utf-8') as cfg:
        data = json.load(cfg)
        login = data['vklogin']
        password = data['vkpassword']
        owner_id = data['vkownerid']
        scripts.vkparser.ParseAudio(login, password, owner_id)
        scripts.spotify.main('parsed/parsedmusic.json', 'b69a5e81d56f485a9e5dc9ee9d005543')

        with open('parsed/tracksNotFoundInSpotify.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            percent = data[len(data) - 1]['countOfFoundTracksInPercent']
            file.close()
        print('VKAudioParserToSpotify закончил свою работу.')
        print('Файл parsed/tracksNotFoundInSpotify содержит информацию о треках, не найденных данным приложением.')
        print('Процентное количество найденных треков: {}'.format(percent))
        print('Нажмите любую клавишу для закрытия окна.')
        input()

if (__name__ == '__main__'):
    main()