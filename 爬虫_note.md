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
  * 上面属于请求定制前的准备工作，在createRequest的最后，正式请求对象定制，并将request返回，以便于在下一个函数中作为参数传递并使用。
  * 创建getContent函数，接收上一个函数返回的request为参数，另起名为acceptRequest，在该函数中获取网页源码，并将其调用decode方法进行解码，最后再将解码的结果返回，以便于在下一个下载数据的函数中使用。
  * 创建downloadFilm函数，接受page和创建getContent函数中返回的acceptContent作为参数，调用open方法和write方法创建新文件，并将数据写入进去，需要注意的是open方法中必须有encoding='utf-8'，这样才能没有报错和乱码。
## 十、 ajax的post请求
* 案例：向KFC官网发送post请求，获取北京市门店地址前十页的数据，并下载到本地
  * 点击每一页后查看请求地址可以理解到，不同于上面的案例，这次的请求地址没有不同，就是那一个请求地址，因此省去了计算请求地址的步骤。但既然是post请求就会有所区别于get请求的步骤，就是将data编码为Unicode格式的步骤。首先，创建一个if判断，在其中声明会输入的起始页码和结束页码的两个变量startPage和endPage。其次，用for循环将输入的startPages和endPage进行遍历，在循环外创建一个叫createRequest的函数，并在循环中调用时，将遍历startPage和endPage的page作为参数。在createRequest函数中做好请求对象定制前的准备工作和请求对象定制的操作，data是payload中的form data，请求对象定制后用return，将request返回，以便于在下一个函数中使用。
  * 创建getContent函数，并接收上一个createRequest函数中返回的request，另起变量名为returnRequest为参数，在getContent函数中获取网页源码，并调用decode方法将获取的反馈数据解码，再一次返回其值，也就是content。最后创建downloadData函数，接收page和上一个函数中返回的content，另起名为returnContent作为参数，用```with open('filename'+str(page)+'.json','w',encoding='utf-8') as file:file.write(content)```的方式，创建文件并将获取的数据写入进去。
## 十一、 URLError\HTTPError
* 简介：
  * 1. 因为url里包含http，HTTPError类是URLError类的子类。协议：主机：端口：请求路径s：请求参数：锚点。
  * 2. 导入的包urllib.error.HTTPError urllib.error.URlError。
  * 3. http错误：http错误是针对浏览器无法连接到服务器二增加出来的错误提示，引导并告诉浏览者该页是哪里出现了问题。
  * 4. 通过urllib发送请求的时候，有可能会发送失败(有可能是服务器宕了，也有可能是地址写错了)这时如果想让代码更加的流畅稳定(老师说是健壮)，可以通过try-except进行捕获异常，异常有两类，URLError\HTTPError。通过try-except捕获异常时，需要引入```import urllib.error```，再在使用except部分时，写明到底是何种错误。
  * 下面两张图展示的就是HTTPError和URLError错误的案例展示：
    * ![url地址错误导致的HTTPError](imgs/url%E5%9C%B0%E5%9D%80%E9%94%99%E8%AF%AF%E5%AF%BC%E8%87%B4%E7%9A%84HTTPError.png)
    * ![url的主机部分错误导致的URLError](imgs/url%E7%9A%84%E4%B8%BB%E6%9C%BA%E9%83%A8%E5%88%86%E9%94%99%E8%AF%AF%E5%AF%BC%E8%87%B4%E7%9A%84URLError.png)
## 十二、 cookie登录
* 适用场景为在进行数据采集时，需要绕过登录，进入到某个指定的页面。当像平常一样进行请求对象定制，模拟浏览器向服务器发送请求，并获取数据后，调用open方法将数据下载到本地的操作后，运行代码会出现UnicodeDecodeError的错误，那是因为并未进入到个人信息页面，而是跳转到了登录页面，但登录页面又不是utf-8，所以才会报那样的错。这是微博的反爬手段。因为不能写成utf-8，在调用decode方法解码时，输入gb312为解法格式，就会正常运行并可以创建文件，把获取的数据写入到新建的文件中。
  * ![下载到本地的数据右键检查后查看到的是gb2312](imgs/%E4%B8%8B%E8%BD%BD%E5%88%B0%E6%9C%AC%E5%9C%B0%E7%9A%84%E6%95%B0%E6%8D%AE%E5%8F%B3%E9%94%AE%E6%A3%80%E6%9F%A5%E5%90%8E%E6%9F%A5%E7%9C%8B%E5%88%B0%E7%9A%84%E6%98%AFgb2312.png)
* 需要做到的就是无论是否登录，又或者在其他浏览器查看，通过cookie绕过登录这个步骤，都可以直接进入并访问某个指定的页面。登录微博后，右键检查，可以在request headers中看到诸多信息，其中需要的就是cookie，将cookie与其值复制粘贴到headers对象当中，顺便把下面调用decode解码格式换回utf-8，就可以不用通过登录步骤也可以进入指定页面中了，但我是成了40%，微成功。request headers中还有一对是referer与其值，它在一般情况下是做图片防盗链的，简单来说就是，若不是通过referer的地址登录的来的，就不允许访客下载图片。
  * ![成功但没完全成功的展示，微成功](imgs/%E6%88%90%E5%8A%9F%E4%BD%86%E6%B2%A1%E5%AE%8C%E5%85%A8%E6%88%90%E5%8A%9F%E7%9A%84%E5%B1%95%E7%A4%BA%EF%BC%8C%E5%BE%AE%E6%88%90%E5%8A%9F.png)
## 十三、 Handler处理器
* 为什么学习handler？
  * urllib.request.open(url)，不能定制请求头
  * urllib.request.Request(url=url,headers=headers,data=data)，可以定制请求头
  * Handler，可以定制更高级的请求头，随着业务逻辑更加复杂，请求对象的定制已经无法满足需求，动态的cookie和代理不能使用请求对象的定制。
  * 若是太高频次地访问一个IP，后台会判断为是在爬虫，会将访问的账号封禁掉，可以使用代理来访问，就需要handler处理器。
  * 需求：使用handler来访问百度，来获取网页源码，具体步骤如下：
    * 前半部分的准备工作到请求对象定制为止都一样，想要使用handler处理器需要添加三步。首先调用urllib.request的HTTPHandler方法获取handler对象；其次调用urllib.request的build_opener方法，将handler作为参数传进去，通过handler获取opener对象，最后就是调用opener的open方法，将request作为参数传进去，这一步就是模拟浏览器向服务器发送请求，返回值依旧用response接收，下面就是正常解码即可。
