__author__ = 'Administrator'

import logging
import os
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#定义全局环境变量，指定文件绝对路径
#print(BASE_DIR)



#定义一个数据字典，可以改变数据库类型
DATABASE = {
    'db_tool':'file',#数据库类型
    'name':'userinfo',#库名
    'path':'%s\db'%BASE_DIR#绝对路径
}
