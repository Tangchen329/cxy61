#!/usr/bin/env python
#coding:utf-8

#导入 selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#打开谷歌浏览器，并访问百度
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

#在https://sites.google.com/a/chromium.org/chromedriver/downloads上下载chrome的浏览器驱动
#Mac系统就安装在usr/local/bin下即可
#具体操作 在终端输入 sudo mv 文件目录 空格 要移动到的目录
#sudo mv /Users/pineapple/Desktop/chromedriver /usr/local/bin


#获取浏览器中 name为wd的标签
elem = driver.find_element_by_name("wd")
#搜索cxy 61
elem.send_keys("cxy61")
elem.send_keys(Keys.RETURN)
#打印页面
print (driver.page_source)


#mac上用option+commond+i打开开发者工具
#windows上用f12. 
#点击左上角类似鼠标的图标一下，然后就可以看到网站页面每一块的代码

