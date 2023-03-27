import logging

# level 表示设置的日志等级
# format 表示日志的输出格式，参数说明：
#   %(levelname)s：打印日志级别名称
#   %(filename)s：打印当前执行程序名
#   %(lineno)d：打印日志的当前行号
#   %(asctime)s：打印日志的时间
#   %(message)s：打印日志信息
# filename 表示日志保存路径
# filemode
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
