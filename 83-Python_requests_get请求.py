# _*_ coding : utf-8 _*_
# @Time : 2025/4/26 13:54
# @Author : 田园
# @File : 83-Python_requests_get请求
# @Project : 079-Python_selenium_交互.py

# urllib
# (1). 一个类型六个方法
# (2). get请求
# (3). post请求 当时案例-百度翻译
# (4). ajax的get请求
# (5). ajax的post请求
# (6). cookie登录  当时案例-微博
# (7). 代理，Handler Process和快代理，只不过代理得花钱，我没整

# requests
# (1). 一个类型六个属性
# (2). get请求
# (3). post请求
# (4). 代理
# (5). cookie  破解验证码
# (6).
# (7).

# 导入requests
import requests
# 定义访问网址
url='http://www.baidu.com/s'
# 请求头，UA反爬
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
# 参数，在浏览器中取得的数据
data={
    'wd':'北京'
}
# 请求对象定制
# get请求
# get方法的三个参数
#     url--请求资源路径
#     params--参数
#     kwargs/headers--数据(字典类型的数据)
response=requests.get(url=url,params=data,headers=headers)
# 解码，用.text
content=response.text
print(content)

# 总结：
# 参数使用params传递
# 参数无需urlencode编码
# 不需要请求对象定制
# 请求资源路径，就是url中的 ? 可以加，也可以删除掉

# 只要能获取到数据用什么手段都无所谓，urllib和request都可以

