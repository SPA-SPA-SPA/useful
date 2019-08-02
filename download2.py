#! python3
#coding=utf-8
import requests, sys
# 从一个URL下载一个文件，并保存到path
def download(url, path):
    # 传进一个下载地址
    res = requests.get(url)

    # 输出异常
    try:
        res.raise_for_status()
    except Exception as exc:
        print ('There was a problem: %s' % (exc))

    # 打开一个文件，以二进制读写格式打开    
    playFile = open(path, 'wb')

    # 将下载的文件写进文件中
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
        
    # 关闭文件
    playFile.close()