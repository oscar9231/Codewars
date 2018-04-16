__author__ = 'Administrator'

def file(database):
    '''定义文件形式数据库函数，返回文件数据库的绝对路径'''
    file_path = '%s\%s'%(database['path'],database['name'])
    #print(file_path)
    return file_path
def mysql(database):
    '''定义mysql形式数据库函数，返回mysql数据库的绝对路径'''
    mysql_path = '%s\%s'%(database['path'],database['name'])
    #print(mysql_path)
    return mysql_path
def control(database):
    '''定义数据库形式函数，如果传来的值为file，返回file函数中的文件数据库的绝对路径'''
    if database['db_tool'] == 'file':
        return file(database)
    elif database['db_tool'] == 'mysql':
        return mysql(database)


