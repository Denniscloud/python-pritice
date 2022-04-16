'''
seleium  搞一下知网
'''


from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
import csv
from urllib.parse import urljoin
import time
import random
import json


def getpage(url,keyword,page):
    opt= Options()
    opt.add_argument("--headless")
    opt.add_argument("--disabli-gpu")  #无头浏览器
    web=Firefox(options=opt)
    # web=Firefox()
    web.get(url)
    time.sleep(1)
    web.find_element(by=By.ID,value='keyword_ordinary').click()
    web.find_element(by=By.ID,value="keyword_ordinary").send_keys(keyword)
    web.find_element(by=By.CLASS_NAME,value='btn-search ').click()
    # 显示等待文献是否加载完成
    WebDriverWait(web, 1000).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'g-search-body')
        )
    )
    # 声明一个标记，用来标记翻页几页
    count = 1
    while True:
        # 显示等待加载更多按钮加载完成
        WebDriverWait(web, 1000).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'c-company__body-item-more')
            )
        )
        # 获取加载更多按钮
        Btn = web.find_element(by=By.CLASS_NAME,value='c-company__body-item-more')
        # 显示等待该信息加载完成
        WebDriverWait(web, 1000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH,
                 '//div[@id="searchlist_div"]/div[{}]/div[@class="c-company__body-item"]'.format(2 * count - 1))
            )
        )
        # 获取在div标签的信息，其中format(2*count-1)是因为加载的时候有显示多少条
        # 简单的说就是这些div的信息都是奇数
        divs = web.find_elements(by=By.XPATH,value=
            '//div[@id="searchlist_div"]/div[{}]/div[@class="c-company__body-item"]'.format(2 * count - 1))
        # 遍历循环
        for div in divs:
            data_list = []
            # 获取文献的题目
            name = div.find_element(by=By.CLASS_NAME,value='c-company__body-title').text
            # 获取文献的作者
            author = div.find_element(by=By.CLASS_NAME,value='c-company__body-author').text
            # # 获取文献的摘要
            # content = div.find_element_by_class_name('c-company__body-content').text
            # 获取文献的来源和日期、文献类型等
            text = div.find_element(by=By.CLASS_NAME,value='c-company__body-name').text.split()
            if (len(text) == 3 and text[-1] == '优先') or len(text) == 2:
                # 来源
                source = text[0]
                # 日期
                datetime = text[1]
                # 文献类型
                literature_type = None
            else:
                source = text[0]
                datetime = text[2]
                literature_type = text[1]
            # 获取下载数和被引数
            temp = div.find_element(by=By.CLASS_NAME,value='c-company__body-info').text.split()
            # 下载数
            download = temp[0].split('：')[-1]
            # 被引数
            cite = temp[1].split('：')[-1]
            # 文献链接
            link = div.find_element(by=By.CLASS_NAME,value='c-company-top-link').get_attribute('href')
            # 拼接
            link = urljoin(web.current_url, link)
            # 获取关键字（需要访问该文献，url就是上面获取到的link）
            # browser.get(link) # 这行和下面那行不推荐使用，因为句柄的问题，会报错
            # browser.back()
            # 打印查看下未访问新窗口时的句柄
            # print(browser.current_window_handle)
            js = 'window.open("%s");' % link
            # 每次访问链接的时候适当延迟
            time.sleep(random.uniform(1, 2))
            web.execute_script(js)
            # 打印查看窗口的句柄，对比看下当前的句柄是哪个
            # 结果是原先窗口的句柄，而不是新打开窗口的句柄，因为和上面打印的句柄一样
            # print(browser.current_window_handle)
            # 切换句柄到新打开的窗口，browser.window_handles是查看全部的句柄
            # browser.switch_to_window是切换句柄
            web.switch_to.window(web.window_handles[1])

            #等待加载完再获取内容，防止报错
            WebDriverWait(web, 1000).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'c-card__aritcle')
                )
            )
            # 获取关键字（使用xpath）
            key_worlds = web.find_elements(by=By.XPATH, value=
                '//div[@class="c-card__paper-name"][contains(text(), "关键词")]/following-sibling::div[1]/a')
            key_worlds = ','.join(map(lambda x: x.text, key_worlds))
              # 获取文献的摘要
            content = web.find_element(by=By.CLASS_NAME, value="c-card__aritcle").text

            web.close()
            web.switch_to.window(web.window_handles[0])
            data_dict = {}
            data_dict['name'] = name
            data_dict['author'] = author
            data_dict['content'] = content
            data_dict['source'] = source
            data_dict['datetime'] = datetime
            data_dict['literature_type'] = literature_type
            data_dict['download'] = download
            data_dict['cite'] = cite
            data_dict['link'] = link
            data_dict['key_worlds'] = key_worlds

            data_list.append(data_dict)
            # print(data_dict)
            writefile(data_list)
        
        # 如果Btn按钮（就是加载更多这个按钮）没有找到（就是已经到底了），就退出
        if not Btn:
            break
        else:
            Btn.click()
        # 如果到了爬取的页数就退出
        if count == page:
            break

        count += 1

        time.sleep(2)
        print("haole")
        
    # 全部爬取结束后退出浏览器
    web.quit()
    
 
def writefile(data_list):
    # with open('data_json.json', 'a+', encoding='utf-8') as f:
    #     json.dump(data_list, f, ensure_ascii=False, indent=4)
    # print('json文件写入完成')

    # 将数据写入csv文件
    with open('zhihu\data_csv.csv', 'a', encoding='gbk', newline='') as f:
        # 表头
        value = data_list[0].values()
        # 声明writer对象
        writer = csv.writer(f)

        writer.writerow(value)
    print('csv文件写入完成')

if __name__ == '__main__':
    url='https://wap.cnki.net/touch/web/Article/SearchIndex'
    keyword='商超'
    page=15     # 
    list=getpage(url,keyword,page),
     
    
    
    




