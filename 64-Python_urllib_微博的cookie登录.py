# _*_ coding : utf-8 _*_
# @Time : 2025/3/1 16:09
# @Author : 田园
# @File : 64-Python_urllib_微博的cookie登录
# @Project : 爬虫_note.md

# 适用场景：在进行数据采集时，需要绕过登录，进入到某个指定的页面。
# 个人信息页面是utf-8，但还是报了UnicodeDecodeError，因为并未进入到个人信息页面，而是跳转到了登录页面
# 那么登录页面就不是utf-8，所以报错，这是常见的反爬手段。

# 什么情况下才会访问不成功？
# 在请求头的信息不够时，访问就会失败

import urllib.request

url='https://weibo.com/u/7534244872'

# 反爬：UA和cookie
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # cookie中携带着用户的登录信息，如果有登录之后的cookie，那就可以携带着cookie进入到登陆之后的任何页面
    'cookie':'XSRF-TOKEN=XaulXbjXbdNg_VmlGLYfp0eA; SCF=AjaLQBTMzO0XaVve-LHo63nv_-Lxt95_Hziet13vjZsLncz1-HYT6CgF2aM2i_IwUtDdNFlAAqne9RC_kVih_G8.; _s_tentry=weibo.com; Apache=4522188140868.185.1740813514085; SINAGLOBAL=4522188140868.185.1740813514085; ULV=1740813514186:1:1:1:4522188140868.185.1740813514085:; SUB=_2A25KxrqgDeRhGeFL6FYT9CrEzD6IHXVpvbJorDV8PUNbmtANLVjBkW9NQjji3g3jL61gBVFBg93dhqiAaADS8KrD; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF9s0I19FAkwo7i4HrhY.ZY5JpX5KzhUgL.FoMfe0BEShBRS0z2dJLoI0nLxK-L1h-LBKnLxK-LB--LBoqLxK-L1-eLBo5LxKBLB.BL12BLxKqL1-eL1h5LxKBLB.BL12-41Btt; ALF=02_1743411184; WBPSESS=Dt2hbAUaXfkVprjyrAZT_NXVJvTjtJHtzAH-ou5Emb49XWQtRHUKE3MZExgEl_QAVB6YNaywKesGo0iOhw0JAv0CmBEDmtEsbe-FgsiIBlAi9ShZ4Iui1vEQ3AgYtGxCS2JIOI3HTggd2aZzvQeOfanU5mJiXON3RiNZx7mThOUWdq-ERwowRrFe3X1BS_jbYApm8GbZtDMd0IVRkM9a1g==',
    # 判断当前路径是否由上一个路径进来的，一般情况下是做图片防盗链的，简单来说就是如果不是通过referer的地址登录来的，就不让你下载图片
    'referer':'https://weibo.com/u/7534244872'
}

# 请求对象定制
request=urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
# 获取响应的数据，虽然右键检查登录页面后依旧是utf-8，但显然不是，
content=response.read().decode('utf-8')
# 将解码格式换成gb2312，才可以正常创建文件并写入数据，gb2312是登录页面的编码
# content=response.read().decode('gb2312')
# print(content)
# 将数据保存到本地
with open('weibo.html','w',encoding='utf-8') as file:
    file.write(content)

