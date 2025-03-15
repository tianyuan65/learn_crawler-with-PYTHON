# _*_ coding : utf-8 _*_
# @Time : 2025/3/12 14:54
# @Author : 田园
# @File : 73-Python_解析_bs4的基本使用
# @Project : 爬虫_note.md

from bs4 import BeautifulSoup

# 通过解析本地文件，讲解bs4的基础语法
# 声明变量soup，调用BeautifulSoup方法，因为解析的是本地文件，所以再调用open方法，打开想要解析的文件作为第一个参数，第二个参数为lxml，因为bs4的内核是lxml。
# 但打印soup后会发现报错，报错原因是Unicode解码错误，因为默认打开的文件的编码格式为gbk，所以打开文件时需要指定编码，就是open方法中添加第二个参数encoding，并设置编码格式为utf-8
soup=BeautifulSoup(open('73-Python_解析_bs4的基本使用-解析本地文件.html',encoding='utf-8'),'lxml')

# 根据标签名查找节点，找到并返回的是第一个符合条件的数据，也就是谁在前面，谁就被抽
# print(soup.a)   #<a href="">百度一下</a>
# 获取标签的所有属性和属性值
# print(soup.a.attrs) #{'href': '', 'id': '', 'class': []}

# bs4的三个函数
# find()，和根据标签名查找节点一样，会返回第一个符合条件的数据，返回的是一个对象
# print(soup.find('a'))   #<a class="" href="" id="">百度一下</a>
# 根据条件找到指定的标签对象，
# 这个是根据title属性的值找到的对应的标签对象
# print(soup.find('a',title="a2"))    #<a href="https://www.youtube.com/" title="a2">油管</a>
# 根据class的属性值找对应的标签对象，class这个关键字在Python中用过了，因此不能直接写class，但写成class_就代表通过class的属性值找到相应的标签对象
# print(soup.find('a',class_="a1"))   #<a class="a1" href="" id="">百度一下</a>
# print(soup.find('li'))  #<li>Sariel</li>

# find_all()，会返回所有符合条件的数据，返回的是一个列表
# 返回了一个列表，列表中元素就是本地文件中所有的a标签
# print(soup.find_all('a'))   #[<a class="a1" href="" id="">百度一下</a>, <a href="https://www.youtube.com/" title="a2">油管</a>]
# 若想要获取多个标签的数据，就需要在find_all的参数中传入列表格式的数据，就是将想要获取的标签名，用[]括起来传进find_all方法中
# print(soup.find_all(['a','span']))  #[<a class="a1" href="" id="">百度一下</a>, <span>哈哈哈哈</span>, <a href="https://www.youtube.com/" title="a2">油管</a>]
# 获取所有li标签
# print(soup.find_all('li'))  #[<li>Sariel</li>, <li>Vilhelm</li>, <li>Sylus</li>]
# 通过传递第二个参数limit，可以获取指定标签的前几个数据
# print(soup.find_all('li',limit=2))  #[<li>Sariel</li>, <li>Vilhelm</li>]

# select()，根据选择器得到节点对象【推荐】，select方法返回的是一个列表
# select方法会返回多个数据，这么写就跟find_all的作用一样
# print(soup.select('a')) #[<a class="a1" href="" id="">百度一下</a>, <a href="https://www.youtube.com/" title="a2">油管</a>]

# 根据class查找标签，可以用.来代表class，叫做类选择器
# print(soup.select('.a1'))   #[<a class="a1" href="" id="">百度一下</a>]

# 根据id查找标签，需要在前面加个#，这是前端的知识
# print(soup.select('#l2'))   #[<li id="l2">Vilhelm</li>]

# 属性选择器，通过属性来寻找对应的标签
# 找到有id的li标签
# print(soup.select('li[id]'))    #[<li id="l1">Sariel</li>, <li id="l2">Vilhelm</li>]
# print(soup.select('li[class]')) #[<li class="l3">Sylus</li>]
# 找到id为l2的li标签
# print(soup.select('li[id="l2"]'))   #[<li id="l2">Vilhelm</li>]

# 层级选择器
# 后代选择器
# 空格，找到div下面的li
# print(soup.select('div li'))    #[<li id="l1">Sariel</li>, <li id="l2">Vilhelm</li>, <li class="l3">Sylus</li>]
# 还可以通过属性获取的想要的标签
# print(soup.select('div li[class]'))     #[<li class="l3">Sylus</li>]

# 子代选择器，指定的某标签的第一级子标签
# 大于，找到div下面的li，需要一层一层地将从父标签到子标签，再到其子标签的过程列出来
# 很多计算机编程语言中，如若不加空格就不会输出内容，但在bs4中会显示内容，还不会报错
# print(soup.select('div>ul>li')) #[<li id="l1">Sariel</li>, <li id="l2">Vilhelm</li>, <li class="l3">Sylus</li>]
# print(soup.select('div>ul>li[id="l2"]'))    #[<li id="l2">Vilhelm</li>]

# 逗号，组合使用
# 需求：找到a标签和li标签的所有对象
# print(soup.select('a,li,span')) #[<li id="l1">Sariel</li>, <li id="l2">Vilhelm</li>, <li class="l3">Sylus</li>, <a class="a1" href="" id="">百度一下</a>, <span>哈哈哈哈</span>, <a href="https://www.youtube.com/" title="a2">油管</a>]

# 节点信息
# 获取节点内容-需求：获取div下span标签里的内容
# select函数返回的是一个列表，列表没有string属性，直接调用获取节点信息的string方法和get_text()，就会报错。
# 因此想要通过string属性或get_text方法获取标签对象，就通过下标的方式来获取列表里的内容
# obj=soup.select('#d1')[0]
# 若标签对象中，只有内容，那string和get_text()没有区别，都可以使用，但如果标签独对象中一旦除了内容，还有了层级关系，string就获取不到数据，而get_text()就可以，
# 想要使用string实现的话，就需要将标签对象的子标签或子孙标签都一一列出来，
# print(obj.string)   #None
# obj=soup.select('#d1>span')[0]
# print(obj.string)   #嘿嘿嘿
# 因此推荐使用get_text()
# print(obj.get_text())   #嘿嘿嘿

# 节点的属性-需求：通过属性名获取p标签
# 通过id获取p标签，依旧因为调用select函数返回的是一个列表，而无法直接通过.name来获取节点的属性，因此需要先获取列表中的元素，再调用.name
# obj=soup.select('#p1')[0]
# name时标签的名字
# print(obj.name) #p
# attrs，将该标签拥有的所有属性值整理成一个字典返回
# print(obj.attrs)    #{'id': 'p1', 'class': ['p1'], 'style': 'font-size:30px;color:aqua'}

# 获取节点属性-需求：获取p标签的class属性
obj=soup.select('#p1')[0]
# 调用标签对象的attrs属性，返回的是字典，不同于其他返回的是列表，可以调用get方法，并传入标签的属性来获取指定的属性值
print(obj.attrs.get('class'))   #['p1']
print(obj.get('class')) #['p1']
print(obj['class']) #['p1']




