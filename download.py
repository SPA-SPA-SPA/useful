#! python3
#coding=utf-8
import requests, sys

# 从输入中传进一个下载地址和一个文件名，保存为一个文件
res = requests.get(sys.argv[1])

# 输出异常
try:
    res.raise_for_status()
except Exception as exc:
    print ('There was a problem: %s' % (exc))

# 打开一个文件（文件名从输入中获取），以二进制读写格式打开    
playFile = open(sys.argv[2], 'wb')

# 将下载的文件写进文件中
for chunk in res.iter_content(100000):
    playFile.write(chunk)
    
# 关闭文件
playFile.close()