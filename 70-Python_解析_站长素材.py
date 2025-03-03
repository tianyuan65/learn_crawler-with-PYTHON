# _*_ coding : utf-8 _*_
# @Time : 2025/3/2 19:38
# @Author : 田园
# @File : 70-Python_解析_站长素材
# @Project : 68-Python_解析_XPath的基本使用.py

# 1. 请求对象定制
# 2. 获取网页源码
# 3. 解析并下载

# 需求：下载站长素材里小猫的前十页图片
# 第一页地址：https://sc.chinaz.com/tupian/xiaomaotupian.html
# 第二页地址：https://sc.chinaz.com/tupian/xiaomaotupian_2.html
# 第三页地址：https://sc.chinaz.com/tupian/xiaomaotupian_3.html
# 1. 请求对象定制
import urllib.request
from lxml import etree

def createRequest(page):
    if(page==1):
        url='https://sc.chinaz.com/tupian/xiaomaotupian.html'
    else:
        url='https://sc.chinaz.com/tupian/xiaomaotupian_' + str(page) + '.html'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
    request=urllib.request.Request(url=url,headers=headers)
    return request

def getContent(returnRequest):
    response=urllib.request.urlopen(returnRequest)
    content=response.read().decode('utf-8')
    return content

def downloadPng(returnContent):
    # 下载图片
    # urllib.request.urlretrieve('图片地址','文件名')
    tree=etree.HTML(returnContent)
    # xpath返回的是列表类型的数据，一般涉及到图片的网站都会进行懒加载，点开img所在的div标签，都会短暂出现属性值为lazy的class属性
    picList=tree.xpath('//div[@class="container"]/div/div/img/@data-src')
    # 懒加载的图片
    # srcList=tree.xpath('//div[@class="container"]/div/div/img/@class')
    # print(len(picList),len(srcList)) #40,40，一页40张图片
    # 遍历picList的长度
    for i in range(len(picList)):
        pictures=picList[i]
        # src=srcList[i]
        picUrl='https://'+pictures
        # 调用urlretrieve方法下载到当前文件夹
        urllib.request.urlretrieve(url=picUrl,filename='./maomaoImg/'+pictures+'.jpg')

if __name__ == '__main__':
    startPage=int(input('请输入起始页码'))
    endPage=int(input('请输入结束页码'))

    for page in range(startPage,endPage+1):
        # 函数内请求对象定制
        returnRequest=createRequest(page)
        # 获取网页源码
        returnContent=getContent(returnRequest)
        # 下载到本地
        downloadPng(returnContent)
