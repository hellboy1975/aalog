"""
class to access the config files
At the moment there are two:
    * user.config
    * system.config
Config will use the standard librarly ConfigParser
https://docs.python.org/3/library/configparser.html#module-ConfigParser
"""
import configparser

SYSTEM_CONFIG_FILE = "settings/system.ini"

class Config:
    """ parent class containing shared functionality """

    def __init__(self):
        self.parser = configparser.ConfigParser()

    def load(self, file):
        """ loads the system config file """
        self.config = self.parser.read(file)

    def save(self, file):
        """ saves the requested config file """
        self.parser.write(file)

class SystemConfig(Config):
    """ Class to access system config values """
    
    def __init__(self):
        super().__init__()
        self.load(SYSTEM_CONFIG_FILE)

class UserConfig(Config):
    """ Class to access user config values """

    def __init__(self, user_config_file):
        super().__init__()
        self.load(user_config_file)
