# _*_ coding : utf-8 _*_
# @Time : 2025/2/16 15:20
# @Author : 田园
# @File : 53-Python_urllib_1个类型6个方法
# @Project : 爬虫

# 解码的方式不止调用read方法后，再调用decode方法，下面介绍1个类型6个方法来，进行解码
# 依旧一百度为例
import urllib.request
# 1. 定义一个url
url='http://www.baidu.com'

# 2. 模拟浏览器向服务器发送请求，并接收服务器的反馈
response=urllib.request.urlopen(url)

# 3. 1个类型和6和方法
# response的数据类型为<class 'http.client.HTTPResponse'>
# print(type(response))       #<class 'http.client.HTTPResponse'>
# 一个方法，就是read方法，read方法的弊端就是它是一字节一字节读取数据的，虽然不是不行，但实在是有点慢
# content=response.read()

# read方法传递数字参数，代表读取并返回那几个字节
# content=response.read(5)
# print(content)      #b'<!DOC'

# readline方法，只能读取一行，但快了很多
# content=response.readline()
# print(content)

# readlines方法也是一行一行地读取，但是它是直到读取完为止
# content=response.readlines()
# print(content)

# getcode()，可以返回状态码，如果是200就证明逻辑正确
# print(response.getcode())       #200

# geturl()，返回的是url地址
# print(response.geturl())        #http://www.baidu.com

# getheaders()，返回的是一些状态信息，也就是响应头的信息
print(response.getheaders())

# 1个类型 - HTTPResponse
# 6个方法 - read(),readline(),readlines(),getcode(),geturl(),getheaders()

