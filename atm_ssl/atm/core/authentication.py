__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import os
import json,logging
from conf import setting
from core import db_connect
from core import logger



def authenticated(login_username,login_passwd,logger):

    '''验证登录模块，检验db中的用户信息
    '''
    db_path = db_connect.control(setting.DATABASE)
    logger.debug('读取数据连接方式')
    #print(db_path)
    user_file = '%s\%s.json'%(db_path,login_username)
    print((user_file))
    if os.path.exists(user_file):#判断用户文件是否尊在
        with open(user_file,'r',encoding='utf-8') as f1:
            user_dict = json.load(f1)
        #print(type(user_dict))
        if login_passwd == user_dict['password']:
            logger.info('信息认证成功')
            return user_dict
        else:
            print('密码错误')
            logger.info('密码输入错误')
    else:
        print('用户不存在')
        logger.info(('用户不存在'))

def login(user_tem_data,logger):
    '''判断临时字典，为False且小于三次执行authenticated函数,并把用户输入的用户名和密码传入'''
    count = 0
    if user_tem_data['is_authenticated'] == False and count <3:
        login_username = input('请输入用户名：').strip()

        login_passwd = input('请输入密码：').strip()
        user_data1 = authenticated(login_username,login_passwd,logger)
        count+=1
        user_tem_data['is_authenticated']= True
        #print(user_data1['status'])
        if user_data1['status']==1 or user_data1['status']==2:
            logger.info('%s认证完成，返回用户数据'%user_data1['id'])
            return user_data1
        else:
            print('用户未激活')
            logger.warning('用户未激活')


