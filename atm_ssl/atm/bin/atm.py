__author__ = 'Administrator'
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#增加全局变量
from core import main
#执行main程序中的run函数
main.run()
