# _*_ coding : utf-8 _*_
# @Time : 2025/3/10 11:43
# @Author : 田园
# @File : 72-Python_解析_jsonpath解析淘票票
# @Project : 爬虫_note.md

import urllib.request
import json
import jsonpath

url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1741526795585_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

# 反爬
headers = {
    # 带冒号的请求头一般是不好使的，而且不但没作用还会报错
    # ':authority':'dianying.taobao.com',
    # ':method':'GET',
    # ':path':'/cityAction.json?activityId&_ksTS=1741526795585_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme':'https',
    'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # accept-encoding请求头的值，在爬虫中需要被注释掉，
    # 'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'zh-CN,zh;q=0.9',
    'bx-v':'2.5.28',
    'cookie':'t=d40bdca5558c500c6aa1309290cf868a; cookie2=1aefcff07205818dee6c55304610c0a2; v=0; _tb_token_=f67863793e9e8; cna=MQEbGHFp+xsCAVXLFYf7bU6r; xlly_s=1; tfstk=gDhoCiViwYy7wYoO2mPWB46kCUvxPaNQADCLvWEe3orjwu3L26lnX2C-eJUptkmTD6L7wpNnxomQ28Frtx1n52GJPWL7N4NQThK96X0SPWapqSIXDq8URW4z39Yn24NQTnK96C3SPc5cmbcUTEV4-yazTuzeo-z_0_zFayS2oyZ4T_5z4I74yPCU8ToEuE4Q0kPUUbMH4ulEwj-qvyxTayzqiz2ubqA1T6mP68qZnofevj4kYluzm6532NRYjq0Jq1gYNfmgW0dVZc0E5vymti-gAj0qavufqEPioxHTExxPtoh8cRhzswRro7quQj2N-1nZo2kTnjLw17Vz4vFSJNx-obm-Pj0d8tPuwx2iZ5R14kHxSX4nOHOmj2usL-chqgrG3OJ0D6a2JjWCd8zbolCpgVll9qYhSEYcIkwzlzr9oEXCd8zbolLDoO0QUrazX; isg=BEhIJhi7u6apTtcqoJnM_O2JGbZa8az78RsjGQL5GUO23epHqgMSihOTVaWta2TT',
    'priority':'u=1, i',
    'referer':'https://dianying.taobao.com/',
    'sec-ch-ua':'"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Windows',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-requested-with':'XMLHttpRequest'
}

# 请求对象定制
request=urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
# 解码获取源码
content=response.read().decode('utf-8')
# 打印源码可以得到jsonp开头的数据，但这不符合可以解析的条件，
# print(content)
# 因此需要对获取到的源码content，调用split方法进行切割，且需要两次切割，目的是提取JSONP响应中可以被解析的json数据，去掉外层的回调函数包裹。
# 第一次切割是根据(切割，将jsonp和json数据割开，并提取下标为1部分的数据，也就是json数据；第二次分割用)，还是提取下标为0的json数据部分，去掉最后的;
content=content.split('(')[1].split(')')[0]
# content=content.split('(')
# print(content)

# jsonpath只能解析本地文件，因此需要将数据下载到本地
with open('72-Python_解析_jsonpath解析淘票票.json','w',encoding='utf-8') as file:
    file.write(content)

# 创建新文件下载到本地后，需要的数据只有城市名，也就是json数据里的regionName属性的值
loadedObj=json.load(open('72-Python_解析_jsonpath解析淘票票.json','r',encoding='utf-8'))
# 声明cityName用来接收数据，调用jsonpath的jsonpath方法，传入反序列化的数据loadedObj做第一个参数，第二个参数是想要提取的值的属性名
cityName=jsonpath.jsonpath(loadedObj,'$..regionName')
print(cityName)


