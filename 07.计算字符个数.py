# 计算hello world每个字符个数
my_str = "hello world"
# 定义一个列表存放字符
my_list = []
# 循环取值
for c in my_str:
    # 去除空格  且这个字符没有保存过
    if c != " " and c not in my_list:
        # 计算每个字符出现的次数
        count = my_str.count(c)
        print("%s:%d" % (c, count))
        # 保存下这个字符
        my_list.append(c)


# 方法二：
my_str = "hello world"
# 先把str分割切片成list
my_list2 = my_str.split()
print(my_list2)
# 再合并成一个新的字符串
new_str = "".join(my_list2)
print(new_str)

# 定义一个列表存放字符
list1 = []
for c1 in new_str:
    if c1 not in list1:
        count2 = new_str.count(c1)
        print("%s:%d" % (c1, count2))
        list1.append(c1)

