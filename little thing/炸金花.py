'''
作用： 生成炸金花，并计算谁大谁小
日期  2022年01月24日
'''
import random

#生成牌
def make_poke():
    poke_types=["♦","♣","♥","♠"]
    poke_num=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    poke_list=[]
    for i in poke_types:
        count=0
        for j in poke_num:
            count+=1
            card=[f"{i}{j}",count]
            poke_list.append(card)
    return poke_list

#发牌

def hand_poke(players,poke_list):
    player_dic={}
    for p_name in players:
        p_cards=random.sample(poke_list,3)
        for card in p_cards:
            poke_list.remove(card)
        player_dic[p_name]=p_cards
        print(f"为玩家{p_name}生成了牌",p_cards)
    return player_dic

#对拿到的牌排序好  冒泡排序
def sortlist(lis):
    l=len(lis)
    for i in range(0,l):
        for j in range(0,l-i-1):
            if lis[j][1] > lis[j+1][1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]   #交换顺序
    return lis

#算分规则
#单排
def calculate_single(p_cards,score):
    p_cards=sortlist(p_cards)
    weight_val=[1,10,100]   #设置权重
    count=0
    for card in p_cards:
        score+=card[1]*weight_val[count]
        count+=1
    print(f"计算单排",p_cards,score)
    return score

#对子
def calculate_pair(p_cards,score):
    p_cards=sortlist(p_cards)
    card_val=[i[1] for i in p_cards]
    if len(set(card_val))==2:    #放进集合里面，根据集合的不重合性质看剩下几个元素判断对子
        if card_val[0]==card_val[1]:   #判断对子在前两个还是后两个乘上相应的权重
            score=(card_val[0]+card_val[1])*50+card_val[2]
        else:
            score=(card_val[2]+card_val[1])*50+card_val[0]
    print(f"计算对子",p_cards,score)
    return score

#顺子
def calculate_straight(p_cards,score):
    p_cards=sortlist(p_cards)
    card_val=[i[1] for i in p_cards]
    a,b,c=card_val
    if( b-a == 1 and c-b == 1):  #若A23 算顺子则加上 or card_val == [2,3,14]:
        score*=100
    print(f"计算顺子",p_cards,score)
    return score

#计算同花
def calculate_same_color(p_cards,score):
    color_set={i[0][0] for i in p_cards}  #直接放进集合里面方便计算
    if len(color_set) == 1:
        score*=1000
    print(f"计算同花",p_cards,score)
    return score

#计算同花顺
def calculate_same_color_straight(p_cards,score):
    p_cards = sortlist(p_cards)
    card_val = [i[1] for i in p_cards]
    a, b, c = card_val
    if (b - a == 1 and c - b == 1):
        color_set = {i[0][0] for i in p_cards}  # 直接放进集合里面方便计算
        if len(color_set) == 1:
            score *= 0.1
    print(f"计算同花顺",p_cards,score)
    return score

#计算豹子
def calculate_leopard(p_cards,score):
    card_val={i[1] for i in p_cards}
    if len(card_val) == 1:
        score*=10000
    print(f"计算豹子",p_cards,score)
    return score

calculate_func_order=[       #把前面计算权重分数的函数整合成一个列表，方便每个函数多次的调用
    calculate_single,
    calculate_pair,
    calculate_straight,
    calculate_same_color,
    calculate_same_color_straight,
    calculate_leopard
]

# 因为calculate_func_order[0]()=calculate_single()

players=["jake","lucy","dad","denis","niubi"]
poke_list=make_poke()      #调用牌，生成牌
random.shuffle(poke_list)   #洗牌，打乱列表顺序，使拿到的牌更加随机
prefomance=[]

player_dic={}
player_dic=hand_poke(players,poke_list)
for p_name,p_cards in player_dic.items():
    print(f"开始计算玩家{p_name}的牌")
    score=0
    for cal_func in calculate_func_order:
        score=cal_func(p_cards,score)
    prefomance.append([p_name,score])
print(prefomance)

winner=sortlist(prefomance)[-1]   #-1 为字典里排在末位的元素
for i in prefomance:
    if int(i[1]) == int(winner[1]):   #若分数相同，可以产生多个赢家（数字相同，花色不同）
        print(f"赢家是",i)
