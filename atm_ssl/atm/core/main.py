__author__ = 'Administrator'
from core import authentication
from conf import setting
from core import db_connect
from core import logger
import json,os,logging,datetime,time
#导入日志模块
use_log=logger.log()

user_tem_data = {
    'userid':None,
    'is_authenticated':False,
    'user_data':None
}
def withdraw(user_auth):#提现模块
    #print(user_auth)
    print('现在进入提款操作......')
    use_log.info('现在进入提款操作')
    choose1=float(input('请输入提款金额:').strip())*1.05#用户输入提款额后有百分之五利息
    withdraw_choose=float(choose1)
    withdraw_credit=float(user_auth["credit"])
    withdraw_balance=float(user_auth["balance"])
    #print(withdraw_money)
    if withdraw_choose <= withdraw_credit:#用户信息和用户输入信息做比对，如果在范围之内，则扣钱并将新信息写入文件
        if withdraw_choose<=withdraw_balance:
            db_path1 = db_connect.control(setting.DATABASE)
            withdraw_username=str(user_auth['id'])
            user_file1 = '%s\%s.json'%(db_path1,withdraw_username)
            #print(user_file1)
            with open(user_file1,'w',encoding='utf-8') as f2:
                user_auth['balance']=float(user_auth['balance'])-choose1
                print(user_auth)
                json.dump(user_auth,f2)
                print('交易成功,余额为%s'%user_auth['balance'])
                use_log.info('交易成功,余额为%s'%user_auth['balance'])
        else:
            print('交易失败,余额不足')
            use_log.warning('交易失败,余额不足')
    else:
        print('交易失败,余额不足')
        use_log.warning('交易失败,额度不足')

def repayment(user_auth):#还款模块，用户输入金额后直接更新用户信息写入文件
    print('现在进入还款操作......')
    use_log.info('现在进入还款操作')
    repaymenet_money=float(input('请输入还款金额:').strip())
    db_path2 = db_connect.control(setting.DATABASE)
    repayment_username=str(user_auth['id'])
    user_file2 = '%s\%s.json'%(db_path2,repayment_username)
    with open(user_file2,'w',encoding='utf-8') as f3:
        user_auth['balance']=float(user_auth['balance'])+repaymenet_money
        #print(user_auth)
        json.dump(user_auth,f3)
        print('交易成功,余额为%s'%user_auth['balance'])
        use_log.info('交易成功,余额为%s'%user_auth['balance'])
def transfer(user_auth):#转账模块，对用户输入转账id和输入金额进行判断，如果条件在范围内，就修改转账人文件和被转账人文件
    print('现在进入转账操作......')
    use_log.info('现在进入转账操作......')
    transuser_id=input('请输入用户id:').strip()
    db_path3 = db_connect.control(setting.DATABASE)
    user_file3 = '%s\%s.json'%(db_path3,transuser_id)
    transuser_file = '%s\%s.json'%(db_path3,user_auth['id'])

    trans_balance=float(user_auth["balance"])
    #print(user_file3)
    if os.path.exists(user_file3):
        trans_money=float(input('请输入转账金额:'))
        if trans_money<=trans_balance:
            with open(transuser_file,'w',encoding='utf-8') as f5:
                    user_auth['balance']=float(user_auth['balance'])-trans_money
                    #print(user_auth)
                    json.dump(user_auth,f5)

            with open(user_file3,'r',encoding='utf-8') as f4:
                transuser_info=json.load(f4)
                transuser_info["balance"]+=trans_money
                #print(transuser_info["balance"])
            with open(user_file3,'w',encoding='utf-8') as f6:
                json.dump(transuser_info,f6)
                print('交易成功，余额为%s'%user_auth['balance'])
                use_log.info('交易成功，余额为%s'%user_auth['balance'])
        else:
            print('余额不足，无法转账')
            use_log.warning('余额不足，无法转账')
    else:
        print('转账用户不存在')
        use_log.warning('转账用户不存在')

def logout(user_auth):#退出
    use_log.info('用户退出')
    exit()