## 十四、 代理服务器，简单来说代理就是用别人的ip访问网站
* 14.1 代理的常用功能
  * 1. 突破自身IP访问限制，访问国外站点。
  * 2. 访问一些单位或团体内部资源，例如，校园内部或企事业单位内部是理论上只有内部员工或本校学生才可以访问的，但并不代表外部的人就没有机会，外部人员可以通过代理查询各类资料并共享。
  * 3. 提高访问速度。扩展：通常代理服务器都设置一个较大的硬盘缓冲区，当有外界的信息通过时，同时也将其保存到缓存区中，当其他用户再访问相同的信息时，则直接在缓冲区中取出信息，传给用户，以提高访问速度。
  * 4. 隐藏真实IP。扩展：上网者可以通过这种方法隐藏自己的IP，免受攻击。
* 14.2 代码配置代理
  * 创建Request对象
  * 创建ProxyHandler对象
    * 前期准备工作到请求对象定制都一样，到创建handler对象时，又跟上面的handler处理器有一点不同，这次调用urllib.request的ProxyHandler方法，当查看ProxyHandler方法的源码可以看到，调用该方法需要传递proxies参数，这个参数就是代理IP，需要提前以字典类型声明。再调用urllib.request的build_opener方法创建opener对象，传递handler为参数，再然后调用opener的opener对象，模拟浏览器向服务器发送请求，最后解码即可。
    * 但这个代理IP如果找免费的，成功概率很低，想要成功可以花钱生成一个成功率高的。下面是免费IP的响应失败报错，但没啥关系，使用了代理IP就可以有效避免被追踪，这个有效IP不好使了换一个用就行。在打开创建的html文件就可以看到真实IP会被代理IP取代的结果。
      * ![免费的代理IP会出现不响应的情况](imgs/%E5%85%8D%E8%B4%B9%E7%9A%84%E4%BB%A3%E7%90%86IP%E4%BC%9A%E5%87%BA%E7%8E%B0%E4%B8%8D%E5%93%8D%E5%BA%94%E7%9A%84%E6%83%85%E5%86%B5.png)
  * 用handler对象创建opener对象(这就是上面刚学的Handler处理器)
  * 使用opener.open函数发送请求(也是上面刚学的代替urlopen方法，模拟浏览器向服务器发送请求的步骤)
## 十五、 cookie库

## 十六、 解析
* 16.1 XPath
  * 安装XPath扩展程序，在chrome应用商店里找，安装了XPath Tester，快捷键Ctrl+shift+x后出现小白框就是安装成功了
  * 1. 安装lxml库，pip install lxml，这是国外版，但在国内的话可能会慢一些，就可以下载国内版https://pypi.douban.com/simple，在安装python的文件夹的script文件夹里可以看到，若没有就在pycharm的设置-python interpreter-加号中搜lxml，安装即可。在python interpreter中看见lxml就可以了。
    * ![找到正确的路径安装lxml，可安装国外版，若在国内嫌国外版下载慢的话也可安装国内版](imgs/%E6%89%BE%E5%88%B0%E6%AD%A3%E7%A1%AE%E7%9A%84%E8%B7%AF%E5%BE%84%E5%AE%89%E8%A3%85lxml%EF%BC%8C%E5%8F%AF%E5%AE%89%E8%A3%85%E5%9B%BD%E5%A4%96%E7%89%88%EF%BC%8C%E8%8B%A5%E5%9C%A8%E5%9B%BD%E5%86%85%E5%AB%8C%E5%9B%BD%E5%A4%96%E7%89%88%E4%B8%8B%E8%BD%BD%E6%85%A2%E7%9A%84%E8%AF%9D%E4%B9%9F%E5%8F%AF%E5%AE%89%E8%A3%85%E5%9B%BD%E5%86%85%E7%89%88.png)
    * ![在终端安装失败的话，可以在设置Python interpreter，+中安装](imgs/%E5%9C%A8%E7%BB%88%E7%AB%AF%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5%E7%9A%84%E8%AF%9D%EF%BC%8C%E5%8F%AF%E4%BB%A5%E5%9C%A8%E8%AE%BE%E7%BD%AEPython%20interpreter%EF%BC%8C%2B%E4%B8%AD%E5%AE%89%E8%A3%85.png)
  * 2. 导入lxml.etree
    * ```from lxml import etree```
  * 3. etree.parse('xxx.html')，解析本地文件
  * 4. etree.HTML(response.read().decode('utf-8'))，解析服务器响应的文件
  * 5. html_etree.xpath(xpath路径)
  * xpath基本语法
    * 1. 路径查询
      * //：查找所有子孙节点，不考虑层级关系，```liList=tree.xpath('//body//li')```
      * /：找直接子节点,```liList=tree.xpath('//body/ul/li')```
    * 2. 谓词查询
       * //div[@id]，过滤出带有id属性的标签，也可以查询id属性标签的文本内容
         * ```liWithId=tree.xpath('//ul/li[@id]')```
         * ```liWithContent=tree.xpath('//ul/li[@id]/text()')```
      * //div[@id="miancontent"]，过滤出带有id属性且该id属性还有专属值的标签
        * ```liWithIdAndContent=tree.xpath('//ul/li[@id="l1"]/text()')```
    * 3. 属性查询
      * //@class，过滤出带有class属性的标签，并获取class属性的值
        * ```liWithIdAndClassValue=tree.xpath('//ul/li[@id="l1"]/@class')```
    * 4. 模糊查询
      * //div[contains(@id,"he")]，需求：找出id属性值包含l的li标签
        * ```liWithL=tree.xpath('//ul/li[contains(@id,"l")]/text()')```
      * //div[starts-with(@id),"he"]，需求：找出id属性值为c开头的里标签
        * ```liStartWithL=tree.xpath('//ul/li[starts-with(@id,"c")]/text()')```
    * 5. 内容查询
      * //div/h1/text()，想要获取某一标签的文本内容，就在最后添加/text()即可。
    * 6. 逻辑运算
      * //div[@id="head" and @class="s_down"]，但不常用，两个过滤条件的话，把第二个过滤条件写后面就行。
      * //title | //price，没必要。
  * 案例：获取百度首页的百度一下文本内容
    * 不同于上面的解析本地文件，案例是解析服务器响应的文件，因此首先需要获取网页源码，步骤依旧是熟悉的请求对象定制，模拟浏览器向服务器发送请求，并进行解码来获取网页源码。正式进入解析网页源码的步骤：
    * 引入```from lxml import etree```，声明变量tree，接收etree的HTML方法的返回值，HTML方法是专门在解析网页源码时调用的，HTML方法内传入解析的源码content做参数。下一步就能获取想要的数据，也就是百度一下文本内容：
    * 先到chrome，用快捷键(Ctrl+Shift+X)激活XPath Tester，在左侧用属性查询的方式找到id值为su的有value属性的input标签，右侧就会显示对应的文本内容，查看是否正确，若正确，就把xpath路径复制下来，调用tree的xpath方法，将xpath路径传递进去即可得到百度一下文本内容。xpath路径：```//input[@id="su"]/@value```
      * ![用快捷键激活XPath Tester，检查里找到百度一下所在的标签，过滤出id值为su和有value属性的指定input标签的文本内容](imgs/%E7%94%A8%E5%BF%AB%E6%8D%B7%E9%94%AE%E6%BF%80%E6%B4%BBXPath%20Tester%EF%BC%8C%E6%A3%80%E6%9F%A5%E9%87%8C%E6%89%BE%E5%88%B0%E7%99%BE%E5%BA%A6%E4%B8%80%E4%B8%8B%E6%89%80%E5%9C%A8%E7%9A%84%E6%A0%87%E7%AD%BE%EF%BC%8C%E8%BF%87%E6%BB%A4%E5%87%BAid%E5%80%BC%E4%B8%BAsu%E5%92%8C%E6%9C%89value%E5%B1%9E%E6%80%A7%E7%9A%84%E6%8C%87%E5%AE%9Ainput%E6%A0%87%E7%AD%BE%E7%9A%84%E6%96%87%E6%9C%AC%E5%86%85%E5%AE%B9.png)
  * 案例：站长素材网站中获取小猫图片的前十页，并下载到本地
    * if main判断中声明startPage和endPages两个变量，并使用for循环对其之间的步长进行遍历，循环体中，调用createRequest函数，传入遍历的结果page作为参数，在for循环体外声明createRequest函数。观察站长素材小猫图片的每一页网址后可以发现第二页开始路径的变化是在请求路径的最后有了_page，因此createRequest中用if-else做个判断，若page值等于1，请求路径url的值就是第一页的值；否则，url的值就是https://sc.chinaz.com/tupian/xiaomaotupian_加上强制转换为字符串类型的page，最后不上.html。UA反爬后，进行请求对象定制的操作，函数体内的最后将获取的request返回，以便于在下面的获取源码的函数中使用。
    * 返回的request，在for循环中用变量returnRequest接收，创建获取源码的getContent函数，将returnRequest作为参数传进去，for循环体外照样声明getContent函数，getContent函数体内模拟浏览器向服务器发送请求，随后进行解码操作，获取到源码后将得到的content返回，以便于在下载图片的函数中使用。
    * 返回的content，在for循环体中用returnContent变量接收，创建下载图片的函数downloadPng，接收returnContent为参数。downloadPng函数体内，首先要做的就是调用etree的HTML方法创建tree对象，HTML方法中将returnContent传进去解析。点开小猫所在网页用快捷键激活xpath，一层一层找出包裹图片的标签，将他们一一列出来，再在右侧查看是否正确，若正确就将xpath路径粘贴到xpath方法里面做参数，就可以得到图片列表，用变量picList接收。用for循环遍历piclist的长度，变量设置为i，在循环体内将picList[i]赋值给pictures。下载图片到本地调用的是urlretrieve方法，方法内第一个参数时图片地址，第二个参数是存储图片的文件名或文件夹名，最后点击运行即可。
    * 但是我失败了，可能是访问了太多次网站被反爬了，又或者是逻辑错误，但询问了deepseek说是基本逻辑无误。
