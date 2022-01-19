import time
# from common.log_cases import loger
from common.log import log
from common.get_project_path import output_path


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        self.base_url = 'http://localhost:5001/ECShop_V2.7'
        self.logger = log

    def find_element(self, locator):
        try:
            self.logger.info('开始查找元素{}'.format(locator))
            ele = self.driver.find_element(*locator)
            self.logger.info('查找成功')
            return ele
        except Exception as err:
            # 记录日志，截屏
            self.logger.error('查找元素失败')
            self.logger.error(err)
            self.screenshot()
            raise
        pass

    def click(self, locator):
        ele = self.find_element(locator)
        try:
            self.logger.info('开始点击元素{}'.format(locator))
            ele.click()
            self.logger.info('点击成功')
            return ele
        except Exception as err:
            # 记录日志，截屏
            self.logger.error('点击元素失败')
            self.logger.error(err)
            self.screenshot()
            raise
        pass

    def send_keys(self, locator, value):
        ele = self.find_element(locator)
        try:
            self.logger.info('开始输入元素{}'.format(locator))
            ele.send_keys(value)
            self.logger.info('输入成功')
            return ele
        except Exception as err:
            # 记录日志，截屏
            self.logger.error('输入元素失败')
            self.logger.error(err)
            self.screenshot()
            raise
        pass

    def screenshot(self):
        str1 = time.strftime('%Y%m%d%H%M%S')
        filename = output_path+'/screenshot'+str1+'.png'
        self.driver.get_screenshot_as_file(filename)
        self.logger.info('截屏并保存到文件'+filename)
        pass

    pass
