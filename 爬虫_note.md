## Urllib
## 一、 什么是互联网爬虫？
* 如果我们把互联网那个比作一张蜘蛛网，那一台计算机上的数据就是蜘蛛网上的一个猎物，而爬虫程序就是一只蜘蛛，沿着蛛网抓取自己想要的数据。
* 解释1：通过一个程序，根据地址/域名/url(https://jd.com/)进行爬取网页，获取有用信息。
* 解释2：使用程序模拟浏览器，去向服务器发送请求，获取响应信息。
## 二、爬虫核心
* 2.1 爬取网页：爬取整个网页，包含了网页中的所有内容。
* 2.2 解析数据：将从网页中得到的数据进行解析，从中获取想要的数据。
* 2.3 难点：爬虫和反爬虫之间的博弈，爬虫就是向服务器获取数据，反爬虫就是服务器拒绝提供数据。但反爬也是有原因的，这个问题可以解决。
## 三、爬虫的用途
* 数据分析/人工数据集
* 社交软件冷启动，有一些社交软件爬取了其他社交软件(如微博)的用户数据，作为自家软件的假数据。
* 舆情监控，爬取某一时段的人流量或天气状况有关的数据后，可以分解人流量和控制灾情。
* 竞争对象监控
## 四、 爬虫分类
* 通用爬虫：我不学
  * 实例：百度，360，google，sougou等搜索引擎
  * 功能：访问网页->抓取数据->数据存储->数据处理->提供检索服务
  * robots协议：一个约定俗成的协议，添加robots.txt文件，来说明本网站的那些内容不可以被抓取，起不到限制作用，自己写的爬虫无需遵守。
  * 网站排名(SEO)
    * 1. 根据pagerank算法值进行排名(参考网站流量，点击率等指标)
    * 2. 百度竞价排名
  * 缺点：
    * 1. 抓取的数据大多是无用的
    * 2. 不能根据用户的需求来精准获取数据
* 聚焦爬虫：我会以及要学
  * 功能：根据需求，实现爬虫程序，抓取需要的数据
  * 设计思路：
    * 1. 确定爬取的url。如何获取url？
    * 2. 模拟浏览器通过http协议访问url，获取服务器返回的htm代码。如何访问？
    * 3. 解析html字符串(根据一定规则提取需要的数据)。如何解析？
## 五、 反爬手段
* 5.1 User-Agent
  * User-Agent，中文名为用户代理，简称UA，它是一个特殊字符串头，使服务器能够识别客户使用的操作系统及版本，CPU类型、浏览器及其版本、浏览器渲染引擎、llq语言、浏览器插件等。
* 5.2 代理IP：若有异于人类基本操作的行为，服务器方就会封IP。
  * 西次代理
  * 快代理
  * 什么是高匿名、匿名和透明代理？它们之间有何区别？
    * 1. 使用透明代理，对方服务器可以知道你使用了代理，并且也知道你的真实IP。
    * 2. 使用匿名代理，对方服务器可以知道你使用了代理，但不知道你的真实IP。
    * 3. 使用高匿名代理，对方服务器不知道你使用了代理，更不知道你的真实IP。
* 5.3 验证码访问，就是为了防止爬虫，但都不是事。
  * 打码平台
  * 云打码平台
  * 超级
* 5.4 动态加载网页，网站返回的是js数据，并不是网页的真实数据，但也都不是大问题。
  * selenium驱动真实的浏览器发送请求
* 5.5 数据加密
  * 分析js代码
## 六、 urllib库的使用
* urllib库，该库不需要安装，因为它是Python本身自带的，不像其他的库，需要去官网手动安装。
* 6.1 主要是学习如何使用urllib来模拟浏览器，来访问服务器的数据。在这里向百度发送请求，获取百度首页的源码，并从其中获取真正想要的数据
  * 首先导入urllib库下的request，
    * ```import urllib.request```
  * 其次，定义一个变量url，用于存放要访问的地址，在这里就是百度首页的地址
    * ```url='http://www.baidu.com'```
  * 再次，就可以向浏览器发送请求，发送请求的方法为urlopen方法，将要访问的地址作为参数传进去，即可向对应的服务器发送请求并接收服务器的反馈。
    * ```response=urllib.request.urlopen(url)```
    * ![urlopen方法，向服务器访问请求时调用的方法，将地址作为参数传进去即可](imgs/urlopen%E6%96%B9%E6%B3%95%EF%BC%8C%E5%90%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%AE%BF%E9%97%AE%E8%AF%B7%E6%B1%82%E6%97%B6%E8%B0%83%E7%94%A8%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%8C%E5%B0%86%E5%9C%B0%E5%9D%80%E4%BD%9C%E4%B8%BA%E5%8F%82%E6%95%B0%E4%BC%A0%E8%BF%9B%E5%8E%BB%E5%8D%B3%E5%8F%AF.png)
  * 再次，打印接收的数据response可以发现，是有响应头、响应体和响应行等的全部数据，但需要的只是相应当中的页面的源码，因此需要调用read方法来提取页面源码，再打印可以看到输出的是字节形式的二进制数据。
    * ![这个b代表，返回的是字节形式的二进制数据](imgs/%E8%BF%99%E4%B8%AAb%E4%BB%A3%E8%A1%A8%EF%BC%8C%E8%BF%94%E5%9B%9E%E7%9A%84%E6%98%AF%E5%AD%97%E8%8A%82%E5%BD%A2%E5%BC%8F%E7%9A%84%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%95%B0%E6%8D%AE.png)
  * 最后，因在下一步需要做的，就是将这些二进制数据转换为字符串类型的数据，这一步叫做解码，解码方法为decode()，参数位置传对应页面的编码格式，在这里就是utf-8，找编码格式的话，就是charset的值。最后打印时可以发现，打印出来的结果最前面没有**b'**了，也可以看见汉字了，就意味着解码成功。
    * ![调用decode方法并用utf-8的编码格式转换后，可以发现b没了，且可以看见汉字了，说明解码成功了](imgs/%E8%B0%83%E7%94%A8decode%E6%96%B9%E6%B3%95%E5%B9%B6%E7%94%A8utf-8%E7%9A%84%E7%BC%96%E7%A0%81%E6%A0%BC%E5%BC%8F%E8%BD%AC%E6%8D%A2%E5%90%8E%EF%BC%8C%E5%8F%AF%E4%BB%A5%E5%8F%91%E7%8E%B0b%E6%B2%A1%E4%BA%86%EF%BC%8C%E4%B8%94%E5%8F%AF%E4%BB%A5%E7%9C%8B%E8%A7%81%E6%B1%89%E5%AD%97%E4%BA%86%EF%BC%8C%E8%AF%B4%E6%98%8E%E8%A7%A3%E7%A0%81%E6%88%90%E5%8A%9F%E4%BA%86.png)
* 6.2 urllib的1个类型6个方法
  * 1个类型
    * 就是认识response的数据类型，是<class 'http.client.HTTPResponse'>，简单来说就是HTTPResponse类型的，不是之前学习的那些类型，因为它是向服务器请求返回的结果，所以接下来可以用6个方法来读取其中想要的数据。
  * 6个方法
    * read()，如上一部分所示，就是效率比较低，也可以向其中传递数字参数，就会读取并输出那几个字节。
      * ```
          content=response.read(5)
          print(content)      #b'<!DOC'
        ```
    * readline()，虽然会快很多，但调用readline方法只会读取一行，若需要读取全部数据时，还是不顶用。
    * readlines()，调用readlines方法快很多，是一行一行读取的，它是把全部的数据读取完为止，且返回的依旧是字节形式的数据。
      * ![readlines方法读取response就会快很多，前面有b，就是字节形式的数据](imgs/readlines%E6%96%B9%E6%B3%95%E8%AF%BB%E5%8F%96response%E5%B0%B1%E4%BC%9A%E5%BF%AB%E5%BE%88%E5%A4%9A%EF%BC%8C%E5%89%8D%E9%9D%A2%E6%9C%89b%EF%BC%8C%E5%B0%B1%E6%98%AF%E5%AD%97%E8%8A%82%E5%BD%A2%E5%BC%8F%E7%9A%84%E6%95%B0%E6%8D%AE.png)
    * getcode()，response调用getcode方法，会返回状态码，如果是200就意味着，请求和反馈都没问题，就是逻辑正常。
    * geturl()，response调用geturl方法，返回的是url地址，也就是发送了请求的服务器的地址。
    * getheaders()，返回一些状态信息，也就是得到的反馈中响应头的信息。
      * ![getheaders方法，返回的是服务器反馈的响应头的信息](imgs/getheaders%E6%96%B9%E6%B3%95%EF%BC%8C%E8%BF%94%E5%9B%9E%E7%9A%84%E6%98%AF%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%8F%8D%E9%A6%88%E7%9A%84%E5%93%8D%E5%BA%94%E5%A4%B4%E7%9A%84%E4%BF%A1%E6%81%AF.png)
* 6.3 下载
  * 如何将图片、音频、视频、网页等下载到本地？调用urllib.request的urlretrieve()，第一个参数传网页地址的变量名，第二个参数传下载到本地时的文件名。
    * ![urlretrive方法，用于下载网页、音视频和图片时调用](imgs/urlretrive%E6%96%B9%E6%B3%95%EF%BC%8C%E7%94%A8%E4%BA%8E%E4%B8%8B%E8%BD%BD%E7%BD%91%E9%A1%B5%E3%80%81%E9%9F%B3%E8%A7%86%E9%A2%91%E5%92%8C%E5%9B%BE%E7%89%87%E6%97%B6%E8%B0%83%E7%94%A8.png)
    * 网页
      * 依旧引入```import urllib.request```，虽然都是通过调用urlretrieve方法来实现，但根据需求的不同操作也有所不同。下载网页的话，首先声明存储网页地址的变量，随后调用```urllib.request.urlretrieve()```，方法内传递两个参数，第一个参数传递存储网页的那个变量名，第二个参数传递下载到本地之后的网页的文件名，运行后没有报错的话可以在文件夹中查看到已成功创建一个html文件。
    * 图片
      * 若是下载图片，如同上面的操作，记得传递第二个参数时，将文件名的后缀写成.jpg或.png等图片的后缀，否则就算运行成功打开所谓图片文件时，会让选择打开此文件的格式。有一个小提示就是，传递参数时，可以直接写url地址和filename的值，也可以以变量名=值的格式写，看个人习惯。
    * 视频
      * 若下载的是视频，记得别下载b站的，他们做了反爬，运行了会直接报412的错，视频的后缀用.mp4，向上面一样正常传递参数运行后，在pycharm点击视频文件的话会无法播放，因为pycharm没有播放器，直接去本地文件夹，找到刚刚下载好的视频文件双击即可查看。
## 七、 请求对象的定制
* UA介绍：User Agent中文名为用户代理，简称UA，它是一个特殊字符串头，使服务器能够识别客户使用的操作系统及其版本、CPU类型、浏览器及版本、浏览器内核、浏览器渲染引擎、浏览器语言、浏览器插件等。
* 语法：request=urllib.request.Request()
  * 这是通过UA进行的反爬，因为无法识别是否是真的浏览器，所以通过UA进行请求对象的定制，伪装成有请求头的样子。将UA拿到后声明一个名为headers的字典，将UA存进去，查看urlopen方法的底层代码可以看到urlopen方法不接收字典作为参数，urlopen方法只接收字符串和Request对象作为参数。所以需要请求对象的定制，需要调用request的Request方法来声明一个Request对象，并向其中传递服务器的url路径和字典headers作为参数即可。需要注意的是，传递参数时不能进行简化，这是因为Request方法的底层代码的缘故，源码中因为参数顺序的问题，因为url对象和headers对象中间还设置了data这个变量，所以需要关键字传参，也就是以变量名=值的格式传入即可。最后向urlopen方法中将Request对象作为参数传递进去，在想服务器发送请求并接收。
    * ```
        import urllib.request
        url='https://www.baidu.com'
        headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
        request=urllib.request.Request(url=url,headers=headers)
        response=urllib.request.urlopen(request)
        content=response.read().decode('utf8')
        print(content)
      ```
* 扩展：编码的由来
  * 编码集的演变
    * 最早只有127个字符被编码到早期计算机里，也就是大小写字母、数字和一些符号。这个编码表被称为ASCII编码，如A的编码是65，z的编码是122。处理中文时这些字节显然不够，且大部分中文需要两个字节，还不能和ASCII编码集有冲突。所以中国制定了GB2312编码，把中文编了进去。
    * 即便如此世界上有上百种语言，各国有各国的标准，不可避免地会产生冲突，结果就是多语言混合的文本中，就会出现乱码。因此Unicode出现并将所有语言统一到了一套编码中，这样就会不会再出现乱码的问题。现代操作系统和大多数编程语言都支持Unicode。
## 八、 编解码
* 8.1 get请求方式：urllib.parse.quote()
  * 百度任意搜一个人，搜出来的路径只有到wd的值是这个人的信息，后面的都是广告，因此可以先声明一个url变量，并将网址的一部分，也就是到wd为止的网址赋值给url。随后，若想将汉字字符转换为Unicode编码格式，就先引入urllib.parse，因为需要调用它下面的quote方法，quote方法中传递汉字字符作为参数，并用一个变量名name接收，然后将url和name进行拼接就可以得到完整的关于一个人的搜索地址。最后正常进行请求对象定制的操作即可。
  * 下面是因为网址路径当中不是Unicode编码导致的报错和Unicode编码时成功运行并输出的结果。
    * ![UnicodeEncodeError，获取的字符部分已超出设定的128个字符以外](imgs/UnicodeEncodeError%EF%BC%8C%E8%8E%B7%E5%8F%96%E7%9A%84%E5%AD%97%E7%AC%A6%E9%83%A8%E5%88%86%E5%B7%B2%E8%B6%85%E5%87%BA%E8%AE%BE%E5%AE%9A%E7%9A%84128%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%BB%A5%E5%A4%96.png)
    * ![将人名转换为Unicode形式后，运行结果](imgs/%E5%B0%86%E4%BA%BA%E5%90%8D%E8%BD%AC%E6%8D%A2%E4%B8%BAUnicode%E5%BD%A2%E5%BC%8F%E5%90%8E%EF%BC%8C%E8%BF%90%E8%A1%8C%E7%BB%93%E6%9E%9C.png)
  * 这是调用urllib.parse下的quote方法后，将路径和Unicode编码格式的人名拼接之后，进行请求对象定制操作的结果
    * ![urllib.parse的quote方法，用于将汉字字符转换为通用的Unicode格式](imgs/urllib.parse%E7%9A%84quote%E6%96%B9%E6%B3%95%EF%BC%8C%E7%94%A8%E4%BA%8E%E5%B0%86%E6%B1%89%E5%AD%97%E5%AD%97%E7%AC%A6%E8%BD%AC%E6%8D%A2%E4%B8%BA%E9%80%9A%E7%94%A8%E7%9A%84Unicode%E6%A0%BC%E5%BC%8F.png)
* 8.2 get请求方式：urllib.parse.urlencode()
  * urlencode方法用于处理多个参数的情况，若给一个网址添加其他信息时，可以事先将这些信息统一存储到字典中，并需要先声明一个基础路径baseUrl。其次，调用urllib.parse下的urlencode方法，将整合为字典的数据作为参数传递进去，就可以得到转换为Unicode格式的数据，用一个变量接收。随后，就可以将基础路径和转换为Unicode格式的数据进行拼接，这就是完整的请求资源的路径。再次做好UA反爬，再然后照常进行请求对象定制的操作，并打印输出。
  * ```
      import urllib.request
      import urllib.parse
      baseUrl='https://www.baidu.com/s?'
      data={
          'wd':'谷江山',
          'gender':'男',
          'job':'配音演员',
          'location':'北京'
      }
      newData=urllib.parse.urlencode(data)
      lastUrl=baseUrl+newData
      headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
      request=urllib.request.Request(url=lastUrl,headers=headers)
      response=urllib.request.urlopen(request)
      content=response.read().decode('utf-8')
    ```
* 8.3 post请求方式
  * 以网页版百度翻译为例，右键点击检查->网络后，在左侧写上需要翻译的单词(这里以spider举例)，可以说就像再加载了一遍网页一样，会有好多向服务器发送各种请求后，请求成功并返回的结果，比如名为sug的就是post请求得来的。在sug的preview中，可以查看到具体的数据data，其中我需要的是key值为kw的数据，将它存储到名为data的字典中。然后就正常声明请求地址，这次的请求地址可以在sug的请求头中找到。再用UA反爬，再调用urlencode方法传入data做参数进行编码，这次因为是post请求，所以需要对urlencode方法进行编码的数据进行进一步的编码，调用encode方法，参数传utf-8即可。继续根据流程进行请求对象定制的操作，只不过这一步骤需要多添加一个小部分。Request方法的源码中第二个参数名叫data，之前发送get请求时，只用了url和headers参数，但post请求中需要用到data参数，因此这次请求对象定制的操作，需要传递url、data和headers这三个参数。随后正常进行下一步模拟浏览器向服务器发送请求，再将得到的反馈，用read方法和decode方法进行提取和解码操作。
  * ```
      # post请求，post的参数在请求体中
      import urllib.request
      import urllib.parse
      url='https://fanyi.baidu.com/sug'
      headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
      data={
          # 在sug的preview中可以查看到
          'kw':'spider'
      }
      newData=urllib.parse.urlencode(data).encode('utf-8')
      # post请求的参数，是不会拼接在url的后面的，而是需要放在请求对象定制的参数中
      request=urllib.request.Request(url=url,data=newData,headers=headers)
      response=urllib.request.urlopen(request)
      content=response.read().decode('utf-8')
      print(content)
    ```
  * post请求中需要注意的就是，post请求的参数不会拼接在url的后面，所以需要放在请求对象定制的参数当中，```request=urllib.request.Request(url=url,data=newData,headers=headers)```
  * 并且还有一个特别需要注意的部分就是，post请求方式的参数，必须进行两次编码，urlencode和encode，```newData=urllib.parse.urlencode(data).encode('utf-8')```
  * ![post请求方式](imgs/post%E8%AF%B7%E6%B1%82%E6%96%B9%E5%BC%8F.png)
## 九、 ajax的get请求
* get请求的话，就知道引入```import urllib.request```即可，照常从豆瓣电影-动作片-检查中获取请求路径，UA反爬，请求对象定制，并调用urlopen方法来，像服务器发送请求并获取数据，将获取到的数据调用read方法和decode方法进行解码。
* 需求是获取豆瓣电影动作片第一页的数据，并保存到本地。所以根据在Python基础部分学过的，调用open方法创建名为douban.json的文件，访问文件的模式为w，随后调用file变量的write方法，参数位传入content数据即可，只不过这次需要格外注意的一点是，open方法默认情况下使用的是gbk编码，若想要保存为汉字的格式，就需要在open方法传递第三个参数就是encoding='utf-8'，这样在打开文件时，才不会报错，不写报的错截图放下面。
* 若以传统的方式也就是调用open方法后，再调用write方法的话，最后还需要手动调用close方法来关闭文件。为了图方便也可以这么写。这么写，一是不用再调用close方法来关闭文件，二是真的很方便：
  * ```
      with open('douban1.json','w',encoding='utf-8') as file:
          file.write(content)
    ```
  * ![没有传入encoding='utf-8'的结果](imgs/%E6%B2%A1%E6%9C%89%E4%BC%A0%E5%85%A5encoding%3D%27utf-8%27%E7%9A%84%E7%BB%93%E6%9E%9C.png)
* 案例：向豆瓣电影的官网发送get请求，获取前十页的数据，并下载到本地
  * 查看请求地址可以了解到，区别只在于最后一部分的start的部分，且因为要获取的数据需要从不同的路径获取，所以不能单纯地实现一次请求对象定制，也不能反复地向网站发送请求，会被封号。因此在正式请求对象定制前，需要创建一个函数createRequest，在这个函数内做好请求对象定制前的全部准备工作。查看地址规律后可发现，请求路径的前部分重复性很高，所以声明baseUrl，用于存储请求路径的前部分，另外又声明data字典，存储start和limit数据，start的规律是```(page-1)*20```，limit的值固定为20。调用urlencode方法，将data数据转换为Unicode格式的新数据newData，并将baseUrl和newData进行拼接，就是一条一条的请求地址。在下面声明startPage和endPage两个变量，用于在控制台输入页码，并创建一个for循环，for循环中调用createRequest函数，并传递遍历的page作为参数。下面的图片是获取的前六页请求地址。
    * ![向豆瓣电影发送get请求，获取前六页的获取路径](imgs/%E5%90%91%E8%B1%86%E7%93%A3%E7%94%B5%E5%BD%B1%E5%8F%91%E9%80%81get%E8%AF%B7%E6%B1%82%EF%BC%8C%E8%8E%B7%E5%8F%96%E5%89%8D%E5%85%AD%E9%A1%B5%E7%9A%84%E6%95%B0%E6%8D%AE.png)
  * 上面属于请求定制前的准备工作，
## 十、 ajax的post请求
## 十一、 复杂get
## 十二、 URLError\HTTPError
## 十三、 cookie登录
## 十四、 Handler处理器
## 十五、 代理服务器
## 十六、 cookie库
