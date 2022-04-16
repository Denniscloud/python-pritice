'''
作用： 模拟车牌摇号
日期  2022年01月25日
'''
# 若没摇到想要的号码，一共可以摇三次
import random
import string

count=0
a=string.digits+string.ascii_uppercase
num=[]
while count<3:
    for i in range(20):
        d=string.ascii_uppercase
        d=random.choice(d)
        b=random.sample(a,6)
        b="".join(b)
        b=f"京{d}.{b}"
        num.append(b)
        print(b)
    c=input("输入你想要的车牌").strip()   #除去空格
    if c in num:
        print("你要的车牌我正好有")
        print("恭喜你获得车牌",c)
    else:
        print("抱歉，你要的车牌我没有哦,\n再摇一次吧")
    count+=1



