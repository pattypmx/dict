tuple1 = (1, 30, "hello", 3.14)
# 获取元组中的元素
# my_tuple = tuple1[2]
# print(my_tuple)

# tuple = (1)
# print(type(tuple))
# tuple = (1,)
# print(type(tuple))

# 修改元素---报错
# tuple[0] = 113
# print(tuple)

# 查看元素
# my_tuple =tuple1.index("hello")
# print(my_tuple)
# my_tuple2 = tuple1.count("hello")
# print(my_tuple2)

# 遍历循环
for tuple3 in tuple1:
    print(tuple3)

index = 0
tuple4 = len(tuple1)
while index < tuple4:
    tuple5 = tuple1[index]
    print(tuple5)
    index += 1


