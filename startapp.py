import scripts.vkparser, scripts.spotify, json


def main():
    with open('config.json', 'r', encoding='utf-8') as cfg:
        data = json.load(cfg)
        login = data['vklogin']
        password = data['vkpassword']
        owner_id = data['vkownerid']
        scripts.vkparser.ParseAudio(login, password, owner_id, data['CountOfParsedTracks'])
        scripts.spotify.main('parsed/parsedmusic.json', 'b69a5e81d56f485a9e5dc9ee9d005543')

if (__name__ == '__main__'):
    main()