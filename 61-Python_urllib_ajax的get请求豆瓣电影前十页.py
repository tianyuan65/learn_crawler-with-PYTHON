# _*_ coding : utf-8 _*_
# @Time : 2025/2/23 16:51
# @Author : 田园
# @File : 61-Python_urllib_ajax的个体请求豆瓣电影前十页
# @Project : 爬虫

import urllib.request
import urllib.parse

# 第一页的请求地址 0-20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20

# 第二页请求地址  21-40
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20

# 第三页请求地址  41-60
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20

# 第四页请求地址  61-80
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=60&limit=20

# 第五页请求地址  81-100
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=80&limit=20

# 第六页请求地址  101-120
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=100&limit=20

# 第七页请求地址  121-140
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=120&limit=20

# 第八页请求地址  141-160
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=140&limit=20

# 第九页请求地址  161-180
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=160&limit=20

# 第十页请求地址  181-200
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=180&limit=20

# page    1     2     3     4
# start   0    20    40    60
# start=(page-1)*20

# UA反爬
# headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

# 将豆瓣电影前十页的数据下载到本地
# 1. 请求对象定制
# 2. 获取响应数据
# 3. 将数据下载到本地

# 定义一个函数，在里面请求对象定制
def createRequest(page):
    # 在这个函数内请求对象定制
    # 声明baseUrl，以便于在后面进行拼接
    baseUrl='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data={
        # page和start的规律关系上面写了
        'start':(page-1)*20,
        'limit':20
    }
    # 用urlencode方法，将字典中的数据转换为Unicode格式
    newData=urllib.parse.urlencode(data)
    # 将基础路径和转换为Unicode格式之后的数据进行拼接
    lastUrl=baseUrl+newData
    print(lastUrl)
    # UA反爬
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
    # 1. 正式请求对象定制
    request=urllib.request.Request(url=lastUrl,headers=headers)
    # 返回request
    return request

# 获取响应数据，并接收调用时传递的acceptRequest
def getContent(acceptRequest):
    # createRequest函数中返回了request，在下面调用createRequest函数时，已用变量acceptRequest接收，所以在这里就可以正常作为参数穿进去了
    response=urllib.request.urlopen(acceptRequest)
    content=response.read().decode('utf-8')
    # 返回content
    return content

# 3. 将数据下载到本地，接收page参数
def downloadFilm(page,acceptContent):
    # 方法一：即将创建若干文件，将文件名根据page进行分类。且在这里必须将page进行强制类型转换，page是int型，必须转换为str才可拼接
    with open('filmList'+str(page)+'.json','w',encoding ='utf-8') as file:
        file.write(acceptContent)
    # 方法二：
    # file.open('filmList'+str(page)+'.json','w',encoding ='utf-8')
    # file.write(acceptContent)
    # file.close()

# if判断内，声明会输入的数字，也就是起始页码和结束页码，并用for循环获取起始页码和结束页码之间的步长，最后调用createRequest函数
if __name__=='__main__':
    # 声明会输入在控制台的数字
    startPage=int(input('请输入起始页码'))
    endPage=int(input('请输入终止页面'))

    # 遍历
    for page in range(startPage,endPage+1):
        # 每一页都有自己的请求对象定制，调用createRequest时，
        print(page)
        # 因为createRequest函数最后将request返回了，所以在这里可以用acceptRequest变量接收其值
        # 这就是作用域的知识点了，局部作用域的数据不能在全局或另一个局部中使用，想用就在函数内返回，并在需要的函数中作为参数传递进去。
        acceptRequest=createRequest(page)
        # 2. 获取响应数据
        acceptContent=getContent(acceptRequest)
        # 3. 将数据下载到本地，接收page为参数，用于创建若干文件后存储数据
        downloadFilm(page,acceptContent)



