# _*_ coding : utf-8 _*_
# @Time : 2025/3/2 9:48
# @Author : 田园
# @File : 68-Python_解析_XPath的基本使用
# @Project : 爬虫_note.md

# 在终端安装lxml失败的话，可以在pycharm的设置中手动强制安装
# 导入所需库
from lxml import etree

# xpath解析有两种文件，本地文件
# 1. 本地文件，就是和html在同一目录下的文件，或者可以说是存在电脑里的文件
# 2. 服务器响应的数据，就是response.read().decode('utf-8')，用的最多

# 解析本地文件           etree.parse()
tree=etree.parse('68-Python_解析_XPath的基本使用.html')
# print(tree)     #<lxml.etree._ElementTree object at 0x0000017F46A0FDC0>
# tree.xpath('xpath路径')，调用tree的xpath方法，将xpath路径作为参数，如果xpath路径写对了，想要啥有啥
# 1. 路径查询：查找ul下面的li
# liList=tree.xpath('//body/ul/li')
# 如下面代码所示//找的是所有的子孙节点，需要明确//后面子孙的标签，如果想一步到位就可以这么写
liList=tree.xpath('//body//li')
# print(liList)   #[<Element li at 0x2138bcc1100>, <Element li at 0x2138bcc1140>, <Element li at 0x2138bcc1180>, <Element li at 0x2138bcc11c0>]
# print(len(liList))  #4

# 2. 谓词查询：查找所有有id属性的li标签，[]内输入过滤条件，格式：div[@属性名]，查找所有有改属性名的div标签
liWithId=tree.xpath('//ul/li[@id]')
# print(len(liWithId))    #2
# //ul/li[@id]/text()，在后面加上text()，过滤出有id属性的里标签的内容
liWithContent=tree.xpath('//ul/li[@id]/text()')
# print(liWithContent)    #['Evan', 'Artem']
# 查询id为l1的li标签，要注意引号，在html文件中用了双引号，在这里就得老老实实地保持同步
liWithIdAndContent=tree.xpath('//ul/li[@id="l1"]/text()')
# print(liWithIdAndContent)   #['Evan']

# 3. 属性查询，查找id为l1的li标签的class的属性值
liWithIdAndClassValue=tree.xpath('//ul/li[@id="l1"]/@class')
# print(liWithIdAndClassValue)    #['c1']

# 4. 模糊查询，
# contains，需求：查询id属性中属性值包含字母l的li标签，输出后因为不是文本内容，所以看不太出来，最后/text()就可以看到了
liWithL=tree.xpath('//ul/li[contains(@id,"l")]/text()')
# print(liWithL)  #['Evan', 'Artem']
# starts-with，需求：查询id的值以c开头的li标签
liStartWithL=tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
print(liStartWithL) #['Victor', 'Sylus']

# 5. 逻辑运算，需求：查询id为l1和class为c1的标签
li=tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
# print(li)   #['Evan']
# | 针对的是标签，不允许通过属性来使用或，只能通过标签来使用或并正常运行下去
liList=tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')
# print(liList)   #['Evan', 'Artem']



# 解析服务器响应文件/数据  etree.HTML()



