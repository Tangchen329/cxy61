#!/usr/bin/env python
#coding:utf-8

from selenium import webdriver

dr=webdriver.Chrome()
dr.get('http://www.qiushibaike.com/')


#获取id为content-left的元素
main_content=dr.find_element_by_id('content-left')
#获取class为content的元素
contents=main_content.find_elements_by_class_name('content')

#for循环
i=1
for content in contents:
	print(str(i)+"."+content.text + '/n')
	i=i+1


#退出
dr.quit()