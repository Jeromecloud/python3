#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

while True:
    import Cards_tool

    Cards_tool.show_menu()

    action_str = input("Please input your action!")
    print("your action is [%s]" % action_str)

    if action_str in ["1","2","3"]:
        #新增名片
        if action_str == "1":
            Cards_tool.new_card()
        #显示全部
        elif action_str == "2":
            Cards_tool.show_all()
        #查询名片
        elif action_str == "3":
            Cards_tool.search_card()
    #退出系统
    elif action_str == "0":
        print("Welcome to use the card mangamant system again!")
        break
    else:
        print("No ,you're wrong")

