from configparser import ConfigParser


def config_reader(section, key):
    config = ConfigParser()
    config.read(".\\Configurations\\conf.ini")
    return config.get(section, key)
