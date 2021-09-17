from vk_api.exceptions import VkApiError
import scripts.vkparser


def main():
    login = '+79264121417'
    password = 'misha905054'
    owner_id = '272513683'
    scripts.vkparser.ParseAudio(login, password, owner_id)

if (__name__ == '__main__'):
    main()