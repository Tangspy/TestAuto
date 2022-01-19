import unittest
from pages.login_page import LoginPage
from common.get_browser import get_driver


class TestLoginPage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()

    def tearDown(self) -> None:
        self.driver.quit()

    # 正常登陆
    def test_login(self):
        login = LoginPage(self.driver)
        login.login('ufo', '123456')
        # ele = self.driver.find_element_by_xpath('//div[@class=\'boxCenterList RelaArticle\']/div/p')
        # self.assertEqual("登录成功", ele.text)
        self.assertEqual("登录成功", login.get_login_tip())


if __name__ == '__main__':
    unittest.main()
