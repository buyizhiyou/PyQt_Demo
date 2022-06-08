import logging
import colorlog


def ms_to_time(millis):
    '''
    ms 转 hours:minutes:seconds
    '''
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24
    hours = int(hours)
    lay = millis - hours*1000 * 60 * 60 - minutes*1000 * 60 - seconds*1000

    return("%d:%d:%d.%d" % (hours, minutes, seconds, lay))


def contains_chinese(strs):
    '''
    判断字符串是否包含汉字
    '''
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


# 定义不同日志等级颜色
log_colors_config = {
    'DEBUG': 'bold_cyan',
    'INFO': 'bold_green',
    'WARNING': 'bold_yellow',
    'ERROR': 'bold_red',
    'CRITICAL': 'red',
}


class Logger(logging.Logger):
    def __init__(self, name=None, level='DEBUG', encoding='utf-8'):
        super().__init__(name)
        self.encoding = encoding
        self.level = level
        # 针对所需要的日志信息 手动调整颜色
        formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(asctime)s [%(filename)s:%(''lineno)d] %(log_color)s%(levelname)s:%(message)s',
            reset=True, log_colors=log_colors_config,
            secondary_log_colors={
                'message': {
                    'DEBUG': 'blue',
                    'INFO': 'blue',
                    'WARNING': 'blue',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_red'
                }
            },
            style='%'
        )  # 日志输出格式
        if(name):
            # 创建一个FileHandler，用于写到本地
            rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=self.name,
                                                                       maxBytes=1024 * 1024 * 50,
                                                                       backupCount=5)
            rotatingFileHandler.setFormatter(
                logging.Formatter('%(asctime)s [%(filename)s:%(''lineno)d] %(levelname)s:%(message)s'))
            rotatingFileHandler.setLevel(logging.DEBUG)
            self.addHandler(rotatingFileHandler)
        # 创建一个StreamHandler,用于输出到控制台
        console = colorlog.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(formatter)
        self.addHandler(console)
        self.setLevel(logging.DEBUG)
