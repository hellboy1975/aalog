"""
class to access the config files
At the moment there are two:
    * user.config
    * system.config
Config will use the standard librarly ConfigParser
https://docs.python.org/3/library/configparser.html#module-ConfigParser
"""
import configparser

parser = configparser.ConfigParser()

SYSTEM_CONFIG_FILE = "settings/system .ini"

class Config:
    """ parent class containing shared functionality """
    
    def load(self, file):
        """ loads the system config file """
        self.config = parser.read(file)
        self.file = file

    def save(self, file):
        """ saves the requested config file """
        config.write(file)

class SystemConfig(Config):
    """ Class to access system config values """

    def __init__(self):
        config = self.load(SYSTEM_CONFIG_FILE)
        
        #check that the file exists
        self.exists = False
        if config:
            self.exists = True

class UserConfig(Config):
    """ Class to access user config values """

    def __init__(self):
        self.load(SYSTEM_CONFIG_FILE)
