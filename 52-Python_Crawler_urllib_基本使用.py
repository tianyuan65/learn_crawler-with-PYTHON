# _*_ coding : utf-8 _*_
# @Time : 2025/2/16 12:35
# @Author : 田园
# @File : 01-Crawler_urllib_基本使用
# @Project : 爬虫

# 使用urllib来获取百度首页的源码，从而可以在其中获取真正想要的数据
# 导入urllib库下的request
import urllib.request
# 1. 定义一个url，指的是要访问的地址，在这里就是百度首页的地址
url='http://www.baidu.com'

# 2. 模拟浏览器向服务器发送请求，并声明一个变量接收服务器返回的反馈
response=urllib.request.urlopen(url)
# 从服务器返回的数据的数据类型是HTTPResponse
# print(type(response))   #<class 'http.client.HTTPResponse'>

# 3. 接收的response里有响应头、响应体、响应行等，需要做的是从中提取响应中的页面的源码
# 调用read方法，提取页面源码，声明变量content来接收其内容，返回的是字节形式的二进制数据，
# 在下一步需要做的就是，将这些二进制的数据转换为字符串类型的数据，这一步骤叫解码，
# 解码方法为decode()，参数位置传对应页面的编码格式，格式为decode('编码的格式')，编码格式就是charset的值
content=response.read().decode('utf-8')

# 4. 打印数据
print(content)


