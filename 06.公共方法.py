# 运算符
# +
list1 = [1, 2]
list2 = [3, 4]
my_list = list1 + list2
print(my_list)

name = "小明"
ret = "我叫" + name
print(ret)
# *
print("*" * 8)
list3 = [1, 2, 3]*2
print(list3)

#
# # in
list4 = [1, 2, 3]
if 2 in list4:
    print("2存在")

# not  in;在对字典操作时，判断的是字典的键
my_dict = {"姓名": "小明", "班级": "2班", "年龄": 18}
if "性别" not in my_dict:
    print("不存在")
else:
    print("存在")

# 判断value值
if "小明" in my_dict.values():
    print("小明存在")




