from selenium.webdriver.common.by import By
from pages.test_base_page import BasePage

'''
类---属性和方法
1、添加实例属性和方法
2、页面元素、元素的操作
3、元素的定位方式--locator(By.ID, value)
4、元素操作---基本，点击，输入，属性获取
5、
'''


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = webdriver.Chrome()  # 不能新建driver对象，调试代码可以放开，用完关掉
        self.url = self.base_url+'/upload/user.php'
        pass

    username = (By.NAME, 'username')
    password = (By.NAME, 'password')
    submit = (By.NAME, 'submit')
    tip = (By.XPATH, '//div[@class=\'boxCenterList RelaArticle\']/div/p')

    # locator = {"username": (By.NAME, 'username'),
    #            "password": (By.NAME, 'password'),
    #            "submit": (By.NAME, 'submit')
    # }

    def login(self, username, password):
        if self.driver.current_url != self.url:
            self.driver.get(self.url)
        self.send_keys(self.username, username)
        self.send_keys(self.password, password)
        self.click(self.submit)
        pass

    def get_login_tip(self):
        return self.find_element(self.tip).text

    pass
