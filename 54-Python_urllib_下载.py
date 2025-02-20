# _*_ coding : utf-8 _*_
# @Time : 2025/2/20 17:25
# @Author : 田园
# @File : 54-Python_urllib_下载
# @Project : 爬虫

# 如何将视频、音频、图片等下载到本地
import urllib.request

# 下载网页
# urlPage='http://www.baidu.com'
# 第一个参数url代表下载的路径，filename是下载后文件的名字
# 在Python中，参数可以写变量名=值，或者直接写值都可，运行后可以看到文件夹中已新建一个文件
# urllib.request.urlretrieve(urlPage,'baidu.html')

# 下载图片
# pictureUrl='https://img1.baidu.com/it/u=2947501551,1597168974&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=1774'
# 这次参数写成变量名=值的格式，运行即可查看到成功下载，需要注意的是，图片需要写明后缀，否则将会被视为不知名文件，届时需要重新命名文件后缀
# urllib.request.urlretrieve(url=pictureUrl,filename='Sylus.png')

# 下载视频
# 尽量别下载b站的视频，做反爬了，运行直接报错
videoUrl='https://vdept3.bdstatic.com/mda-qm53adm1qajbswbf/cae_h264/1733451954227807608/mda-qm53adm1qajbswbf.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1740056997-0-0-f8a3abada9abe9b86600b822d7c27833&bcevod_channel=searchbox_feed&pd=1&cr=0&cd=0&pt=3&logid=0597451879&vid=9232592005464223964&klogid=0597451879&abtest=132219_1'
# 视频文件一般都用mp4做后缀，运行后在当前pycharm当中点击视频文件时，是看不到视频的，因为pycharm没有播放器，但既然已经下载到本地了，就可以到本地文件夹汇总查看播放。
urllib.request.urlretrieve(videoUrl,'Sylus.mp4')


