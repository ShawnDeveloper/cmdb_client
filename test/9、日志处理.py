import logging

'''单文件日志
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log.txt')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
'''
#
# # 定义文件
# file_1_1 = logging.FileHandler('l1_1.log', 'a', encoding='utf-8')
# fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
# file_1_1.setFormatter(fmt)
#
# file_1_2 = logging.FileHandler('l1_2.log', 'a', encoding='utf-8')
# fmt = logging.Formatter()
# file_1_2.setFormatter(fmt)
#
# # 定义日志
# logger1 = logging.Logger('s1', level=logging.DEBUG)
# logger1.addHandler(file_1_1)
#
# logger2 = logging.Logger('s2', level=logging.DEBUG)
# logger2.addHandler(file_1_2)
#
#
# # 写日志
# logger1.critical('1111')
# logger2.error('1111')

import datetime
print(datetime.datetime)