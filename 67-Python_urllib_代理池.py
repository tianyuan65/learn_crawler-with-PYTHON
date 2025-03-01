# _*_ coding : utf-8 _*_
# @Time : 2025/3/1 21:13
# @Author : 田园
# @File : 67-Python_urllib_代理池
# @Project : 爬虫_note.md

import urllib.request
import random

# 代理池，是一个列表类型的数据，里面是一个一个的代理，代理是字典类型的数据
proxiesPool=[
    {'http':'162.223.90.130:80'},
    {'http': '218.87.205.29:18442'},
    {'http':'59.54.238.10:19458'}
    # {'http': '162.223.90.130:8357630'},
    # {'http': '162.223.90.130:85430'},
    # {'http': '162.223.90.130:125780'},
    # {'http': '162.223.90.130:125767880'},
    # {'http': '162.223.90.130:5780'},
    # {'http': '162.223.90.130:125766780'},
]

# 引入random后，调用random的choice方法，传入代理池做参数，就会在代理池中随机选一个
proxies=random.choice(proxiesPool)

url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=ip'

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
# 请求对象定制
request=urllib.request.Request(url=url, headers=headers)
# 创建handler对象
handler=urllib.request.ProxyHandler(proxies=proxies)
# 创建opener对象
opener=urllib.request.build_opener(handler)
# 模拟浏览器向服务器发送请求
response=opener.open(request)
# 解码
content=response.read().decode('utf-8')

with open('daili2.html','w',encoding='utf-8') as file:
    file.write(content)


# print(proxies)