* 16.2 JsonPath
  * JsonPath的安装：打开终端，在下载Python的目录下，用```pip install jsonpath```即可。
    * ![安装jsonpath](imgs/%E5%AE%89%E8%A3%85jsonpath.png)
  * JsonPath的用法：jsonpath只解析本地文件，引入json和jsonpath后，将json文件中的数据反序列化，将json类型的数据转换为Python的dic类型。调用json的load方法，load方法中再调用open方法，open方法中奖json文件，按照r模式打开，并设置encoding='utf-8，```loadedObj=json.load(open('71-Python_解析_jsonpath.json','r',encoding='utf-8'))```。
  * 且与xpath不同，获取jsonpath路径的方式与xpath大有不同，比如不用/来分隔上下级，也不用//来分隔上一级和子孙阶级，用$代替//，用.来代替/。筛选元素时，会调用jsonpath的jsonpath方法，将反序列化数据和jsonpath路径作为参数传进去。下面是几个不同的jsonpath路径案例。
  * $.store.book[*].author，过滤出所有书的作者。[]里的*代表当前节点下的全部。若[]内传递数值，就代表可以通过下标来获取指定对象的属性值
    * authorList=jsonpath.jsonpath(loadedObj,'$.store.book[*].author')  #['竹已', '匪我思存', '梁实秋', '曹雪芹']
    * authorList=jsonpath.jsonpath(loadedObj,'$.store.book[3].author')  #['曹雪芹']
  * $..author，所有的作者。..代表xpath里的//，代表查找所有子孙节点，在该案例里代表获取并整合根元素下下级中的所有author属性的值。
    * allAuthors=jsonpath.jsonpath(loadedObj,'$..author')  #['竹已', '匪我思存', '梁实秋', '曹雪芹', '关心则乱']
  * $.store.*，获取json中store下所有的元素。有了*就代表获取节点下全部元素
    * storeList=jsonpath.jsonpath(loadedObj,'$.store.*')
  * $.store..price，获取json中store下所有物品的price的值。
    * priceList=jsonpath.jsonpath(loadedObj,'$.store..price') ##[8.95, 12.99, 8.99, 22.99, 19.95]
  * $..book[2]或$.store.book[2]，获取json中book数组中第三本书。两种写法，可以一步一步写下来，也可以用..代替，这里为了明确第三本书的书名，最后有加了.title.
    * thirdBook=jsonpath.jsonpath(loadedObj,'$..book[2].title') #['快乐就是哈哈哈哈哈']
    * thirdBook=jsonpath.jsonpath(loadedObj,'$.store.book[2].title')  #['快乐就是哈哈哈哈哈']
  * $.store.book[(@.length-1)]，获取json中最后一本书。用@表示当前节点，在这里表示book节点下，根据条件进行过滤，()内，用长度-1的方式计算下标。
    * lastBook=jsonpath.jsonpath(loadedObj,'$.store.book[(@.length-1)]') #[{'category': '现实主义文学', 'author': '曹雪芹', 'title': '红楼梦', 'isbn': '9787101086591', 'price': 22.99}]
  * $..book[0,1]或$..book[:2]，获取json中book数组中的前两本书。也有两种方法，用下标来明确，或用切片的方式。
    * firstTwobook=jsonpath.jsonpath(loadedObj,'$..book[0,1].title')  #['难哄', '东宫']
    * firstTwobook=jsonpath.jsonpath(loadedObj,'$..book[:2].title')  #['难哄', '东宫']
  * $..book[?(@.isbn)]，获取json中的book数组中包含isbn属性的所有值。条件过滤需要在()的前面加一个?，?的作用是引入一个过滤表达式（filter expression），用于筛选符合条件的节点。
    * bookContainsISBN=jsonpath.jsonpath(loadedObj,'$..book[?(@.isbn)].title')  #['快乐就是哈哈哈哈哈', '红楼梦']
  * $..book[?(@.price>10)]，获取json中的book数组中price大于10的书。
    * bookList=jsonpath.jsonpath(loadedObj,'$..book[?(@.price>10)].title') #['东宫', '红楼梦']
  * 案例：jsonpath解析淘票票
    * 需求：向淘票票获取全国影院城市。
    * 鉴于jsonpath只能解析本地文件，因此通过请求对象定制获取源码后，需要创建一个新文件来存储源码，将其转为本地文件，就此可以通过jsonpath来解析并输出。需要注意的是，在进行反爬时，将请求标头的全部放到headers里，但带冒号的和accept-encoding请求头不要，因为它们几个不但不起作用，放着还报错。随后正常进行请求对象定制，模拟浏览器向服务器发送请求并获取源码的操作。打印数据后可以看到，数据不是json类型的数据，而是用jsonp函数包裹的数据，因此调用split方法，第一次以(进行分割，并取下标为1部分的数据，也就是真正的json数据部分，第二次用)进行分割，取下标为0部分的数据，去掉最后的;，才获取到真正需要的json数据。
      * ![反爬手段中前几个从请求标头拿来的带冒号的会导致报错，因此会删除掉](imgs/%E5%8F%8D%E7%88%AC%E6%89%8B%E6%AE%B5%E4%B8%AD%E5%89%8D%E5%87%A0%E4%B8%AA%E4%BB%8E%E8%AF%B7%E6%B1%82%E6%A0%87%E5%A4%B4%E6%8B%BF%E6%9D%A5%E7%9A%84%E5%B8%A6%E5%86%92%E5%8F%B7%E7%9A%84%E4%BC%9A%E5%AF%BC%E8%87%B4%E6%8A%A5%E9%94%99%EF%BC%8C%E5%9B%A0%E6%AD%A4%E4%BC%9A%E5%88%A0%E9%99%A4%E6%8E%89.png)
      * ![accept-encoding请求头及其值需要被注释掉，和上面带冒号的一样，不但没作用放着还报错，没了就可正常运行](imgs/accept-encoding%E8%AF%B7%E6%B1%82%E5%A4%B4%E5%8F%8A%E5%85%B6%E5%80%BC%E9%9C%80%E8%A6%81%E8%A2%AB%E6%B3%A8%E9%87%8A%E6%8E%89%EF%BC%8C%E5%92%8C%E4%B8%8A%E9%9D%A2%E5%B8%A6%E5%86%92%E5%8F%B7%E7%9A%84%E4%B8%80%E6%A0%B7%EF%BC%8C%E4%B8%8D%E4%BD%86%E6%B2%A1%E4%BD%9C%E7%94%A8%E6%94%BE%E7%9D%80%E8%BF%98%E6%8A%A5%E9%94%99%EF%BC%8C%E6%B2%A1%E4%BA%86%E5%B0%B1%E5%8F%AF%E6%AD%A3%E5%B8%B8%E8%BF%90%E8%A1%8C.png)
      * ![调用split方法将源码数据进行两次分割，以便于提取可解析的json数据](imgs/%E8%B0%83%E7%94%A8split%E6%96%B9%E6%B3%95%E5%B0%86%E6%BA%90%E7%A0%81%E6%95%B0%E6%8D%AE%E8%BF%9B%E8%A1%8C%E4%B8%A4%E6%AC%A1%E5%88%86%E5%89%B2%EF%BC%8C%E4%BB%A5%E4%BE%BF%E4%BA%8E%E6%8F%90%E5%8F%96%E5%8F%AF%E8%A7%A3%E6%9E%90%E7%9A%84json%E6%95%B0%E6%8D%AE.png)
    * 到此，数据依旧是服务器响应的数据，不是本地数据，创建新文件72-Python_解析_jsonpath解析淘票票.json，并将数据下载到文件中。既然作为本地文件就可以通过jsonpath来获取想要的数据了。引入json和jsonpath后，调用json的load方法，进行反序列化，load方法中调用open方法来打开刚创建的json文件，声明一个变量loadedObj，反序列化后的数据存储在其中。随后就可以调用jsonpath的jsonpath方法，将loadedObj和jsonpath路径传进去，就可以获取全部城市名。
