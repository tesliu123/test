import yaml

'''读取yaml配置文件'''


class ReadYaml():
    def __init__(self, file_Path):
        self.conf = open(file_Path, 'r', encoding='utf-8')
        self.str_conf = self.conf.read()

    def get_driver(self, yaml_name):
        dict_conf = yaml.load(self.str_conf, Loader=yaml.Loader)
        driver = dict_conf[yaml_name]['driver']
        return driver

    def get_url(self, yaml_name):
        dict_conf = yaml.load(self.str_conf, Loader=yaml.Loader)
        url = dict_conf[yaml_name]['url']
        return url

    def get_path(self, yaml_name):
        dict_conf = yaml.load(self.str_conf, Loader=yaml.Loader)
        path = dict_conf[yaml_name]['path']
        return path

    def get_sendmail(self, yaml_name):
        dict_conf = yaml.load(self.str_conf, Loader=yaml.Loader)
        sendmail = dict_conf[yaml_name]['sendmail']
        return sendmail


if __name__ == '__main__':
    c = ReadYaml('../fileConfig/config.yaml')
    print(c.get_driver('guge'))
    print(c.get_sendmail('guge'))
