import os


class Constants:
    TEACHER_DATA = {
        "login_shot": "teacher5@uchi.ru",
        "password_shot": "12345678"
    }

    try:
        login2 = os.getenv('PROD_LOGIN1')
        password2 = os.getenv('PROD_PW1')
    except KeyError:
        print("LOGIN OR PW WASN'T FOUND")

    try:
        key = os.getenv('API_KEY')
    except KeyError:
        print("API KEY wasn't found")