import json

url_resources = 'resources/'

url_icon = f'{url_resources}icon.ico'
url_logo = f'{url_resources}logo.png'
url_logo_database = f'{url_resources}logo_db_browser.png'
url_flag_eng = f'{url_resources}eng.png'
url_flag_spa = f'{url_resources}spa.png'
url_data = f'{url_resources}data'
url_back = f'{url_resources}back1.png'
url_right_arrow = f'{url_resources}right_arrow.svg'
url_save = f'{url_resources}floppy.svg'
url_plus = f'{url_resources}plus3.png'
url_minus = f'{url_resources}minus.png'
url_cross = f'{url_resources}cross1.svg'
url_loading = f'{url_resources}loading.gif'
url_loading_mini = f'{url_resources}loading_mini.gif'
url_tick = f'{url_resources}tick.png'
url_interrogation = f'{url_resources}interrogation.png'


def get_language_code():
    return json_load()['language_code']


def get_last_user():
    return json_load()['last_user']


def json_dump(data):
    with open(url_data, 'w') as file:
        json.dump(data, file)


def json_load():
    with open(url_data) as file:
        data = json.load(file)
    return data


def set_language_code(lang_code):
    data = json_load()
    data['language_code'] = lang_code
    json_dump(data)


def set_last_user(user_name):
    data = json_load()
    data['last_user'] = user_name
    json_dump(data)


class MyStrings:
    def __new__(cls):
        language_code = get_language_code()
        if language_code == 'eng':
            from resources.languages.english import English
            my_strings = English()
        else:
            from resources.languages.spanish import Spanish
            my_strings = Spanish()
            # raise Exception('Invalid language code')
        return my_strings
