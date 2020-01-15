# 6公里(含)内3元;
# 6公里至12公里(含)4元;
# 12公里至22公里(含)5元;
# 22公里至32公里(含)6元;
# 定义变量记录公里数即票价
km = 53
money = 0

if km <= 6:
    money = 3
elif km > 6 and km <= 12:
    money = 4
elif km >12 and km <=22:
    money = 5
elif km >22 and km <=32:
    money = 6
# print(money)
elif km > 32:
# 32公里以上部分，每增加1元可乘坐20公里
# 分析：51km（32+19）---6+1
#      52km（32+20）---6+1
#      53km（32+20+1）---6+1+1
# 定义变量，求公里数差值
    km_km = km - 32
# 分两种情况：差值被20整除
    if km_km % 20 == 0:
        money = 6 + km_km / 20
# 差值，没有被20整除，取去掉小数点的部分
    else:
        money = 6 + int(km_km / 20) + 1
print(money)

# 每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠
# 满150元以后的乘次，价格给予5折优惠;
# 支出累计达到400元以后的乘次，不再享受打折优惠。
# 假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁
# 帮小明完成每月乘坐地铁需要的总费用

# 定义一个变量总费用
total_money = 0
# 假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁
# 即循环40次
for x in range(40):
    if total_money < 100:
        total_money += money
    # 每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠
    elif total_money >=100 and total_money <150:
        total_money = total_money + money * 0.8

     # 满150元以后的乘次，价格给予5折优惠;
    elif total_money >= 150 and total_money <400:
        total_money += money * 0.5

    # 支出累计达到400元以后的乘次，不再享受打折优惠。
    elif total_money >= 400:
        total_money += money
print("总费用:%.2f" % total_money)


