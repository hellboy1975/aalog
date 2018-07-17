"""
This package will access the yaml file used for user settings
"""
from yaml import load, dump

DEFAULT = """
    email: test@test.com
    nickname: test
    first_name: Test
    last_name: McTestFace
"""

def check_for_config(config = USER_SETTINGS_FILE):    
    with open(USER_SETTINGS_FILE) as stream:
        try:
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)

def load_user_config(config=USER_SETTINGS_FILE):
    file = yaml.load(config)

check_for_config()
