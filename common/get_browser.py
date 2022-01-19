from selenium import webdriver
from common.get_datas import get_data_from_conf
from common.get_project_path import driver_path, conf_path


filename = conf_path+'/browser.ini'
browser_type = get_data_from_conf(filename, 'chrome', 'browser_type')
timeout = int(get_data_from_conf(filename, 'chrome', 'timeout'))


def get_driver():
    if browser_type.lower() == 'chrome':
        path = driver_path+'/chromedriver.exe'
        driver = webdriver.Chrome(executable_path=path)
    elif browser_type.lower() == 'firefox':
        path = driver_path+'/geckodriver.exe'
        driver = webdriver.Firefox(executable_path=path)
    else:
        path = driver_path+'/IEDriverServer.exe'
        driver = webdriver.Ie(executable_path=path)
    driver.implicitly_wait(timeout)
    driver.maximize_window()
    return driver
    pass

