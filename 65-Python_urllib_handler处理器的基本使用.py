# _*_ coding : utf-8 _*_
# @Time : 2025/3/1 19:50
# @Author : 田园
# @File : 65-Python_urllib_handler处理器的基本使用
# @Project : 爬虫_note.md

# 需求：使用handler来访问百度，来获取网页源码
import urllib.request

url='http://www.baidu.com'

# 反爬
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

# 请求对象定制
request=urllib.request.Request(url=url, headers=headers)
# handler   build_opener  open，代理IP、动态cookie、handler基本使用靠这三个实现
# 1. 调用urllib.request的HTTPHandler方法获取handler对象
handler=urllib.request.HTTPHandler()
# 2. 调用urllib.request的build_opener方法，将handler作为参数传进去，通过handler获取opener对象
opener=urllib.request.build_opener(handler)
# 3. 调用open方法，相当于之前模拟浏览器向服务器发送请求的步骤，就是调用urlopen方法一样，这里的返回值就是response
response=opener.open(request)
# 模拟浏览器向服务器发送请求
# response=urllib.request.urlopen(request)
# 随后就是正常解码
content=response.read().decode('utf-8')
print(content)
