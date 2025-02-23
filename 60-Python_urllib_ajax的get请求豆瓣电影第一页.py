# _*_ coding : utf-8 _*_
# @Time : 2025/2/22 21:08
# @Author : 田园
# @File : 60-Python_urllib_ajax的get请求豆瓣电影第一页
# @Project : 爬虫

# get请求
# 获取豆瓣电影动作片第一页的数据，并保存起来
import urllib.request

# 请求路径
url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

# UA反爬
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

# 请求对象的定制
request=urllib.request.Request(url=url,headers=headers)
# 获取相应的数据
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')

# print(content)

# 将数据下载到本地
# 创建一个名为douban.json的文件，并能设置访问模式为w。因为数据是json字符串形式的，所以创建并保存文件的后缀也是.json。
# 且这里需要注意一点，open方法默认情况下使用的是gbk的编码，若想要保存为汉字格式，则需要在open方法中需要传入第三个参数encoding='utf-8'，来指定编码格式为utf-8。
# 虽然不像老师的那样不报错了，但是进入文件中就可以发现需要UTF-8的编码才可以。
# file=open('douban.json','w',encoding='utf-8')
# # 调用write方法，将数据写入到file中
# file.write(content)

# 这样也可以实现创建新文件，并将数据写入到文件中
# with 就是为了防止因发生异常而没有关闭文件，会自动关闭文件，上一种方法是需要调用close方法来手动关闭的
with open('douban1.json','w',encoding='utf-8') as file:
    file.write(content)



# 后端返回JSON，前端进行数据渲染