* 16.3 BeautifulSoup
  * 1. 基本简介
    * BeautifulSoup简称：bs4
    * 什么是BeautifulSoup？
      * BeautifulSoup和lxml一样，是一个HTML、解析器，主要功能也是解析和提取数据。
    * 优缺点：
      * 缺点：效率没有lxml高
      * 优点；接口设计人性化，使用方便
  * 2. 安装以及创建
    * 安装：pip install bs4
      * ![依旧安装在Scripts里，但会在lib下的site-packages中，反正是安装成功了](imgs/%E4%BE%9D%E6%97%A7%E5%AE%89%E8%A3%85%E5%9C%A8Scripts%E9%87%8C%EF%BC%8C%E4%BD%86%E4%BC%9A%E5%9C%A8lib%E4%B8%8B%E7%9A%84site-packages%E4%B8%AD%EF%BC%8C%E5%8F%8D%E6%AD%A3%E6%98%AF%E5%AE%89%E8%A3%85%E6%88%90%E5%8A%9F%E4%BA%86.png)
    * 导入：from bs4 import BeautifulSoup，与xpath的导入方式一样。
    * 创建对象，与xpath使用方式很相似：
      * 服务器响应的文件生成对象
        * ```soup=BeautifulSoup(response.read().decode('utf-8'),'lxml')```
      * 本地文件生成对象
        * ```soup=BeautifulSoup(open('1.html'),'lxml')```
        * 因为以上面的方法生成对象后，默认打开文件的方式是gbk，所以会报错，因此需要给open方法传入第二个参数也就是encoding，其值为utf-8，以这种方式来指定编码格式。
          * ![直接打开文件后，不设置编码格式的结果，默认是gbk模式，因此需要将编码格式手动设置为utf-8](imgs/%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%E6%96%87%E4%BB%B6%E5%90%8E%EF%BC%8C%E4%B8%8D%E8%AE%BE%E7%BD%AE%E7%BC%96%E7%A0%81%E6%A0%BC%E5%BC%8F%E7%9A%84%E7%BB%93%E6%9E%9C%EF%BC%8C%E9%BB%98%E8%AE%A4%E6%98%AFgbk%E6%A8%A1%E5%BC%8F%EF%BC%8C%E5%9B%A0%E6%AD%A4%E9%9C%80%E8%A6%81%E5%B0%86%E7%BC%96%E7%A0%81%E6%A0%BC%E5%BC%8F%E6%89%8B%E5%8A%A8%E8%AE%BE%E7%BD%AE%E4%B8%BAutf-8.png)
  * 3. 节点定位
    * 根据标签名查找节点
      * soup.a
        * ![按照标签名找节点，会找出并输出第一个符合条件的数据](imgs/%E6%8C%89%E7%85%A7%E6%A0%87%E7%AD%BE%E5%90%8D%E6%89%BE%E8%8A%82%E7%82%B9%EF%BC%8C%E4%BC%9A%E6%89%BE%E5%87%BA%E5%B9%B6%E8%BE%93%E5%87%BA%E7%AC%AC%E4%B8%80%E4%B8%AA%E7%AC%A6%E5%90%88%E6%9D%A1%E4%BB%B6%E7%9A%84%E6%95%B0%E6%8D%AE.png)
      * soup.a.attrs
        * ![soup.a.attrs，可以查找符合条件的标签的所有属性](imgs/soup.a.attrs%EF%BC%8C%E5%8F%AF%E4%BB%A5%E6%9F%A5%E6%89%BE%E7%AC%A6%E5%90%88%E6%9D%A1%E4%BB%B6%E7%9A%84%E6%A0%87%E7%AD%BE%E7%9A%84%E6%89%80%E6%9C%89%E5%B1%9E%E6%80%A7.png)
    * 函数，这三个函数不是单独使用的，实际使用时，都会用到，会组合使用
      * find()：
        * soup.find('a')，只找第一个a标签
        * soup.find('a',属性值="属性值")：只找存在指定属性和属性值的a标签
        * soup.find('a',class_="值")：只找class属性为其值的a标签，class要写成class_
          * ![class被Python征用了，所以不能直接写class来找标签，需要写成class_，就代表通过class属性找指定的标签](imgs/class%E8%A2%ABPython%E5%BE%81%E7%94%A8%E4%BA%86%EF%BC%8C%E6%89%80%E4%BB%A5%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E5%86%99class%E6%9D%A5%E6%89%BE%E6%A0%87%E7%AD%BE%EF%BC%8C%E9%9C%80%E8%A6%81%E5%86%99%E6%88%90class_%EF%BC%8C%E5%B0%B1%E4%BB%A3%E8%A1%A8%E9%80%9A%E8%BF%87class%E5%B1%9E%E6%80%A7%E6%89%BE%E6%8C%87%E5%AE%9A%E7%9A%84%E6%A0%87%E7%AD%BE.png)
      * find_all()：
        * soup.find_all('a')：查找所有a标签
        * soup.find_all('a','span')：查找所有a和span标签
        * soup.find_all('li',limit=2)：返回前两个li标签
          * ![find_all函数，传递第二个参数limit，可以获取前几个指定的数据](imgs/find_all%E5%87%BD%E6%95%B0%EF%BC%8C%E4%BC%A0%E9%80%92%E7%AC%AC%E4%BA%8C%E4%B8%AA%E5%8F%82%E6%95%B0limit%EF%BC%8C%E5%8F%AF%E4%BB%A5%E8%8E%B7%E5%8F%96%E5%89%8D%E5%87%A0%E4%B8%AA%E6%8C%87%E5%AE%9A%E7%9A%84%E6%95%B0%E6%8D%AE.png)
      * select()：
        * 元素选择器-element:soup.select('a')，查找所有a标签，直接传标签名的话就和find_all的作用一样
        * 类选择器-class：soup.select('.a1')，根据class属性的值，查找指定的标签/数据，需要在属性值钱加个.
        * id选择器-#id：soup.select('#l2')，返回id属性值为l2的标签，需要在属性值前加个#
        * 属性选择器:
          * soup.select('li[id]')，返回有id属性的所有li标签
          * soup.select('li[class]')，返回有class属性的所有li标签
          * soup.select('li[id="l2"]')，返回id属性值为l2的li标签
        * 层级选择器/后代选择器
          * 空格  ，后代选择器，通过空格可以将两个祖孙关系的标签连起来，快速找到子孙标签的对象，返回的是一个列表。
            * element element
          * 大于 >，子代选择器，通过逗号可以获取指定的某标签的第一级子标签，不能一步实现找到子孙标签，需要一层一层地列出标签。
            * element>element1>element2
          * 逗号 ,，与需要写成两个独立的标签用逗号隔开的find_all方法不同，select方法中想要获取多个标签对象，写在一起，用逗号隔开即可，这一点相比xpath和jsonpath更加人性化。
            * element,element，eg：soup=soup.select('a,li')
  * 4. 节点信息
    * 获取节点内容：适用于标签中嵌套标签的结构，调用select函数返回的结果是列表，而列表不会有string属性和get_text()，因此需要通过下标的方式提取出列表里的元素，再调用string或get_text()来获取节点的内容。
    * string和get_text方法虽然都是获取节点内容的方式，但更加推荐使用get_text方法，因为如果标签中除了内容，还包含了了其他标签，就无法通过string属性获取节点内容，还需要将标签对象的子标签或子孙标签一一列出来，但get_text不同，可以直接获取。
      * obj.string
      * obj.get_text()【推荐】
        * ```
            obj=soup.select('#d1')[0]
            print(obj.string)   #None
            obj=soup.select('#d1>span')[0]
            print(obj.string)   #嘿嘿嘿
            print(obj.get_text())   #嘿嘿嘿
          ```
    * 节点的属性
      * tag.name-获取标签名，通过id获取p标签，依旧因为调用select函数返回的是一个列表，而无法直接通过.name来获取节点的属性，因此需要先获取列表中的元素，再调用.name。
        * ```
            obj=soup.select('#p1')[0]
            print(obj.name) #p
          ```
      * tag.attrs-将该标签拥有的所有属性值整理成一个字典返回
        * ```
            obj=soup.select('#p1')[0]
            print(obj.attrs)    #{'id': 'p1', 'class': ['p1'], 'style': 'font-size:30px;color:aqua'}
          ```
    * 获取节点属性，三种方法，调用标签对象的attrs属性后，再调用get方法，传递属性名做参数；直接调用标签对象的get方法传递属性名作参数；不调用任何方法或属性，用[]包裹属性名，从标签对象中获取。三种方法皆可，但推荐使用第一种。
      * obj.attrs.get('title')
      * obj.get('title')
      * obj['title']
        * ```
            obj=soup.select('#p1')[0]
            print(obj.attrs.get('class'))   #['p1']
            print(obj.get('class')) #['p1']
            print(obj['class']) #['p1']
          ```
  * 案例：bs4解析麦当劳
    * 从麦当劳官网的菜单的汉堡区，获取URL路径，随后照常引入urllib.request，但这次不用UA和cookie进行反爬，直接模拟浏览器向服务器发送请求，并调用read方法和decode方法来获取网页源码。回到网页当中，用快捷键(Ctrl+Shift+X)激活xpath工具，获取想要爬取的麦当劳汉堡页数据的xpath路径//div[@class="row"]//a/span。根据xpath路径可以推算出，相对应的bs路径.row a>span。引入bs4后，调用BeautifulSoup方法，里面传入获取的网页源码content和lxml做参数，并将返回值赋值给变量soup，查询数据调用select方法，将bs路径传进去做参数，即可获得有关汉堡的全部信息，但因为select方法返回的数据是列表类型的数据，想要获取汉堡的名字不能直接用string属性或get_text方法，因此通过for循环对select方法的返回值进行遍历即可获取汉堡的名字。
    
