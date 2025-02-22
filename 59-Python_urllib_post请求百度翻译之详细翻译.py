# _*_ coding : utf-8 _*_
# @Time : 2025/2/22 19:16
# @Author : 田园
# @File : 59-Python_urllib_post请求百度翻译之详细翻译
# @Project : 爬虫

import urllib.request
import urllib.parse

# 请求地址
url='https://fanyi.baidu.com/sug'

# UA反爬
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

data={
    'kw': 'light'
}

# post请求的参数必须进行urlencode和encode两次编码
newData=urllib.parse.urlencode(data).encode('utf=8')

# 请求对象定制
request=urllib.request.Request(url=url,data=newData,headers=headers)

# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
# 对获取的反馈进行解码操作，传递UTF-8的意义是将字节数据解码为字符串
content=response.read().decode('utf-8')
print(content)

# 反序列化，将json字符串转为python对象
import json

obj=json.loads(content)
print(obj)
# print(type(obj))    #<class 'dict'>
