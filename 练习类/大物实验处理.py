'''
液体的粘度系数实验数据的处理
'''

import math

def jisuan2(A,B):
    res=A/B
    return res

def jisuan1(d,t):
    resltlist=[]
    for (i,j) in zip(d,t):
        i=i/1000   
        #  毫米转米
        A=(p-p0)*g*(i**2)*j
        B=(1+(2.4*i/D))
        B=18*s*B
        result=jisuan2(A,B)
        resltlist.append(result)
    return resltlist

def ave(resltlist):      #计算均值
    total=0
    for i in range(0,len(resltlist)):
        total=total+resltlist[i]
    total=total/len(resltlist)
    return total

def unsure(d,t,result1):
    resultlist=[]
    Ndd=Nd/1000      #处理单位 
    Nss=Ns/1000
    for (i,j,k) in zip(d,t,result1):
        i=i/1000   
        nn=((2*Ndd/i)**2)+((Nt/j)**2)+((Nss/s)**2)
        un=k*math.sqrt(nn)
        resultlist.append(un)
    return resultlist


#-------------------------------------输入数据--------------------#
p=7980            
#小球密度 
p0=1060
#甘油密度
s=0.1
#设计距离差
D=0.06381
#量筒直径
g=9.7903
#重力常数

d=[0.815,0.803,0.784,0.756,0.774]    
#小球直径
t=[6.15,6.12,5.94,5.84,5.63]
# 10 cm 经历时间

#不确定度
Nd=0.005       #单位毫米
Ns=0.5          #单位毫米
Nt=0.01           #单位 秒
#-------------------------------------输入数据--------------------#

result1=jisuan1(d,t)
# 求数值

average=ave(result1)
#求均值
unsur=unsure(d,t,result1)
unave=ave(unsur)

print("各个结果是",result1)

print("各不确定度是",unsur)
print("均值是",average,unave)