## 十七、Selenium
* 17.1 Selenium
  * 1. 什么是selenium？
    * Selenium是一个用于Web应用程序测试的工具。
      * 通过请求对象定制，向服务器发送请求，获取数据时，因为有一部操作是模拟浏览器向服务器发送请求，所以获取到的数据多多少少会有遗漏，且网站可能会监测到用户是在使用爬虫程序，还会有各种各样的反爬手段，比如：获取到的数据是加密的，又或者直接不给数据。而selenium就是帮助驱动真实的浏览器，就不会被反爬手段拦截掉数据。
    * Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。
    * 支持通过各种driver(FirefoxDriver,InternetExplorerDriver,OperaDriver,ChromeDriver)驱动真实浏览器完成测试。
    * selenium也是支持无界面浏览器操作的。
  * 2. 为什么使用selenium？
    * 通过请求对象定制，从服务器获取源码是模拟浏览器向服务器发送请求的，获取的数据不完整。但用selenium的话，是在浏览器直接运行的，是模拟浏览器功能，自动执行网页中的js代码，实现动态的加载。下面的图就是，通过请求对象定制，模拟浏览器向服务器发送请求后获取的源码，无法想要通过class属性查找到淘宝秒杀。
      * ![通过对象定制获取淘宝首页源码后，用淘宝秒杀模块的class属性值查找源码，无法找到](imgs/%E9%80%9A%E8%BF%87%E5%AF%B9%E8%B1%A1%E5%AE%9A%E5%88%B6%E8%8E%B7%E5%8F%96%E6%B7%98%E5%AE%9D%E9%A6%96%E9%A1%B5%E6%BA%90%E7%A0%81%E5%90%8E%EF%BC%8C%E7%94%A8%E6%B7%98%E5%AE%9D%E7%A7%92%E6%9D%80%E6%A8%A1%E5%9D%97%E7%9A%84class%E5%B1%9E%E6%80%A7%E5%80%BC%E6%9F%A5%E6%89%BE%E6%BA%90%E7%A0%81%EF%BC%8C%E6%97%A0%E6%B3%95%E6%89%BE%E5%88%B0.png)
  * 3. 如何安装selenium
    * 操作谷歌浏览器驱动下载地址
    * 谷歌驱动和谷歌浏览器版本之间的映射表，在下面这个地址中查看
      * https://googlechromelabs.github.io/chrome-for-testing/
    * 查看谷歌浏览器版本
      * 谷歌浏览器右上角三个点-->帮助-->关于，确定浏览器的版本后，根据浏览器版本安装对应的驱动。下载驱动后，将其放在文件所在的同一目录中。并准备安装selenium。
    * pip install selenium
      * 安装selenium，下载到安装Python的Script文件夹中，但会被下载到Lib下的site-package目录中。
  * 4. selenium的使用步骤
    * (1). 导入，导入前安装webdriver-manager，可以自动管理驱动，```pip install webdriver-manager```
      * ```
          from selenium import webdriver
          from selenium.webdriver.chrome.service import Service
        ```
    * (2). 创建谷歌浏览器操作对象
      * ```
          service=Service('chromedriver.exe')
          driver=webdriver.Chrome(service=service)
        ```
    * (3). 访问地址
      * ```
          url='https://taobao.com'
          driver.get(url)
        ```
    * 随后就可以调用page_source来获取网页源码，可以打印出来查看是否与浏览器中查看到的源码一致。运行后，访问的网址就会被打开，控制台中也会打印出完整的数据，如下图可以查看到是完整的全部数据，之前用请求对象定制的方式无法爬取到。点击运行后会打开访问地址，但也会闪退，这是因为selenium的版本过高，需要跳到3.3.x版本，但我懒得在下一次selenium，就不试了。想不闪退可以在文件最后加个死循环或者打印input语句，在控制台输入内容前，不会退出，亲测有效。
      * ![通过selenium爬取淘宝数据，可查看到是获取到了完整的数据](imgs/%E9%80%9A%E8%BF%87selenium%E7%88%AC%E5%8F%96%E6%B7%98%E5%AE%9D%E6%95%B0%E6%8D%AE%EF%BC%8C%E5%8F%AF%E6%9F%A5%E7%9C%8B%E5%88%B0%E6%98%AF%E8%8E%B7%E5%8F%96%E5%88%B0%E4%BA%86%E5%AE%8C%E6%95%B4%E7%9A%84%E6%95%B0%E6%8D%AE.png)
    * 4-1 selenium的元素定位
     * 元素定位：自动化要做的就是模拟鼠标和键盘来操作这些元素，点击、输入等等，操作这些元素前，首先要找到它们，WebDriver提供很多定位元素的方法。
       * 方法：
         * find_element(By.ID,'idValue')/find_element('id','idValue')：唯一元素-根据id值查找对象，两种方法皆可。
         * find_element(By.NAME,'nameValue')/find_element('name','nameValue')：根据标签属性的属性值来获取对象。
           * ![通过name属性的值查找对象](imgs/%E9%80%9A%E8%BF%87name%E5%B1%9E%E6%80%A7%E7%9A%84%E5%80%BC%E6%9F%A5%E6%89%BE%E5%AF%B9%E8%B1%A1.png)
         * find_element(By.XPATH,'//标签名[属性名="属性值"]')/find_element('xpath','//标签名[属性名="属性值"]')：嵌套结构-根据xpath语句获取对象，哪个属性方便就用哪个，一般用id属性。
         * find_element(By.TAG_NAME,'标签名')：简单场景，因此慎用-根据标签名获取对象，也可以用CLASS_NAME，但建议慎用，因为鼠标放上去或点击后，其值容易发生变化。
         * find_element(By.CSS_SELECTOR,'attributeValue')：复杂选择-使用的是bs4的语法来获取东西，在情况叫复杂时可以说是最优选择，性能也是最优的。
       * 五种方法中最常用的是，By.ID，By.XPATH，By.CSS_SELECTOR这三种，NAME是因为属性名叫name的不多，TAG_NAME或CLASS_NAME是因为叫同一标签名的太多，不好定位，且CLASS_NAME的值可能随时会出现变化。
    * 4-2 询问元素信息
      * 获取元素属性：.get_attribute('属性名')
        * 调用.get_attribute()，只要传入具体标签的准确的属性名，可以获取到对象内指定标签的所有属性的值。
          * ```
              input=browser.find_element(By.ID,'su')
              print(input.get_attribute('class')) #bg s_btn
              print(input.get_attribute('value')) #百度一下
              print(input.get_attribute('type'))  #submit
            ```
      * 获取元素文本：.text
        * 调用text，可以获取到对象的文本内容，只不过，要获取的文本内容不可以是自闭和标签，比如input，因为这是个输入框标签，起初啥也没有，也就无法获取到
          * ```
              news=browser.find_element(By.LINK_TEXT,'新闻')
              print(news.text)    #新闻
            ```
      * 获取标签名：.tag_name
        * 调用tag_name可以获取到对象的标签名，举两个例子，一个是百度输入框的，一个是页面右上侧地图的。
          * ```
              # 获取百度输入框按钮的标签名
              input=browser.find_element(By.ID,'su')
              print(input.tag_name)   #input
              # 获取页面右上侧地图的标签名
              map=browser.find_element(By.LINK_TEXT,'地图')
              print(map.tag_name) #a
            ```
    * 4-3 交互
      * 点击：click()
      * 输入：send_keys()
      * 后退操作：browser.back()
      * 前进操作：browser.forward()
      * 模拟JS滚动：
        * js='document.documentElement.scrollTop=100000'
        * browser.execute_script(js)
      * 获取网页代码：page_source
      * 退出：browser.quit()
      * 需求：从百度主页面开始，在文本框中输入人名后，点击百度一下按钮，随后往下滑，滑到页面最底部，然后点击下一页，但又想回到上一页，进行后退操作，随后又回到刚才的那一页，进行前进操作，最后退出。
        * 步骤解析：
        * 注：会在每个重要步骤前后调用sleep方法来模拟真人操作。
          * (1). 照常进行交互前三个步骤，导入、创建驱动对象、设置访问地址，随后在百度主页面的搜索框中输入秦彻，调用sleep方法，睡两秒；
          * (2). 点击百度一下按钮，调用sleep方法，睡两秒；
          * (3). 等待搜索后，滚动到页面最底部，调用sleep方法，睡两秒；
          * (4). 在最底部，按下下一页的按钮，调用sleep方法，睡两秒；
          * (5). 目前是在第二页，点击左上侧后退按钮，回到第一页，调用sleep方法，睡两秒；
          * (6). 目前是在第一页的顶部，再点击左上侧前进按钮，回到第二页，调用sleep方法，睡两秒；
          * (7). 目前是在第二页的顶部，最后退出。
