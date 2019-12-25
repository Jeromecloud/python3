""" 学员信息管理系统 """
info = []

def info_print():
    """ 功能展示 """
    print('请选择功能：')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、退出系统')
    print('-' * 20)

def add_info():
    """ 添加学员 """
    new_name = input('学员姓名')
    new_id = int(input('学员学号'))
    new_phone = input('学员电话')

    global info 
    
    # 检测用户是否存在
    for i in info:
        if new_id == i['id']:
            print('已存在该学员')
            return #如果已存在，则不执行下方代码

    # 如果不存在，则添加该学员
    info_dict = {}
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['phone'] = new_phone

    # 将该学员字典信息追加到列表
    info.append(info_dict)
    print(info_dict)
    print('添加成功！\n\n')

def del_info():
    """ 删除学员 """
    del_id = int(input('请输入需要删除的学员学号：'))
    global info
    for i in info:
        if del_id == i['id']:
            info.remove(i)
            print('删除成功')
            break
    else:
        print("查无此人")

def modify_info():
    """ 修改学员信息 """
    global info
    modify_id = int(input('请输入学员学号'))
    for i in info:
        if modify_id == i['id']:
            print(i)
            i['phone'] = input('新电话:')
            break
        else:
            print('该学员不存在')  
    print(info)
while True:

    # 1、显示功能界面
    info_print()

    # 2、用户输入功能选项
    info_input = int(input(''))

    # 3、按照用户不同选项，实现不同功能
    if info_input == 1:
        add_info()
    elif info_input == 2:
        del_info()
    elif info_input == 3:
        modify_info()
    elif info_input == 4:
        break
    else:
        print('输入有误，赶紧滚！')