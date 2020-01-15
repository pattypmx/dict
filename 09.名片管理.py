# 4. 编写程序，完成“名片管理器”项目
# 需要完成的基本功能：
# 添加名片{"小明"：{"姓名"："小明,"年龄":"20"}}
# 删除名片
# 修改名片
# 查询名片
# 退出系统
# 程序运行后，除非选择退出系统，否则重复执行功能

# 定义变量存放用户信息
all_dict = {"小明": {"姓名": "小明", "年龄": "20"}, "小红": {"姓名": "小红", "年龄": "22"}}
# 定义变量存放功能
info = """1.添加名片
2.删除名片
3.修改名片
4.查询名片
5.退出系统
请选择需要的功能：
"""
while True:
# 通过输入的数字引导进入所对应的功能
    index = input(info)
    print(index)
    if index == "1":    #  input是字符串类型
        my_name = input("请输入您的名字：")
        my_age = input("请输入您的年龄：")
        # 构造字典
        my_dict = {"name": my_name, "age": my_age}
        all_dict[my_name] = my_dict
        print(all_dict)
    elif index == '2':
        my_name = input("请输入您要删除信息的名字：")
        if my_name in all_dict:
            del all_dict[my_name]
            print("删除成功")
        else:
            print("数据不存在，请重新输入")
    elif index == "3":
        my_name = input("请输入您要修改年龄的名字：")
        if my_name in all_dict:
            my_age = input("请输入您要修改的年龄：")
            all_dict[my_name]["年龄"] = my_age
            print("修改成功")
        else:
            print("修改失败")
    elif index == "4":
        my_name = input("请输入您要查询的名字：")
        if my_name in all_dict:
            n = all_dict[my_name]["姓名"]
            a = all_dict[my_name]["年龄"]
            print("姓名：%s 年龄：%s" % (n, a))
        else:
            print("查询失败")
    elif index == '5':
        print("谢谢使用")
        break