* 17.2 Phantomjs
  * 1. 什么是Phantomjs？
    * (1). 是一个无界面的浏览器
    * (2). 支持页面元素查找，js的执行等
    * (3). 由于不进行css和gui渲染，运行效率要比真实的浏览器要快很多
    * (4). 但不推荐使用PhantomJS，因为官方已停止更新并有安全隐患。旧项目、老系统上仍可运行，但新项目不建议使用，因为不兼容现代JS或CSS，且无法支持最新的网页标准。
  * 2. 如何使用Phantomjs？
    * (1). 获取PhantomJS.exe文件路径path
    * (2). browser=webdriver.PhantomJS(path)
    * (3). browser.get(url)
    * 扩展：保存屏幕快照:browser.save_screenshot('baidu.png')
    * 其实就是换了一个驱动器使用，其他步骤和操作和selenium一样，但就算写了也不会正常运行，因PhantomJS已停用，非要用的话，可以将Python和Chrome及ChromeDriver的版本降一下，但很显然实在是没必要。
      * ![PhantomJS的基本使用，因PhantomJS不再适用，且这么写了也会报错，就放个图](imgs/PhantomJS%E7%9A%84%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8%EF%BC%8C%E5%9B%A0PhantomJS%E4%B8%8D%E5%86%8D%E9%80%82%E7%94%A8%EF%BC%8C%E4%B8%94%E8%BF%99%E4%B9%88%E5%86%99%E4%BA%86%E4%B9%9F%E4%BC%9A%E6%8A%A5%E9%94%99%EF%BC%8C%E5%B0%B1%E6%94%BE%E4%B8%AA%E5%9B%BE.png)
