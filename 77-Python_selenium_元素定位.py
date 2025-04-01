# _*_ coding : utf-8 _*_
# @Time : 2025/3/30 21:55
# @Author : 田园
# @File : 77-Python_selenium_元素定位
# @Project : 76-Python_selenium_基本使用.py

# 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# selenium4版本，做了些调整，元素定位的方法需要导入By
from selenium.webdriver.common.by import By
# 创建浏览器操作对象
service=Service('chromedriver.exe')
driver=webdriver.Chrome(service=service)

# 访问地址
url='https://www.baidu.com'
driver.get(url)

# 元素定位
# By.ID：找到百度一下中输入框的id属性的值，根据id值查找对象，下面的这个方法被弃用，改在find_element方法第一个参数位中传递属性
# button=driver.find_element_by_id('kw')
# 下面这两种方法都可
# button=driver.find_element(By.ID,'kw')
# button=driver.find_element('id','kw')   #<selenium.webdriver.remote.webelement.WebElement (session="44a67855f0195c1fa5b23f451abc9e21", element="f.41A8D0C3ED84162FA28C7C2464363FE3.d.E4A3F8D5CA84027DC136423FD091CAB7.e.6")>
# print(button)

# By.NAME：根据标签属性的属性值来获取对象
# button=driver.find_element('name','wd')
# button=driver.find_element(By.NAME,'wd')
# print(button)   #<selenium.webdriver.remote.webelement.WebElement (session="8e5ee684d112dbd120d7c5ab333bc1a2", element="f.EB23DCF9813F246BFEAEF8E8373FB1B9.d.5D56A849A80B1833F70BFF1C40010F9F.e.6")>

# By.XPATH：根据xpath语句获取对象
# button=driver.find_element(By.XPATH,'//input[@id="kw"]')
# button=driver.find_element('xpath','//input[@id="kw"]') #<selenium.webdriver.remote.webelement.WebElement (session="892b79716d3ee5eb5b2fe81f717a0803", element="f.6EDE7032027F25C7AF5B7A51A71D5B08.d.625011CC8E253BCF193BA6F4A6D0BE6D.e.6")>
# print(button)

# By.TAG_NAME：根据标签名获取对象，但deepseek建议慎用，还有CLASS_NAME，说是易变化
# button=driver.find_element(By.TAG_NAME,'input') #<selenium.webdriver.remote.webelement.WebElement (session="a2dfc856c2d15a7f01d4190b1b2fb040", element="f.0DA09CE271A2DB33E63D88C821D2FDA0.d.0881AB996D68E8CE32E7815BD2DAE19B.e.12")>
# 这么写不好使，tagName和className用上面的全大写并用下划线隔开的方式写
# button=driver.find_element('tag_name','input')
# print(button)

# By.CSS_SELECTOR：使用的是bs4的语法来获取对象，且因为是复杂情况时选择使用的，deepseek强推，说是性能最优，
# button=driver.find_element(By.CSS_SELECTOR,'#kw')   #<selenium.webdriver.remote.webelement.WebElement (session="fef4fb35ab1e6f4807ab03a146c2f472", element="f.3C352DDC956ECEE3587720C15CFBED8E.d.0EB16F0DE2D9A4382EA05BFCC2684EC6.e.6")>
# print(button)

print(int(input('enter a number')))