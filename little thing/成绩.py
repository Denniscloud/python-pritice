'''
作用：yi个匹配成绩的⼩程序，成绩有ABCDE 5个等级，
日期  2022年01月12日
'''
glod=int(input("glod:"))
if glod<0 or glod>100:
    print("error!")
elif 90<=glod<=100:
    print("A")
elif 80<=glod<=89:
    print("B")
elif 60<=glod<=79:
    print("C")
elif 40<=glod<=59:
    print("D")
elif 0<=glod<=39:
    print("E")
