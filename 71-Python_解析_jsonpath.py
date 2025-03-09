# _*_ coding : utf-8 _*_
# @Time : 2025/3/3 12:32
# @Author : 田园
# @File : 71-Python_解析_jsonpath
# @Project : 68-Python_解析_XPath的基本使用.py

# 引入jsonpath
import json
import jsonpath

# 反序列化json文件中的数据，将其转换为Python的dic类型数据
loadedObj=json.load(open('71-Python_解析_jsonpath.json','r',encoding='utf-8'))
# print(loadedObj)

# 书店所有书的作者
# 与xpath不同，jsonpath路径的获取方式有一套自己的方式，比如不用/来分隔，//用$代替，/用.代替，[]里的*代表要这一对象下的全部
# authorList=jsonpath.jsonpath(loadedObj,'$.store.book[*].author')
# print(authorList)   #['竹已', '匪我思存', '梁实秋', '曹雪芹']
# 也可以通过下标来获取指定的对象的指定属性值
# authorList=jsonpath.jsonpath(loadedObj,'$.store.book[3].author')
# print(authorList)   #['曹雪芹']

# 所有的作者，$..author，这里的..就相当于xpath的//，代表获取、整合并输出该dic下，所有属性名为author的属性值
# allAuthors=jsonpath.jsonpath(loadedObj,'$..author')
# print(allAuthors)   #['竹已', '匪我思存', '梁实秋', '曹雪芹', '关心则乱']

# store下所有的元素，$.store.*，代表获取store下所有元素
# storeList=jsonpath.jsonpath(loadedObj,'$.store.*')
# print(storeList)    #[[{'category': '现言', 'author': '竹已', 'title': '难哄', 'price': 8.95}, {'category': '古言', 'author': '匪我思存', 'title': '东宫', 'price': 12.99}, {'category': '诗歌散文', 'author': '梁实秋', 'title': '快乐就是哈哈哈哈哈', 'isbn': '9787570234059', 'price': 8.99}, {'category': '现实主义文学', 'author': '曹雪芹', 'title': '红楼梦', 'isbn': '9787101086591', 'price': 22.99}], {'author': '关心则乱', 'color': '黑色', 'price': 19.95}]

# store里所有东西的price，如上面所举的例子，..代表xpath的//，因为price元素是字典store的子孙元素，所以需要两个点
# priceList=jsonpath.jsonpath(loadedObj,'$.store..price')
# print(priceList)    #[8.95, 12.99, 8.99, 22.99, 19.95]

# 第三本书，下面两种写法都可
# thirdBook=jsonpath.jsonpath(loadedObj,'$..book[2].title')
# thirdBook=jsonpath.jsonpath(loadedObj,'$.store.book[2].title')
# print(thirdBook)    #['快乐就是哈哈哈哈哈']

# 最后一本书，用@表示当前节点下，也就是book下，根据条件进行过滤
# lastBook=jsonpath.jsonpath(loadedObj,'$.store.book[(@.length-1)]')
# print(lastBook) #[{'category': '现实主义文学', 'author': '曹雪芹', 'title': '红楼梦', 'isbn': '9787101086591', 'price': 22.99}]

# 前两本书，两种方式，用下标[0,1]，或用切片的方式[:2]
# firstTwobook=jsonpath.jsonpath(loadedObj,'$..book[0,1]')
# firstTwobook=jsonpath.jsonpath(loadedObj,'$..book[:2].title')
# print(firstTwobook) #['难哄', '东宫']

# 过滤出所有包含isbn的书，获取json中的book数组中包含isbn属性的所有值
# 条件过滤需要在()的前面添加一个?
# bookContainsISBN=jsonpath.jsonpath(loadedObj,'$..book[?(@.isbn)].title')
# print(bookContainsISBN) #['快乐就是哈哈哈哈哈', '红楼梦']

# price大于10的书
# bookList=jsonpath.jsonpath(loadedObj,'$..book[?(@.price>10)].title')
# print(bookList) #['东宫', '红楼梦']

