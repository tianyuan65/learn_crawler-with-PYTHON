# _*_ coding : utf-8 _*_
# @Time : 2025/4/7 12:03
# @Author : 田园
# @File : 079-Python_selenium_交互
# @Project : 78-Python_selenium_元素信息以及交互.py

# 需求：从百度主页面开始，在文本框中输入人名后，点击百度一下按钮，随后往下滑，滑到页面最底部，然后点击下一页，但又想回到上一页，进行后退操作，随后又回到刚才的那一页，进行前进操作，再滑到第二页的最底部

# 1. 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# selenium4版本，做了些调整，元素定位的方法需要导入By
from selenium.webdriver.common.by import By

# 2. 创建浏览器/驱动对象
# chromedriver.exe是浏览器驱动文件的路径，因为放在了与py文件同意目录，因此这么写，若不在同一目录下就需要写下准确的具体所在的路径
service=Service('chromedriver.exe')
browser=webdriver.Chrome(service=service)

# 3. 访问地址
url='https://www.baidu.com'
# 从访问地址中获取源码
browser.get(url)

import time
# 让它睡两秒，模拟人类操作
time.sleep(2)

# 获取文本框的对象
input=browser.find_element(By.ID,'kw')
# 在文本框中输入秦彻，调用send_keys()，意为发送一个关键字
input.send_keys('秦彻')
# 再睡两秒
time.sleep(2)

# 获取百度一下的按钮
button=browser.find_element(By.ID,'su')
# 点击按钮
button.click()
# 再睡两秒
time.sleep(2)

# 滚动到页面底部
jsBottom='document.documentElement.scrollTop=100000'
# 执行操作
browser.execute_script(jsBottom)
# 再睡两秒
time.sleep(2)

# 获取下一页按钮的对象
nextPageButton=browser.find_element(By.XPATH,'//div[@id="page"]//a/span[@class="n-word_1TXWP"]')
# 点击按钮下一页，到页面下一页
nextPageButton.click()
# print(nextPageButton)   #<selenium.webdriver.remote.webelement.WebElement (session="8c401fdd23fd507747bc2792bcc29c93", element="f.DA4F8E7834548E8230466FFB80EBF333.d.D91C8A2B1F84BA5FFEBAA2380116A761.e.53")>
# 再睡两秒
time.sleep(2)

# 回到上一页
browser.back()
# 再睡两秒
time.sleep(2)

# 再回到第二页，也就是前进一页
browser.forward()
# 再睡三秒
time.sleep(3)

# 最后退出
browser.quit()




