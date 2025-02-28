# _*_ coding : utf-8 _*_
# @Time : 2025/2/28 17:45
# @Author : 田园
# @File : 62-Python_urllib_ajax的post请求肯德基官网
# @Project : 爬虫_note.md

# post请求，肯德基门店地址前十页的数据
# 第一页请求地址：https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# 表单数据 form data
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

# 第二页请求地址：https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse

# baseUrl='https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

def createRequest(page):
    baseUrl = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data={
        'cname': '北京',
        'pid':'',
        'pageIndex': page,
        'pageSize': '10',
    }
    # 将上面的data进行Unicode编码
    newData=urllib.parse.urlencode(data).encode('utf-8')
    # UA反爬
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    # 请求对象定制
    request=urllib.request.Request(url=baseUrl,data=newData,headers=headers)
    return request

def getContent(returnRequest):
    # 获取网页源码
    response=urllib.request.urlopen(returnRequest)
    # 解码
    content=response.read().decode('utf-8')
    return content

import json
# 反序列化，将json数据转换为python对象类型，并下载到本地
def downloadData(returnContent,page):
    # 创建文件并写入数据
    with open('kfc_'+str(page)+'.json','w',encoding ='utf-8') as file:
        file.write(returnContent)
if __name__ == '__main__':
    startPage=int(input('请输入起始页码'))
    endPage=int(input('请输入终止页码'))

    for page in range(startPage,endPage+1):
        # 调用请求对象定制函数
        returnRequest=createRequest(page)
        # 调用获取网页源码函数
        returnContent=getContent(returnRequest)
        # 调用下载到本地函数
        downloadData(returnContent,page)
