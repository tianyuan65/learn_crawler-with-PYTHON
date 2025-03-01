# _*_ coding : utf-8 _*_
# @Time : 2025/3/1 20:30
# @Author : 田园
# @File : 66-Python_urllib_代理
# @Project : 爬虫_note.md

import urllib.request

url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=ip'

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

# 请求对象定制
request=urllib.request.Request(url=url, headers=headers)
# 模拟浏览器访问服务器
# response=urllib.request.urlopen(request)
# 代理IP
proxies={
    # key:value格式，value是主机加上端口号，就是IP+PORT
    # 这个是免费的IP所以失败了，想成功需要花钱注册一个，然后生成成功率高的API，将API地址放到输入栏上就可以得到一个代理IP。
    'http':'162.223.90.130:80'
}
# handler对象，调用urllib.request的ProxyHandler方法，查看ProxyHandler源码可发现需要传递proxies，其值为字典类型的数据，这个字典类型的数据就是ip地址
handler=urllib.request.ProxyHandler(proxies=proxies)
# opener对象
opener=urllib.request.build_opener(handler)
# 调用你open方法，向服务器发送请求
response=opener.open(request)
content=response.read().decode('utf-8')

# 保存到本地
with open('daili.html','w',encoding='utf-8') as file:
    file.write(content)

