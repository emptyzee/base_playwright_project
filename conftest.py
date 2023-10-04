from dotenv import load_dotenv


load_dotenv() #нужно, чтобы  переменные окружения, такие как логины/пароли/api tokens  не хранились в коде, а подгружались
# из файла .env, актуально только для локальных прогонов, для запуска через CI, переменные храняться в secrets.

pytest_plugins = [
    'fixtures.page',
    'fixtures.user_auth'
]
