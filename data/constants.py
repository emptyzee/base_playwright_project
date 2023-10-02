import os


class Constants:
    try:
        login2 = os.getenv('PROD_LOGIN1')
        password2 = os.getenv('PROD_PW1')
    except KeyError:
        print("LOGIN OR PW WASN'T FOUND")