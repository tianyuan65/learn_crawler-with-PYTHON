# _*_ coding : utf-8 _*_
# @Time : 2025/2/21 21:27
# @Author : 田园
# @File : 57-Python_urllib_get请求的urlencode方法
# @Project : 爬虫

# urlencode方法的应用场景：多个参数的时候
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=谷江山1&gender=男

# import urllib.parse
#
# data={
#     'wd':'谷江山',
#     'gender':'男',
#     'job':'配音演员'
# }
# # 调用urlencode方法，并向其中传入字典，就会将字典中的键值对用&拼接起来
# a=urllib.parse.urlencode(data)
# print(a)    #wd=%E8%B0%B7%E6%B1%9F%E5%B1%B1&gender=%E7%94%B7&job=%E9%85%8D%E9%9F%B3%E6%BC%94%E5%91%98

# 获取https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=%E8%B0%B7%E6%B1%9F%E5%B1%B1&gender=%E7%94%B7&job=%E9%85%8D%E9%9F%B3%E6%BC%94%E5%91%98的网页源码
import urllib.request
import urllib.parse

# 声明基础路径baseURL，以便于拼接
baseUrl='https://www.baidu.com/s?'
data={
    'wd':'谷江山',
    'gender':'男',
    'job':'配音演员',
    'location':'北京'
}

# 调用urlencode方法，将字典中的汉字字符数据转换为Unicode格式
newData=urllib.parse.urlencode(data)
# print(newData)  #wd=%E8%B0%B7%E6%B1%9F%E5%B1%B1&gender=%E7%94%B7&job=%E9%85%8D%E9%9F%B3%E6%BC%94%E5%91%98&location=%E5%8C%97%E4%BA%AC

# 拼接基础路径和字典转化后的数据，这是请求资源路径
lastUrl=baseUrl+newData

# UA反爬
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
# 请求对象定制
request=urllib.request.Request(url=lastUrl,headers=headers)
response=urllib.request.urlopen(request)
# 获取网页源码的数据
content=response.read().decode('utf-8')
print(content)