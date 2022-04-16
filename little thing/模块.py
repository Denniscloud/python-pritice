'''
作用： 视频合并模块
日期  2022年02月05日
'''

import re
import time
import os
import requests
from Crypto.Cipher import AES



def m3u8_download(m3u8_url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    res = requests.get(m3u8_url, headers=header)
    res_list = res.text.split('\n')
    # 请求解密文件
    key_url = re.findall('URI="(.*?)"', res.text)[0]
    key_res = requests.get(key_url, headers=header)
    m3u8_ts_urls = []
    for line in res_list:
        if 'ts' in line:
            m3u8_ts_urls.append(line)
    print('共有 ', len(m3u8_ts_urls), ' 个文件')
    base_url = '/'.join(m3u8_url.split('?')[0].split('/')[:-1]) + '/'
    # 生成解密对象
    cryptor = AES.new(key_res.content, AES.MODE_CBC)
    # 下载 .ts 文件
    for index, url in enumerate(m3u8_ts_urls):
        content_url = base_url + url
        response = requests.get(content_url, headers=header)
        file_name = re.findall('(video=.*?)&', url)[0].replace('=', '')
        # 保存解码数据 .ts格式
        with open(f'D:/video/{file_name.replace("video", "")}.ts', 'wb') as fw:
            fw.write(cryptor.decrypt(response.content))
        time.sleep(0.1)
    print('====下载完成====')


def merge_ts_file_with_os(data_dir, out_file_name, des_dir=None):
    # 在window系统下 合并ts为MP4格式

    print('开始合并...')
    files = os.listdir(data_dir)
    scatter_files = []
    for i in files:
        if 'ts' in i:
            scatter_files.append(i)
    # 对文件进行排序
    scatter_files.sort(key=lambda x: int(re.findall('(\d+).ts', x)[0]))

    # 此处如果文件路径过长，将会失败，因此保存文件的名称尽量短，否则只能分步合成文件
    b = '+'.join(scatter_files)
    new_name = out_file_name + '.mp4'
    if des_dir:
        new_name = os.path.join(des_dir, new_name)
    cmd_ = 'copy /b ' + b + ' ' + new_name
    cmd1 = 'd:'
    cmd2 = 'cd ' + data_dir
    del_cmd = 'del /Q *.ts'

    # window中只能多条命令持续执行，否则，将不成功
    cmd_all = ' & '.join([cmd1, cmd2, cmd_, del_cmd])
    os.system(cmd_all)
    print('合并完成', out_file_name)




import re
import time
import os
import requests

def merge_ts_file_with_os(data_dir, out_file_name, des_dir=None):
    # 在window系统下 合并ts为MP4格式

    print('开始合并...')
    files = os.listdir(data_dir)
    scatter_files = []
    for i in files:
        if 'ts' in i:
            scatter_files.append(i)
    # 对文件进行排序
    scatter_files.sort(key=lambda x: int(re.findall('(\d+).ts', x)[0]))

    # 此处如果文件路径过长，将会失败，因此保存文件的名称尽量短，否则只能分步合成文件
    b = '+'.join(scatter_files)
    new_name = out_file_name + '.mp4'
    if des_dir:
        new_name = os.path.join(des_dir, new_name)
    cmd_ = 'copy /b ' + b + ' ' + new_name
    cmd1 = 'd:'
    cmd2 = 'cd ' + data_dir
    del_cmd = 'del /Q *.ts'

    # window中只能多条命令持续执行，否则，将不成功
    cmd_all = ' & '.join([cmd1, cmd2, cmd_, del_cmd])
    os.system(cmd_all)
    print('合并完成', out_file_name)

if __name__ == '__main__':
    merge_ts_file_with_os(data_dir="video",out_file_name="video")

