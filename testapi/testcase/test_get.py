# encoding=gbk
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
        log.printInfo('�ӿڵ��ÿ�ʼ:�����url�ǣ�{}�������ǣ�{},ƴ�Ӻ��url��ַ�ǣ�{}{},case_id��{}'.format(url,params,url,params,case_id))
        response = api.get(url,params)
        log.printInfo('�ӿ�ʵ�ʷ��ؽ����{}'.format(response))
        log.printInfo('�ӿڵ�Ԥ�ڽ����%s' % yuqi)
        if response == yuqi:
            log.printInfo('ʵ�ʷ��ؽ����Ԥ�ڽ��У��Ϊ��True')
            result1='Pass'
        else:
            log.printInfo('ʵ�ʷ��ؽ����Ԥ�ڽ��У��Ϊ: False')
            result1='Fail'
        assert response == yuqi
        self.r.wr_excel('get_case',case_id,response,result1)




if __name__ == '__main__':
    if os.path.exists('../report/xml'):
        shutil.rmtree('../report/xml')
        print('xml�ļ����Ѵ��ڣ�ɾ���ɹ���')
    else:
        pytest.main(['test_get.py', '-v', '--alluredir', '../report/xml/'])
        time.sleep(10)
        os.system('allure generate ../report/xml -o ../report/allurehtml --clean')
