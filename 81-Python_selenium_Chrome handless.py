# _*_ coding : utf-8 _*_
# @Time : 2025/4/16 19:35
# @Author : 田园
# @File : 81-Python_selenium_Chrome handless
# @Project : 079-Python_selenium_交互.py

# 导入
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# # 旧版写法：
# # chrome_options = Options()
# # chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--disable-gpu')

# # 新版写法：
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# # path的值是自己的Chrome浏览器的文件路径，不知道怎么着，就在桌面的Chrome浏览器快捷键处右键，点击打开文件所在位置
# # path = r'C:\Users\田园\AppData\Local\Google\Chrome\Application\chrome.exe'
# # chrome_options.binary_location = path

# # 创建浏览器/驱动对象
# browser = webdriver.Chrome(options=options)

# # 调用get方法来获取数据
# browser.get('http://www.baidu.com/')

# print(browser)
# browser.save_screenshot('imgs/mimi.jpg')

# 封装的headless
# 定义一个shareBrowser函数，函数内进行创建驱动的操作，最后返回browser。需要用到的时候直接调用shareBrowser函数即可。
def shareBrowser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    # 创建浏览器/驱动对象
    browser = webdriver.Chrome(options=options)

    # 返回驱动
    return browser

# 调用shareBrowser函数
browser=shareBrowser()
# 调用get方法，传入访问地址作为参数来获取数据
browser.get('http://www.baidu.com/')
print(browser)  #<selenium.webdriver.chrome.webdriver.WebDriver (session="c94919a690f79a81a61bf73fa650c78e")>
