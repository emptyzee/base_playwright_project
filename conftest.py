import pytest
from dotenv import load_dotenv


load_dotenv() #использовать локально, но сначала pip install python-dotenv

pytest_plugins = [
    'fixtures.page',
    'fixtures.auth'
]