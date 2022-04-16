'''
作用： 多线程操作
日期  2022年02月03日
'''

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def fn(name):
    for i in range(100):
        print(name,i)

if __name__ == '__main__':
    with ThreadPoolExecutor(50)as t:
        for i in range(100):
            i.submi(fn,name=f"线程{i}")
    print("123")




