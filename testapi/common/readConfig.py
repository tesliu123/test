from configparser import ConfigParser, DuplicateSectionError

'''读取ini配置文件'''


class ReadConfig:

    def __init__(self, configPath):
        self.cf = ConfigParser()
        self.configPath = configPath
        self.cf.read(self.configPath, encoding='utf-8')

    def get_http(self, name):
        value = self.cf.get('HTTP', name)
        return value

    def get_datebase(self, name):
        value = self.cf.get('DATABASE', name)
        return value

    def get_email(self, name):
        value = self.cf.get('EMAIL', name)
        return value

    def get_api(self, name):
        value = self.cf.get('API', name)
        return value

    def wr_content(self, selection, key, value):
        try:
            selctions = self.cf.sections()
            self.cf.add_section(selection)
            if selection not in selctions:
                self.cf.set(selection, key, value)
                self.cf.write(open(self.configPath, 'w', encoding='utf-8'))
                print('写入完成！')
        except DuplicateSectionError:
            print('selction:%s已存在，无法写入！' % selection)




if __name__ == '__main__':
    c = ReadConfig('../fileConfig/config.ini')
    print(c.get_email('mail_port'))
    c.wr_content('测试2', 'a1', '11')
