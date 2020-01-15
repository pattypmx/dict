my_dict = {"姓名": "小明", "班级": "2班", "年龄": 18}

# 1.len:测量字典中，键值对的个数
# l = len(my_dict)
# print("列表中的键值对有%d对" % l)

# 2.keys:将字典中的key值以列表的形式展现
# k = my_dict.keys()  # 其实就是dict_keys列表类型
# print(k)
# # 值转换成列表
# print(list(k))

# 3.values：将字典中的value值以列表的形式展现;与keys使用一致
# v = my_dict.values()
# print(v)
# print(list(v))

# 4.items：将key_value全部以列表的形式展现
i = my_dict.items()
print(i)    # dict_items([('姓名', '小明'), ('班级', '2班'), ('年龄', 18)])
#  结果：最外层是一个列表，列表中每一个元素是一个元组
#  取值：年龄
age = list(i)
my_age = age[2][0]
print(my_age)