* 17.3 Chrome handless
  * Chrome-handless模式，Google针对Chrome浏览器59版新增加的一个模式，可以让用户不打开UI界面(如百度一下的页面)的情况下使用Chrome浏览器，所以运行效果与Chrome保持完美一致，效率比用户直接使用Chrome更高。
  * 1. 系统要求：
    * Chrome
      * Unix\Linux 系统需要 chrome>=59
      * Windows 系统需要 chrome>=60
    * Python3.6
    * Selenium==3.4.*
    * ChromeDriver==2.31
  * 2. 配置：
    * ```
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        options=Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        
        path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        chrome_options.binary_location=path
      
        browser=webdriver.Chrome(options=options)
      
        browser.get('http://www.baidu.com/')
      ``` 
    * 最近因为Chrome浏览器更新了，但ChromeDriver的版本没跟上，按照上面的配置运行代码，出现了版本不匹配，需要更新ChromeDriver版本的提示，去安装谷歌驱动的映射表下载最新版即可。
      * ![谷歌驱动和谷歌浏览器版本不匹配时出现的提示](imgs/%E8%B0%B7%E6%AD%8C%E9%A9%B1%E5%8A%A8%E5%92%8C%E8%B0%B7%E6%AD%8C%E6%B5%8F%E8%A7%88%E5%99%A8%E7%89%88%E6%9C%AC%E4%B8%8D%E5%8C%B9%E9%85%8D%E6%97%B6%E5%87%BA%E7%8E%B0%E7%9A%84%E6%8F%90%E7%A4%BA.png)
      * ![谷歌驱动和谷歌浏览器版本匹配时正常运行](imgs/%E8%B0%B7%E6%AD%8C%E9%A9%B1%E5%8A%A8%E5%92%8C%E8%B0%B7%E6%AD%8C%E6%B5%8F%E8%A7%88%E5%99%A8%E7%89%88%E6%9C%AC%E5%8C%B9%E9%85%8D%E6%97%B6%E6%AD%A3%E5%B8%B8%E8%BF%90%E8%A1%8C.png)
  * 3. 配置封装
    * 创建一个函数，在函数内进行创建驱动的操作，最后返回浏览器/驱动对象，在需要用到的时候直接调用shareBrowser函数即可。
    * ```
        def shareBrowser():
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            # 创建浏览器/驱动对象
            browser = webdriver.Chrome(options=options)
            # 返回驱动
            return browser
        # 调用shareBrowser函数
        browser=shareBrowser()
        # 调用get方法，传入访问地址作为参数来获取数据
        browser.get('http://www.baidu.com/')
        print(browser)  #<selenium.webdriver.chrome.webdriver.WebDriver (session="c94919a690f79a81a61bf73fa650c78e")>
      ```
  * PhantomJS和Chrome handless的独特之处就是无界面操作，selenium虽然可用，但是会加载网页页面，速度肯定会跟不上无界面的。目前PhantomJS虽已停用，但Chrome handless还是可用的。

