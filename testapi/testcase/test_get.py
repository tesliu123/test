# encoding=utf-8
import shutil

import pytest

from common.allApi import *
from common.readConfig import *
from common.wrLog import *
from common.readExcel import *
import time
import os

result = ReadConfig('../fileConfig/config.ini')
url = result.get_api('url')
api = Api()
log = Log()


class Test:
    r = ReadExcel()
    get_result = r.get_excel('get_case')

    @pytest.mark.parametrize('all_api', get_result)
    def test_get(self,all_api):
        case_id=int(all_api['case_id'])
        url=all_api['url']
        params=all_api['params']
        yuqi=all_api['yuqi']
        log.printInfo('接口调用开始:请求的url是：{}，参数是：{},拼接后的url地址是：{}{},case_id是{}'.format(url,params,url,params,case_id))
        response = api.get(url,params)
        log.printInfo('接口实际返回结果：{}'.format(response))
        log.printInfo('接口的预期结果：%s' % yuqi)
        if response == yuqi:
            log.printInfo('实际返回结果和预期结果校验为：True')
            result1='Pass'
        else:
            log.printInfo('实际返回结果与预期结果校验为: False')
            result1='Fail'
        assert response == yuqi
        self.r.wr_excel('get_case',case_id,response,result1)




# if __name__ == '__main__':
#     if os.path.exists('../report/xml'):
#         shutil.rmtree('../report/xml')
#         print('xml文件夹已存在，删除成功！')
#     else:
#         pytest.main(['test_get.py', '-v', '--alluredir', '../report/xml/'])
#         time.sleep(10)
#         os.system('allure generate ../report/xml -o ../report/allurehtml --clean')
