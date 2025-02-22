# _*_ coding : utf-8 _*_
# @Time : 2025/2/22 12:49
# @Author : 田园
# @File : 58-Python_urllib_post请求-百度翻译
# @Project : 爬虫

# post请求，post的参数在请求体中
import urllib.request
import urllib.parse

# 请求地址
url='https://fanyi.baidu.com/sug'

# UA反爬
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

# 在浏览器中取得的数据
data={
    # 在sug的preview中可以查看到
    'kw':'spider'
}

# post请求的参数必须进行编码，意思就是需要Unicode格式的数据，若不进行转换，就会报错，报需要转换为字节形式数据的错。
# 在这里就是调用urlencode方法机型编码后，还需要调用一次encode方法，来进行进一步编码
newData=urllib.parse.urlencode(data).encode('utf-8')
# print(newData)      #kw=spider

# 请求对象的定制
# 查看Request方法的源码就可以了解到，该方法的前三个参数至关重要，分别是url、data和headers，之前请求对象定制时，只写了url和headers，但这次data参数的值也有了，那就作为参数传递进去，用于获取数据和反爬。
# post请求的参数，是不会拼接在url的后面的，而是需要放在请求对象定制的参数中
request=urllib.request.Request(url=url,data=newData,headers=headers)
# print(request)  #<urllib.request.Request object at 0x0000017DE9606E40>

# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
# print(response)     #<http.client.HTTPResponse object at 0x00000235DDE8ACE0>
# 获取相应的数据
content=response.read().decode('utf-8')
print(content)

# post请求方式的参数，必须进行编码，newData=urllib.parse.urlencode(data)
# urlencode编码后需要encode编码，newData=urllib.parse.urlencode(data).encode('utf-8')
# 参数是放在请求对象定制的方法中，request=urllib.request.Request(url=url,data=newData,headers=headers)


# decode方法是解码，encode方法是编码
# 可以理解为：url，headers，data为可变化的材料，通过Request进行合成炼丹，变成了一个个性化丹药（网址），再通过urlopen将这丹药吃了（打开）
# 这节内容：使用urllib-post的方法对参数进行爬取