## 十八、requests
* 18.1 基本使用
  * 1. 介绍：Requests是唯一一个非转基因的Python HTTP库，人类可以安全使用，但现在收费。
  * 2. 文档
    * 官方文档：http://cn.python.requests.org/zh_CN/lastest/
    * 快速上手：http://cn.python.requests.org/zh_CN/lastest/user.quickstrat.html
  * 3. 安装
    * pip install requests
  * 4. response的属性及类型--一个类型六个属性
    * 一个类型--请求对象定制的方式获取到的response的类型是HTTPResponse类型，与其不同，用requests获取的数据类型是Response类型
      * ![用requests获取的response的数据类型是Response类型](imgs/%E7%94%A8requests%E8%8E%B7%E5%8F%96%E7%9A%84response%E7%9A%84%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%E6%98%AFResponse%E7%B1%BB%E5%9E%8B.png)
    * 六个属性
      * .text--调用.text可获取到网页源码，但可能会有乱码，不想看见乱码，就可以设置编码格式，即可得到完整又好看的源码。
        * ![用requests获取的数据调用text返回的网页源码可能会有乱码](imgs/%E7%94%A8requests%E8%8E%B7%E5%8F%96%E7%9A%84%E6%95%B0%E6%8D%AE%E8%B0%83%E7%94%A8text%E8%BF%94%E5%9B%9E%E7%9A%84%E7%BD%91%E9%A1%B5%E6%BA%90%E7%A0%81%E5%8F%AF%E8%83%BD%E4%BC%9A%E6%9C%89%E4%B9%B1%E7%A0%81.png)
      * .encoding--用于设置编码格式，图片
        * ![设置好编码格式，设置为utf-8就可以得到完整又好看的网页源码](imgs/%E8%AE%BE%E7%BD%AE%E5%A5%BD%E7%BC%96%E7%A0%81%E6%A0%BC%E5%BC%8F%EF%BC%8C%E8%AE%BE%E7%BD%AE%E4%B8%BAutf-8%E5%B0%B1%E5%8F%AF%E4%BB%A5%E5%BE%97%E5%88%B0%E5%AE%8C%E6%95%B4%E5%8F%88%E5%A5%BD%E7%9C%8B%E7%9A%84%E7%BD%91%E9%A1%B5%E6%BA%90%E7%A0%81.png)
      * .url--可以得到url地址
      * .content--可以获取到网页源码，只不过是二进制的，所以实在是没必要，想要获取源码调用text更方便，实在是没必要遭这份罪
        * ![content用于获取网页源码，只不过是二进制的](imgs/content%E7%94%A8%E4%BA%8E%E8%8E%B7%E5%8F%96%E7%BD%91%E9%A1%B5%E6%BA%90%E7%A0%81%EF%BC%8C%E5%8F%AA%E4%B8%8D%E8%BF%87%E6%98%AF%E4%BA%8C%E8%BF%9B%E5%88%B6%E7%9A%84.png)
      * .status_code--返回响应的状态码
      * .headers--返回响应的头信息
        * ![获取响应的头信息](imgs/%E8%8E%B7%E5%8F%96%E5%93%8D%E5%BA%94%E7%9A%84%E5%A4%B4%E4%BF%A1%E6%81%AF.png)
* 18.2 get请求
  * request.get()
  * 百度一下，北京：
    * ```
        import requests
        url='http://www.baidu.com/s?'
        headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
        data={
            'wd':'北京'
        }
        response=requests.get(url=url,params=data,headers=headers)
        content=response.text
        print(content)
      ```
    * 总结：
      * 参数使用params传递
      * 参数无需urlencode编码
      * 不需要请求对象定制
      * 请求资源路径，就是url中的 ? 可以加，也可以删除掉，加或不加并没有太大的区别
      * 只要能获取到数据用什么手段都无所谓，urllib和request都可以
* 18.3 post请求
  * request.post()
  * 百度翻译：
    * ```
        import requests
        url='https://fanyi.baidu.com/sug'
        headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
        data={
            'kw':'eye'
        }
        response=requests.post(url=url,data=data,headers=headers)
        content=response.text
        print(content)
        # 进一步解码
        import json
        obj=json.loads(content)
        print(obj)
      ```
      * ![requests的post请求.png](imgs/requests%E7%9A%84post%E8%AF%B7%E6%B1%82.png)
    * 总结：
      * post请求不需要编解码
      * post的请求参数是data
      * 不需要请求对象的定制
      * 不同于urllib的post请求，requests的post请求使用起来更加方便，因为requests唯一一个非转基因的、Python自己封装的Python库，因此使用起来没有那么多的顾虑
* 18.4 代理
* 18.5 cookie定制


* 当然是失败的，目标计算机甚至在积极地拒绝，但通过代理池可以更高效地工作，现实中公司会提供一个账号可以得到高匿又成量的代理IP。
* 这个parse和html是将内容转换成xml然后才能用xpath解析  简单说就是xpath只能解析xml文本