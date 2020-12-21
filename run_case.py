import unittest
from HTMLTestRunner import HTMLTestRunner
from setting import TEST_REPORT_PATH, LOGIN_INFO
from api.user_manager import UserManager


if __name__ == '__main__':
    UserManager().login(LOGIN_INFO.get('username'), LOGIN_INFO.get('password'))

    suite = unittest.TestLoader().discover('./cases', 'test*.py')

    with open(TEST_REPORT_PATH, 'wb') as f:

        runner = HTMLTestRunner(f, title='测试报告')
        runner.run(suite)