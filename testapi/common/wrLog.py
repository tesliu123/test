import logging
import os
import time


class Log:
    def __init__(self):
        self.logger = logging.getLogger()  # 创建logger
        self.logger.setLevel(logging.INFO)  # 日志root等级
        self.log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/logs/'  # 日志目录,os.path.dirname():去掉文件名，返回目录（D:\pyworkspace\common），os.path.realpath(__file__)：获取当前执行脚本的绝对路径（D:\pyworkspace\common\wrLog.py）

        # 日志内容格式
        self.formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        if os.path.exists(self.log_path) == False:  # 目录不存在就创建，s.path.exists(path):如果path存在，返回True;如果path不存在，返回False
            os.makedirs(self.log_path) #os.makedirs()创建多层目录，目录不存在报错FileExistsError;os.mkdir()只创建最外层目录


    def printLog(self, log_type, log_content):  # 输出日志
        logTime = time.strftime('%Y%m%d%H', time.localtime(time.time()))  # 当前时间到小时，time.time():返回当前时间的时间戳；time.localtime():转换成元组形式的时间格式；time.strftime():接收元组格式时间，转换成字符串格式
        log_file = self.log_path + logTime + '.txt'  # 文件名
        if os.path.exists(log_file) == False:  # 日志文件不存在就创建
            fd = open(log_file, mode="w", encoding="utf-8")
            fd.close()

        handler = logging.FileHandler(log_file, mode='a')
        handler.setLevel(logging.DEBUG)  # handler的日志等级
        handler.setFormatter(self.formatter)  # 设置日志格式
        self.logger.addHandler(handler)  # 添加handler

        if log_type == 'info':
            self.logger.info(log_content)
        elif log_type == 'warning':
            self.logger.warning(log_content)
        elif log_type == 'error':
            self.logger.error(log_content)
        else:
            self.logger.critical(log_content)
        self.logger.removeHandler(handler)  # 记得删除handler防止重复打印

    def printInfo(self, log_content):
        self.printLog('info', log_content)

    def printWarning(self, log_content):
        self.printLog('warning', log_content)

    def printError(self, log_content):
        self.printLog('error', log_content)

    def printCritical(self, log_content):
        self.printLog('critical', log_content)


if __name__ == '__main__':
    Log = Log()
    Log.printInfo('不')
    Log.printWarning('点')
    Log.printError('赞')
    Log.printCritical('吗')

