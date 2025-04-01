# _*_ coding : utf-8 _*_
# @Time : 2025/3/30 20:39
# @Author : 田园
# @File : 76-Python_selenium_基本使用
# @Project : 75-Python_selenium_为什么学习selenium.py

# 1. 导入selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.webdriver import Service
# 2. 创建浏览器操作对象
# 将驱动文件的路径作为webdriver的Chrome方法的参数，因为是放在与该文件的同一路径，才这么写，若不是同一路径，就要将路径写完整
# 驱动
service=Service('chromedriver.exe')
driver=webdriver.Chrome(service=service)

# 3. 访问网址
url='https://taobao.com'
# 向访问地址发送get请求，来获取数据
driver.get(url)

# page_source获取网页源码
content=driver.page_source
print(content)

print(input('enter one name'))
# 4.0不需要写path，但是要chromedriver的配置驱动的环境变量！！！
# Chrome里面不用放path，什么都不要放，不然有可能报错。