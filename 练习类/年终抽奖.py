'''
作用： 年终抽奖小程序
日期  2022年01月26日
'''
from faker import Faker
import random

people_name=[]
def create_people(people_name):    # 创造员工函数
    for i in range(300):      # 一共300名员工
        p_name = Faker("zh_CN")
        b=p_name.name()
        people_name.append(b)
        # print(b)
    return people_name


people_name = create_people(people_name)
level=[30,6,3]
for i in range(3):
    winner_list=random.sample(people_name,level[i])
    for name in winner_list:
        people_name.remove(name)       # 移除已经抽中的人，不重复中奖
    print(f"抽中{3-i}等奖的人是",winner_list)


