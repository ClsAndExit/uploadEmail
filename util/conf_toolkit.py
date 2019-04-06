# coding:utf-8
#@Time    :2019/3/31 15:44
import configparser


class ConfigManager:
    conf = configparser.ConfigParser()

    @classmethod
    def init_class(cls, config_path):
        cls.conf.read(config_path)

    @classmethod
    def _get(cls, section, key):
        return cls.conf.get(section, key)

    @classmethod
    def get_local_resource_folder(cls):
        return cls._get("file", "local_resource_folder")

    @classmethod
    def get_email_username(cls):
        return cls._get("password", "email_username")

    @classmethod
    def get_email_password(cls):
        return cls._get("password", "email_passwowrd")

    @classmethod
    def get_email_server(cls):
        return cls._get("server", "pop3_server")