def manager(manager_info):#管理员接口

    def useradd(manager_info):
        print('进入添加账户功能')
        use_log.info('进入添加账户功能')
        useradd_id=input('请输入需要添加用户id:').strip()
        db_path3 = db_connect.control(setting.DATABASE)
        useradd_file = '%s\%s.json'%(db_path3,useradd_id)
        if os.path.exists(useradd_file):
            use_log.info('用户名%s存在'%useradd_id)
            print('用户名%s存在'%useradd_id)
        else:
            useradd_info = {"id": useradd_id,
                            "password":'',
                            "credit": 0,
                            "balance": 0,
                            "enroll_date":'',
                            "status": 1}
            useradd_passwd = input('请输入新用户密码:').strip()
            useradd_info['password']=useradd_passwd
            useradd_credit = int(input('请输入额度:'))
            useradd_info['credit'] = useradd_credit
            with open(useradd_file,'w',encoding='utf-8') as f9:
                json.dump(useradd_info,f9)
            use_log.info('%s添加成功'%useradd_info['id'])
    def changecredit(manager_info):
        print('进入修改额度功能')
        use_log.info('进入修改额度功能')
        changecredit_id=input('请输入需要修改额度用户id:').strip()
        db_path3 = db_connect.control(setting.DATABASE)
        changecredit_file = '%s\%s.json'%(db_path3,changecredit_id)
        if os.path.exists(changecredit_file):
            with open(changecredit_file,'r',encoding='utf-8') as f10:
                credit_info=json.load(f10)
                change_credit = int(input('请输入额度:'))
                credit_info['credit']=change_credit
            with open(changecredit_file,'w',encoding='utf-8') as f11:
                json.dump(credit_info,f11)
                print('修改额度成功')
                use_log.info('%s修改额度成功'%credit_info['id'])
        else:
            print('用户不存在')
            use_log.warning('%s用户不存在'%changecredit_id)
    def lock(manager_info):
        print('进入修改用户状态功能')
        use_log.info('进入修改用户状态功能')
        lock_id=input('请输入需要修改用户id:').strip()
        change_status = input('请输入状态（激活1，未激活0，管理员2）:')
        if change_status =='1' or change_status =='0' or change_status =='2':
            db_path3 = db_connect.control(setting.DATABASE)
            lock_file = '%s\%s.json'%(db_path3,lock_id)
            if os.path.exists(lock_file):
                with open(lock_file,'r',encoding='utf-8') as f12:
                    credit_info=json.load(f12)
                    credit_info['status']=change_status
                with open(lock_file,'w',encoding='utf-8') as f13:
                    json.dump(credit_info,f13)
                    print('修改状态成功')
                    use_log.info('%s修改状态成功'%credit_info['id'])
            else:
                print('用户不存在')
                use_log.warning('%s用户不存在'%lock_id)
        else:
            print('输入状态码错误')
            use_log.warning('输入状态码错误')




    use_log.info('进入管理员模式中...')
    manager_information = '''
    ******INFOMATION******
    请选择管理功能：
    1、添加账户
    2、修改用户额度
    3、冻结账户
    '''
    print(manager_information,'\n')
    manager_menu = {
        '1':useradd,#添加账户
        '2':changecredit,#修改用户额度
        '3':lock,#冻结账户

    }
    while 1:
        if manager_info['status']== 2:
            select = input('请输入管理功能号码：').strip()
            if select in manager_menu:
                manager_menu[select](manager_info)
            else:
                print('号码不存在')
                use_log.warning('号码不存在')
        else:
            print('权限不足')
            use_log.warning('权限不足')
            break




def shops(user_auth):#购物商场
    log_file1 = '%s\logs\shopping.log'%(setting.BASE_DIR)#定义日志输出文件路径
    logger1 = logging.getLogger('shoppinglog')
    fh1 = logging.FileHandler(log_file1,encoding='utf-8')
    logger1.setLevel(logging.DEBUG)
    formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh1.setFormatter(formatter1)
    logger1.addHandler(fh1)


    use_log.info('%s进入购物商场...'%user_auth['id'])
    product_list = [('0-bike',100),('1-room',9900),('2-phone',3000)]#商品信息
    print('***购物列表***')
    print(product_list)
    while 1:
        product_num = input('请选择商品编号,按q退出:')
        if product_num.isdigit():
            productnum = int(product_num)
            #print((len(product_list)))
            if productnum <= len(product_list) and productnum>= 0:

                producklist = product_list[productnum]
                product_money = float(producklist[1])

                shops_pay = cart_pay(user_auth,product_money)
                print('%s已购入%s'%(user_auth['id'],producklist[0]))
                logger1.info('%s已购入%s'%(user_auth['id'],producklist[0]))

        elif product_num == 'q':
            use_log.info('%s退出购物车'%user_auth['id'])
            break

        else:
            print('输入商品编号有误')
            use_log.waring('%s输入商品编号有误'%user_auth['id'])

def cart_pay(user_info,product_money):#信用卡支付
    if float(user_info['balance']) >= product_money:

        db_path2 = db_connect.control(setting.DATABASE)
        payment_username=str(user_info['id'])
        user_file2 = '%s\%s.json'%(db_path2,payment_username)
        with open(user_file2,'w',encoding='utf-8') as f3:
            user_info['balance'] = user_info['balance']-product_money
            json.dump(user_info,f3)
            print('交易成功,余额为%s'%user_info['balance'])
            use_log.info('交易成功,余额为%s'%user_info['balance'])
        return user_info
    else:
        print('余额不足')
        use_log.warning('购买失败，余额不足')

def choose(user_auth):
    '''用于定义用户进入交易界面后的选择
'''
    information = '''
    ******INFOMATION******
    请选择交易类型：
    1、提款
    2、还款
    3、转账
    4、退出
    5、购物商城
    6、管理员模式
    '''
    print(information,'\n')

def run():
    user_auth = authentication.login(user_tem_data,use_log)
    #调用authentication中的login模块，把临时用户字典和调用use_lig的日志对象logger传去
    if user_tem_data['is_authenticated']== True:
        print('认证成功')
        use_log.info('进入atm界面中')
        choose(user_auth)
        menu = {
        '1':withdraw,#提现
        '2':repayment,#还款
        '3':transfer,#转账
        '4':logout,#退出
        '5':shops,#购物商场
        '6':manager#管理员模式
    }
        flag = False
        while True:
            select = input('请输入交易类型号码：').strip()
            if select in menu:
                menu[select](user_auth)
            else:
                print('交易号码不存在')
                use_log.warning('交易号码不存在')
