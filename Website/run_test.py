import unittest
from HTMLTestRunnerNew import HTMLTestRunner

from Website.test_case.model.function import *

report_dir = filepath() + '/Website/test_report' + '/test_result'
test_dir = filepath() + '/Website/test_case'

print('start run testcase......')

discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*")
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + '_result.html'

print("start write report......")

with open(report_name, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title='自动化测试报告', description='360租房运营平台', tester='GanYu')
    runner.run(discover)

latest_report = latest_report(report_dir)

send_mail(latest_report)
print('test end!')
