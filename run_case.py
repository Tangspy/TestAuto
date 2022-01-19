import unittest
import HTMLReport
import BeautifulReport
from test_cases.test_login_page import TestLoginPage


def run_report():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLoginPage)
    file = open('test_report.log', 'w')
    # TextTestRunner()自带的报告
    # stream=None（写入的文件）, descriptions=True（描述信息）, verbosity=1（日志输出详细程度）
    unittest.TextTestRunner(file, verbosity=2).run(suite)
    pass


def run_HTMLReport():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLoginPage)
    # 执行
    runner = HTMLReport.TestRunner(report_file_name='自动化测试报告')
    runner.run(suite)


def run_BeautifulReport():
    # case = TestLoginPage.test_login()
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLoginPage)
    # 执行
    runner = BeautifulReport.BeautifulReport(suite)
    # description, filename: str = None, report_dir='.'
    runner.report('自动化执行结果', filename='ecshop自动化结果报告', report_dir='./output')


if __name__ == '__main__':
    # run_report()
    # run_HTMLReport()
    run_BeautifulReport()
