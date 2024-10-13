import configparser

config=configparser.RawConfigParser()
config.read(r'C:\Users\Rafi Ornob\PycharmProjects\honeywell\config_files\config.ini')
#config_object.read(r'C:\Users\Rafi Ornob\PycharmProjects\PeopleAPI-FrameWork\Configuration\config.ini')

class Read_config:
    @staticmethod
    def admin_page_url():
        url=config.get('admin login info','admin_page_url')
        return url

    @staticmethod
    def valid_user_name():
        vusername=config.get('admin login info', 'username')
        return vusername
    @staticmethod
    def valid_password():
        vpass=config.get('admin login info', 'password')
        return vpass;
    @staticmethod
    def invalid_user_name():
        invalid_user=config.get('admin login info', 'invalid_username')
        return invalid_user
