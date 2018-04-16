__author__ = 'solin'
import logging,os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#增加全局变量
from conf import setting

def log():
    log_file = '%s\logs\logger.log'%(setting.BASE_DIR)#定义日志输出文件路径
    logger = logging.getLogger('authlog')
    fh = logging.FileHandler(log_file,encoding='utf-8')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

