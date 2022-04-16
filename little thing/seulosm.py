'''
作用： selenium操作
日期  2022年02月04日
'''
# web.find_element(By.XPATH,'/html/body/div[7]/div[2]/div/div[1]/div/div[5]/div[1]/div/a[1]/h3')
# web.find_elements_by_xpath('/html/body/div[7]/div[2]/div/div[1]/div/div[5]/div[1]/div/a[1]/h3')
# 上一行现在为被弃用写法

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
web=Firefox()

web.get('https://www.lagou.com/')
cd=web.find_element(By.XPATH,"/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/ul/li[7]/a")
cd.click()

time.sleep(1)

shichang=web.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div[1]/div/div[5]/div[1]/div/a[1]/h3")
shichang.click()
time.sleep(5)
print(shichang)
p_list=web.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[3]/div[3]/div/div[1]/div[2]")
for li in p_list:
    job_name=li.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').text
    job_price=li.find_element(By.XPATH,"./div/div/div[2]/span").text
    print(job_name,job_price)

print(p_list)
