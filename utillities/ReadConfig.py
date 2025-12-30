import configparser

config = configparser.RawConfigParser()
config.read("D:\pro\CredKartFreamwork\Configuration\config.ini")


class ReadConfigClass:

    @staticmethod
    def get_data_for_email():
        email = config.get("login data","email")
        return email


    @staticmethod
    def get_data_for_password():
        password = config.get("login data","password")
        return password

    @staticmethod
    def get_application_url():
        login_url = config.get("application url","login_url")
        return login_url