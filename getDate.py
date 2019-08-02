#! python3
#coding=utf-8
import os

from autoDownloadAllFile import download_all_webFile
from analy import create_xlsx, autoGetDate

""" 下载并分析网页：http://www.mca.gov.cn/article/sj/tjjb/sjsj/?2，提取离婚登记的数据 """
""" 首先下载网页 """
""" 若网页文件已经存在，则不再下载。但每运行一次都会更新一次list和表格。 """
# 新建一个列表name_list
name_list = []

# 运行download_all_webFile(main_url, name_list)
download_all_webFile('http://www.mca.gov.cn/article/sj/tjjb/sjsj/?', name_list)
download_all_webFile('http://www.mca.gov.cn/article/sj/tjjb/sjsj/?2', name_list)
download_all_webFile('http://www.mca.gov.cn/article/sj/tjjb/sjsj/?3', name_list)
download_all_webFile('http://www.mca.gov.cn/article/sj/tjjb/sjsj/?4', name_list)

""" 然后分析网页并写入表格中 """
""" 根据name_list循环分析、提取数据 """

# 运行create_xlsx(path)，获得所有网页的列表
for path in name_list:
    if not(os.path.exists('xlsx/' + path + '.xlsx')):
        create_xlsx(path)

# 传入想要的数据名字title_name，获得一份总结数据列表
autoGetDate("离婚登记", name_list)