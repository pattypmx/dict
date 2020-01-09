my_dict = {"姓名": "小明", "班级": "2班", "年龄": 18}

# 修改元素：把班级改为3班----通过key修改
my_dict["班级"] = "3班"
print(my_dict)

# 添加元素
my_dict["性别"] = "女"
print(my_dict)

# 删除元素
del my_dict["年龄"]
print(my_dict)

# 清空元素
my_dict.clear()
print(my_dict)
# 等价于my_dict={}或者my_dict=dict()