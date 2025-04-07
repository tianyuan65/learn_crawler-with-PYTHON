# _*_ coding : utf-8 _*_
# @Time : 2025/4/1 20:07
# @Author : 田园
# @File : 78-Python_selenium_元素信息以及交互
# @Project : 76-Python_selenium_基本使用.py

# 1. 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# selenium4版本，做了些调整，元素定位的方法需要导入By
from selenium.webdriver.common.by import By

# 2. 创建浏览器/驱动操作对象
service=Service('chromedriver.exe')
browser=webdriver.Chrome(service=service)

# 3.访问地址
url='https://www.baidu.com'
browser.get(url)

# 访问地址后，可以获取到百度主页面输入框的class属性的属性值
# 方法1：先通过id获取对象，再查找该标签的class属性的属性值
input=browser.find_element(By.ID,'su')
# 获取标签的属性
print(input.get_attribute('class')) #bg s_btn
print(input.get_attribute('value')) #百度一下
print(input.get_attribute('type'))  #submit
# 获取标签名
print(input.tag_name)   #input
map=browser.find_element(By.LINK_TEXT,'地图')
print(map.tag_name) #a

# .text是用来获取元素文本的，但很显然，input原本默认就是空的，因此无法提取出文本内容
# print(input.text)
# 因为input标签是自闭和标签，所以想要获取标签的文本内容的话，找一个闭和的正常标签即可，这里获取以页面右上角的新闻为例
news=browser.find_element(By.LINK_TEXT,'新闻')
print(news.text)    #新闻


# print(input('enter a word'))

