import logging
from common.get_project_path import output_path


def get_logger():
    # 创建logger对象
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        # 用于输出至文件
        filename = output_path + '/run.log'
        # 日志格式设置---Formatter
        formatter = logging.Formatter(fmt='%(filename)s %(asctime)s %(message)s')
        handler = logging.FileHandler(filename)  # 日志信息写入到info.log文件
        handler.setLevel(logging.INFO)  # 设置写入文件日志信息等级
        handler.setFormatter(formatter)  # 日志信息打印格式设置
        # 打印到控制台---StreamHandler
        formatter2 = logging.Formatter(fmt='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s %(message)s')
        handler2 = logging.StreamHandler()
        handler2.setLevel(logging.INFO)
        handler2.setFormatter(formatter2)
        # logger绑定处理对象
        logger.addHandler(handler)
        logger.addHandler(handler2)
        return logger
    else:
        filename = output_path + '/run.log'
        # 日志格式设置---Formatter
        formatter = logging.Formatter(fmt='%(filename)s %(asctime)s %(message)s')
        handler = logging.FileHandler(filename)  # 日志信息写入到info.log文件
        handler.setLevel(logging.INFO)  # 设置写入文件日志信息等级
        handler.setFormatter(formatter)  # 日志信息打印格式设置
        # logger绑定处理对象
        logger.addHandler(handler)
        return logger
    pass


log = get_logger()  # 避免重复打印信息

