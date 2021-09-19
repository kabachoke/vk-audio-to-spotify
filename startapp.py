import scripts.vkparser, json


def main():
    with open('config.json', 'r', encoding='utf-8') as cfg:
        data = json.load(cfg)
        login = cfg['vklogin']
        password = cfg['vkpassword']
        owner_id = cfg['vkownerid']
        scripts.vkparser.ParseAudio(login, password, owner_id)

if (__name__ == '__main__'):
    main()