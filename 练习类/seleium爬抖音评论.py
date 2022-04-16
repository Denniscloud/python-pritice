##爬抖音评论


from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import csv
import time


def getcomment(url,page):
    opt= Options()
    opt.add_argument("--headless")
    opt.add_argument("--disabli-gpu")  #无头浏览器
    web=Firefox(options=opt)
 
    # web=Firefox()
    web.get(url)
    time.sleep(1)
    for cunt in range(1,page):
        # a=web.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div/div[4]/div['+str(cunt)+']/div/div[2]/p/span/span/span/span/span/span')
        try: 
            web.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)    
        except:
            time.sleep(2)  
            web.execute_script('window.scrollBy(0,140)')

    a=web.find_elements(by=By.XPATH,value='//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div/div[4]/div/div/div[2]/p/span/span/span/span/span/span')  
    count=writecomment(a)                                          
    # a=web.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div/div[4]/div/div/div[2]/p/span/span/span/span/span/span')
    # for jj in range(1,count):                  
        # b=web.find_elements(by=By.XPATH,value=f'//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div/div[4]/div[{jj}]/div/div[2]/div[3]/div/div[2]/p/span/span/span/span/span/span')
        # writecomment1(b)

def writecomment(a):
    count=1
    f=open(f"D:\数据\python 代码\能用的小东西\练习类\comment.csv",mode="a",newline="")    # newline='' 添加这个新一行不是空行
    csvwriter = csv.writer(f)   #开始往文件写入东西
    for i in a:
        dic=i.text.split(",")   #去掉逗号
        count+=1
        csvwriter.writerow(dic)
        print(dic)
    f.close()
    return count   #下滑每个一级评论一个

def writecomment1(b):
    f=open(f"D:\数据\python 代码\能用的小东西\练习类\comment1.csv",mode="a",newline="")    # newline='' 添加这个新一行不是空行
    csvwriter = csv.writer(f)   #开始往文件写入东西                                
    for j in b:
        dic=j.text.split(",")   #去掉逗号
        count+=1
        csvwriter.writerow(dic)
        print(dic)
    f.close()



if __name__ == '__main__':
    url='https://www.douyin.com/video/7018757513445149966'

    # id=url.split("/",4)
    # id=id[4]
    page=30         #滑轮滑倒底部多少次
    getcomment(url,page)
    

'''

//*/div[2]/div[3]/div[1]/div[2]/p/span/span/span/span/span/span
//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/di/span/span
'''