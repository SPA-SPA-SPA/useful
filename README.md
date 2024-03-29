# useful

[TOC]

## 用途
这个程序可以爬取某个网站上的网页表格，并把表格转化成xlsx格式的文件。

## 使用方法
### 输入
在getDate.py文件中，在download_all_webFile函数中输入该网站的网址，和已经定义好了的name_list参数。注意，本程序设计成只能处理相同类型的网址，所以如果换其他的网址，很可能会遇到bug。

然后，在autoGetDate函数中输入想要提取整合的数据的名字，和已经定义好了的name_list参数。

注意，没有使用文件记录name_list参数的原因是，程序设计想要每次运行都与网站的最新数据同步。

程序对上述函数的默认参数是：
1. 程序设计之初存在的4个网址
2. 离婚登记

## 处理过程
正确输入参数后，在终端下输入：
```shell
$ python getDate.py
```

你也许会觉得奇怪，为什么是getDate，而不是getData？那是因为我写错了，而我现在不想修改它了。另外，如果你无法运行，那可能是因为你缺少一些工具，你可以到[Tools](#Tools)看一看。

在输入命令后，程序会执行以下步骤：

1. **启动**：使用 chrome 浏览器打开网页，查看网页列表名字，并将名字保存在name_list列表中。
2. **下载**：查看一个列表名字的同时，程序会查看文件夹html中是否有对应名字的html文件。如果文件已经存在，则不会执行操作3。
3. 如果不存在，则会打开该列表链接，获取新打开的网页的网址，以供下载函数下载该网页到html文件夹中。这部分操作主要的函数在文件autoDownloadAllFile.py中。
4. **转换**：所有网址的列表都被查看过后，程序会启动下一个环节：将网页表格转化为xlsx格式的excel表格。程序会根据name_list列表，遍历并转换所有的html文件夹中的html文件，输出对应的xlsx文件在xlsx文件夹中。
5. **提取**：在转换完成后，程序会根据参数"离婚登记"和name_list列表，遍历每个xlsx文件夹下的xlsx文件，并提取出每个文件的"离婚登记"列的数据，写入根目录下新的文件 离婚登记.xlsx中。步骤4和5的主要函数都在analy.py文件中，其中步骤4最主要的函数是create_xlsx函数，和write_a_row函数。前者是使html -> xlsx，需要调用后者处理html表格的特点和写入xlsx的方式。

### 输出
中间的输出：

1. html文件夹中的html文件
2. xlsx文件夹中的xlsx文件

最终的输出：

1. 根目录下的 离婚登记.xlsx文件

## 文件结构
useful2.0文件夹，属于程序源文件的有：

1. getDate.py
2. analy.py
3. autoDownloadAllFile.py
4. download2.py

其中 getDate.py 是程序启动文件，负责整个程序的流程。调用 analy.py 和 autoDownloadAllFile.py。

analy.py 包含分析和处理文件的函数：

```python
# analy.py文件

""" 写表行的函数 """
def write_a_row(tds, row_num, path):{}

""" 传入一个web文件名，生成一个xlsx文件"""
def create_xlsx(path):{}

""" 一键获取同类数据 """
def autoGetDate(title_name, name_list):{}
```

autoDownloadAllFile.py 处理打开网站和下载网页，以及保存列表：

```python
""" 输入一个列表页的网址和一个列表，将所有列表项的网页下载到本地并记录列表项的名字在列表中。
（如果文件存在就不再下载。） """
def download_all_webFile(main_url, name_list):{}
```

download2.py 处理下载，autoDownloadAllFile实际上要调用它才能下载。

## Tools
1. bs4
2. openpyxl
3. selenium
4. chrome
5. chromeDriver

### bs4
这是一个分析html网页的python工具包，这里给出它的文档，我所遇到的问题在文档都有解答。

bs4文档地址：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#

bs4安装方法在文档中有，但我还是在这里给出当时能用的pip安装方法：
```shell
$ pip install beautifulsoup4
```

### openpyxl
一个可以操作excel文件，例如：xlsx文件的python工具包。

openpyxl文档地址：https://openpyxl.readthedocs.io/en/stable/

pip安装方法：
```shell
$ pip install openpyxl
```

### selenium
一个浏览器自动测试框架，我使用它来打开、关闭网页，并获取网址。具体的使用位置在 autoDownloadAllFile.py。

selenium文档地址：https://www.seleniumhq.org/docs/

pip安装方法：
```shell
$ pip install selenium

```

### chrome
Google发行的浏览器，我使用selenium操作它，所以你如果不修改代码而想要运行程序，我建议你安装chrome。

### chromeDriver
selenium操作chrome需要安装chromeDriver。你需要安装对应chrome版本的 chromeDriver ，下面给出下载地址和查看版本对应关系的网址。

版本对应关系：https://blog.csdn.net/yoyocat915/article/details/80580066

chromeDriver下载地址：http://chromedriver.storage.googleapis.com/index.html

关于版本对应关系，我不喜欢从博客知道这些，但是我暂时还没有找别的方法知道对应关系。如果你知道，希望你能告诉我。

## 遇到的问题和解决
### 1. 如何处理网页表格(table标签)？
我使用bs4，分析表格的特点，并全部按照原表格的结构写入xlsx文件中。再在xlsx上做进一步的处理。

最好先下载好文件，再处理。也即爬取和处理分开。

### 2. 如何使用python下载网页？
使用requests。

### 3. from openpyxl.utils import get_column_letter
这要注意， get_column_letter 函数已经放在 openpyxl.utils 下面了。我的一些参考资料过时了。

### 4. 如何自动化点开网页并获取网址？
使用 selenium，我的代码中有注释。

### 5. 如何使用 selenium 切换网页tab，也就标签？
我的代码中有注释。

### 6. 如何使用python处理excel表格？
使用 openpyxl，我的代码中有注释。

### 7. 为什么无法使用 selenium 操控我的浏览器，比如chrome？
你应该缺少类似 chromeDriver 的东西。

### 8. 为什么要下载完一个文件要等待一分钟?
因为我发现下载太快，会下载失败。

## 参考资料
注意，这份参考资料是不完整的，因为我查完资料后没有及时地保存网址，而且不太想去翻历史记录。

1. Python编程快速上手——让繁琐工作自动化 ISBN：978-7-115-42269-9 [美] Al Sweigart 人民邮电出版社. Kindle版本
2. Python 编程：从入门到实践 ISBN：978-7-115-42802-8 [美] Eric Matthes 译者：袁国忠
3. bs4文档地址：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#
4. openpyxl文档地址：https://openpyxl.readthedocs.io/en/stable/
5. selenium文档地址：https://www.seleniumhq.org/docs/
6. 版本对应关系：https://blog.csdn.net/yoyocat915/article/details/80580066
7. chromeDriver下载地址：http://chromedriver.storage.googleapis.com/index.html
8. http://www.itkeyword.com/doc/3074720452893495x779/python-worksheet-range-names-does-not-exist-keyerror-in-openpyxl

对于查资料而言，我觉得最好能查看官方文档，因为那是会及时更新的，而出版书籍和一些博客感觉则没那么及时。

官方文档一般比较详细，能解决大部分常见问题，十分有用。举例说明：骡子能看官方说明书开gundam :)
