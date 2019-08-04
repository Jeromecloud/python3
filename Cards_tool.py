#记录所有的名片字典
card_list = []

def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 ")
    print("1、新增名片")
    print("2、显示全部")
    print("3、搜索名片")
    print("0、退出系统")
    print("*" * 50)

def new_card():
    """新增名片"""
    print("_" * 50)
    print("新增名片")

    #提示用户输入信息
    name = input("please input your name:")
    age = input("please input your age:")
    phone = input("please input your phone number:")
    
    #将用户资料建立成字典
    card_dict = {
        "name": name,
        "age": age,
        "phone": phone}
    #将名片添加到列表
    card_list.append(card_dict)

    print(card_list)
    print("Succees,%s\'s card done\n\n" % name)

def show_all():
    """"显示全部"""
    print("_" * 50)
    print("显示全部")
    if len(card_list) == 0:
        print("It\'s zero,please fill up!")
        # return可以返回一个函数的执行结果，如果后面没有内容，表示会返回调用函数的位置，并不返回任何结果
        return

    else:
        for name in ["姓名","年龄","电话号码"]:
            print(name,end="\t\t")
        print(" ")
        print("-" * 50)
        for card_dict in card_list:
            print("%s\t\t%s\t\t%s" % (card_dict["name"],
                                      card_dict["age"],
                                      card_dict["phone"]))
    print("\n\n")

def search_card():
    """搜索名片"""
    card_name = input("please input card you wanted:")
    for card_dict in card_list:
        if card_name == card_dict["name"]:
            print("-" * 50)
            print("%s\t\t%s\t\t%s\n" % (card_dict["name"],
                                       card_dict["age"],
                                       card_dict["phone"]))
            #删除名片
            deal_card(card_dict)
            break
    else:
            print("Sorry,it\'s not exist\n\n")

def deal_card(find_dict):
    """"删除名片"""
    print(find_dict)
    action_str = input("please choose action :"
                        "1:change  2:delete")
    if action_str == "1":
        print("change")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("delete successed\n\n")
