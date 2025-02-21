# _*_ coding : utf-8 _*_
# @Time : 2025/2/20 21:55
# @Author : 田园
# @File : 55-Python_urllib_请求对象的定制
# @Project : 爬虫

import urllib.request

url='https://www.baidu.com'

# url的组成-6个部分
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=%E8%B0%B7%E6%B1%9F%E5%B1%B1&fenlei=256&rsv_pq=0xc3853b0e008b12b0&rsv_t=87e066VcwNhNxmwBb%2BUvfM0WK0UVFfoLZWRVZnxlC5hMT0Kfl%2FtzLN1FhFLb&rqlang=en&rsv_dl=tb&rsv_enter=1&rsv_sug3=23&rsv_sug1=8&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=5405&rsv_sug4=6358&rsv_sug=1
# 1. 协议：http和https，https加了ssl加密，更加安全
# 2. 主机：就是域名，www.baidu.com
# 3. 端口号：http是80，https是443，url中可见的到这里为止。题外话-mysql是3306，oracle是1521，redis是6379，mongodb是27017
# 4. 路径：s
# 5. 参数：ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=44004473_40_oem_dg&wd=%E8%B0%B7%E6%B1%9F%E5%B1%B1&fenlei=256&rsv_pq=0xc3853b0e008b12b0&rsv_t=87e066VcwNhNxmwBb%2BUvfM0WK0UVFfoLZWRVZnxlC5hMT0Kfl%2FtzLN1FhFLb&rqlang=en&rsv_dl=tb&rsv_enter=1&rsv_sug3=23&rsv_sug1=8&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=5405&rsv_sug4=6358&rsv_sug=1
# 6. 锚点：

# user-agent:
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
# 将我的UA拿过来放到一个名为headers的字典中
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

# 因为urlopen方法中不能存储字典，所以headers不能作为参数传递进去，urlopen方法中只接收字符串和Request对象作为参数。
# 请求对象的定制，需要提前调用Request方法来声明一个Request，并将其命名为request，向Request方法中传递url路径和需要的参数headers。
# 但因为参数顺序的问题，不可以直接写路径url和需要的参数headers，因为源码中查看时可以看到，中间还有个data，因此需要关键字传参，就是变量名=值，这种格式。
request=urllib.request.Request(url=url,headers=headers)

# 随后向urlopen方法中将request对象作为参数传递进去，再向服务器发送请求并接收
response=urllib.request.urlopen(request)
content=response.read().decode('utf8')
print(content)

