#!python3
#coding=utf-8

from download2 import download
from selenium import webdriver
import time, os
# import bs4, requests

""" 设置 """
browser = webdriver.Chrome()
length = 0

""" 输入一个列表页的网址和一个列表，将所有列表项的网页下载到本地并记录列表项的名字在列表中。（如果文件存在就不再下载。） """
def download_all_webFile(main_url, name_list):
    browser.get(main_url)
    # 找到这个首页的数据列表
    linkElem = browser.find_elements_by_class_name('artitlelist')
    # 获取列表长度
    length = len(linkElem)

    # 循环打开列表每一项，并跳转到最新的窗口，获取url，检查下载网页，跳转回首页
    for i in range(0, length):
        # 获取列表项的名字
        path = linkElem[i].text
        # 添加path到列表中
        name_list.append(path)
        
        # 如果网页文件还不存在就下载网页，并等待1min
        if not(os.path.exists('html/' + path + '.html')):
            # 点击列表项
            linkElem[i].click()
            time.sleep(1)
            # 跳转到最新的窗口（其实第2个打开的窗口）
            browser.switch_to.window(browser.window_handles[1])
            # 获取url
            url = browser.current_url
            # 关闭当前标签页
            browser.close()
            # 下载文件
            download(url, 'html/' + path + '.html')
            time.sleep(60)
        
        # 跳回首页，循环点击下一项
        browser.switch_to.window(browser.window_handles[0])

# 这是调试函数用的语句
# download_all_webFile('http://www.mca.gov.cn/article/sj/tjjb/sjsj/?', name_list)
# download_all_webFile('http://www.mca.gov.cn/article/sj/tjjb/sjsj/?2', name_list)