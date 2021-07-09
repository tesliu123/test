
# coding=utf-8
import shutil
import pytest
import time
import os


if __name__ == '__main__':
    if os.path.exists('../report/xml'):
        shutil.rmtree('../report/xml')
        print('xml文件夹已存在，删除成功！')
    else:
        pytest.main(['../testcase/test_get.py', '-v', '--alluredir', '../report/xml'])
        time.sleep(10)
        os.system('allure generate ../report/xml -o ../report/allurehtml --clean')
