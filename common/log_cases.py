import logging
from common.get_project_path import output_path


def get_loger():
    # 创建logger对象
    loger = logging.getLogger()
    # 设置日志级别
    loger.setLevel(logging.INFO)  # 总开关，总要求等级
    # 设置日志分发---写入文件，打印到控制台

    # 日志格式设置---Formatter
    formatter = logging.Formatter(fmt='%(filename)s %(asctime)s %(message)s')

    # 写入文件---FileHandler
    # filename, mode='a', encoding=None
    filename = output_path+'/run.log'
    handler = logging.FileHandler(filename)  # 日志信息写入到info.log文件
    handler.setLevel(logging.INFO)  # 设置写入文件日志信息等级
    handler.setFormatter(formatter)  # 日志信息打印格式设置
    # 打印到控制台---StreamHandler
    formatter2 = logging.Formatter(fmt='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s %(message)s')
    handler2 = logging.StreamHandler()
    # handler2.setLevel(logging.INFO)
    handler2.setFormatter(formatter2)

    # 添加handler到logger
    loger.addHandler(handler)
    # loger.addHandler(handler2)
    return loger


loger = get_loger()  # 避免重复打印信息

