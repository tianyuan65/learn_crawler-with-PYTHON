# _*_ coding : utf-8 _*_
# @Time : 2025/2/28 20:16
# @Author : 田园
# @File : 63-Python_urllib_异常
# @Project : 爬虫_note.md

import urllib.request
# 引入Error
import urllib.error

# 原地址
# url='https://blog.csdn.net/kkiron/article/details/145614002'
# 错地址，这是导致HTTPError的原因之一
# url='https://blog.csdn.net/kkiron/article/details/1456140020'

# 错地址，这是导致URLError的原因之一，就是主机部分出问题了
url='https://ahahahahahagagaougagagahahahahahaha.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

# 捕获异常
try:
    # 请求对象定制
    request=urllib.request.Request(url=url,headers=headers)
    # 模拟浏览器向服务器发送请求
    response=urllib.request.urlopen(request)
    # 解码
    content=response.read().decode('utf-8')
    print(content)
# 调用urllib.error的HTTPError，表示是HTTPError类型的，也就是锚点部分写错路径地址导致的错误
except urllib.error.HTTPError:
    # 但需要告诉用户，是因为别的问题
    print('系统正在升级...')
# 调用urllib.error的URLError，表示是URLError类型的，也就是主机部分出现错误导致的
except urllib.error.URLError:
    print('系统正在维护...')


