# 字符串，列表，元组，字典----for/while循环
# 字符串
# string = "abcd"
# for s in string:
#     print(s)

# 列表
# 快速创建有规律的列表
# list1 = list("abcd")  # 不需要定义list（"a","b","c","d"）
# for l1 in list1:
#     print(l1)

# 元组
tuple1 = tuple("abcd")   # 创建元组，打印为列表
print(tuple1)
for t1 in tuple1:
    print(t1)

# 字典
my_dict = {"姓名": "小明", "班级": "2班", "年龄": 18}
# 遍历key-value的值
# for key in my_dict.keys():
#     print(key)
# for value in my_dict.values():
#     print(value)
for key, value in my_dict.items():
    print("key:", key)
    print("value:", value)

# 获取列表元素及对应的索引
for index, element in enumerate(my_dict):
    print(index, element)