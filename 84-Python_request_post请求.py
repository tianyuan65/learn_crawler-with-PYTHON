# _*_ coding : utf-8 _*_
# @Time : 2025/7/23 16:22
# @Author : 田园
# @File : 84-Python_request_post请求
# @Project : 83-Python_requests_get请求.py

import requests

# 访问地址
url='https://fanyi.baidu.com/sug'
# 请求头，UA反爬
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
# 参数
data={
    'kw':'eye'
}
# 发送post请求
# url--请求地址
# data--请求参数
# kwargs/headers--数据(字典类型的数据)
response=requests.post(url=url,data=data,headers=headers)
# 解码，依旧用.text
content=response.text
print(content)

import json
obj=json.loads(content)
print(obj)

# 总结：
# post请求不需要编解码
# post的请求参数是data
# 不需要请求对象的定制
# 不同于urllib的post请求，requests的post请求使用起来更加方便，因为requests唯一一个非转基因的、Python自己封装的Python库，因此使用起来没有那么多的顾虑
