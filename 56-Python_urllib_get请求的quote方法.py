# _*_ coding : utf-8 _*_
# @Time : 2025/2/21 17:37
# @Author : 田园
# @File : 56-Python_urllib_get请求的quote方法
# @Project : 爬虫

# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=%E8%B0%B7%E6%B1%9F%E5%B1%B1&fenlei=256&rsv_pq=0x92bf6c4b015a1c11&rsv_t=0254vPC%2FIg6M7eQ7Ye%2FPgT4GkfL8BSZou%2Bui9xICjyADThD7H8ntjMjpjXmB&rqlang=en&rsv_dl=tb&rsv_enter=1&rsv_sug3=13&rsv_sug1=2&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=2385&rsv_sug4=3251&rsv_sug=1
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=%E8%B0%B7%E6%B1%9F%E5%B1%B1
# %E8%B0%B7%E6%B1%9F%E5%B1%B1，这一部分就是Unicode编码的谷江山

# 需求：获取 https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=谷江山 的网页源码

import urllib.request
import urllib.parse

# url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=谷江山'
# url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=%E8%B0%B7%E6%B1%9F%E5%B1%B1'

url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd='

# 将谷江山这三个字，变成Unicode编码的格式
# 需要依赖urllib.parse，调用它下面的quote方法，并传递汉字人名作为参数
name=urllib.parse.quote('谷江山')
# %E8%B0%B7%E6%B1%9F%E5%B1%B1就是谷江山的Unicode编码
# print(name)     #%E8%B0%B7%E6%B1%9F%E5%B1%B1
# 得到了谷江山的Unicode编码后，可以将路径和name进行拼接
url=url+name
# print(url)  #https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=%E8%B0%B7%E6%B1%9F%E5%B1%B1

# 请求对象定制，是为了解决反爬的第一种手段
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
# 请求对象的定制，记得关键字传参
request=urllib.request.Request(url=url,headers=headers)
# 模拟一个浏览器向服务器发送请求
response=urllib.request.urlopen(request)
# 读取响应的内容
content=response.read().decode('utf-8')
# 打印数据
print(content)

