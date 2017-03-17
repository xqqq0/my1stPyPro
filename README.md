# my1stPyPro
我的第一个Python程序
> 本博客是记录跟从慕课网课程所记下的笔记，更多内容请访问慕课网[慕课网](https://www.baidu.com/link? url=XGorjLn3qqtdeVCp5aZj5YuAqaV0mLdYQoR0QcG50wv5BNt55vM-uMqXqDRDoSRX4IfZn8oiVVpqLv6Mwtc2pzMp4JH3vbF050aP-B7X5sW&wd=&eqid=c5446d38004215c20000000358bcd170)--[项目源码](https://github.com/xqqq0/my1stPyPro.git)

# 新建项目
* 打开命令行，进入到打算打算创建项目的目录
*  输入 `django-admin startproject 项目名字`，本例中取名为myBlog

#分析项目文件
![项目目录.png](http://upload-images.jianshu.io/upload_images/954728-27245b9005921ffd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### manager.py
* 与项目交互的命令行工具集入口
* 项目管理器
![manager.py.png](http://upload-images.jianshu.io/upload_images/954728-53084991fd3e1344.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 启动服务器runserver
`python mange.py runserver`
`固定端口启动 python mange.py runserver 端口号`
![runserver.png](http://upload-images.jianshu.io/upload_images/954728-9427db4072237fea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 项目同名目录 myBlog
* 项目的一个容器
* 包含项目的最基本的配置
* 不建议修改

### wsgi.py【Python服务器网管接口】
* Python应用和与web服务器之间的接口

### url.py
* URL配置我呢间
* Django项目的所有地址（页面）都需要在此文件中进行配置

### settings.py
* 项目总配置文件
* 包含数据库，web应用，时间等各种配置
  * BASE_DIR：项目根目录
  * SECRET_KEY：安全码，项目启动所必须，会自动配置好
  * DEBUG： 是否是调试模式，生产环境要置为False
  * ALLOWED_HOSTS: 主机名，限制访问系统的主机地址
  * INSTALLED_APPS：系统创建和自定义的应用
  * MIDDLEWARE: 中间件，简单理解为项目，项目自带的工具集
  * ROOT_URLCONF：URL的根文件，其默认指向的就是url.py
  * TEMPLATES: 模板文件，Django中模板就是HTML文件
  * DATABASES：数据库配置，默认是其自带的sqlite3,具体生产可以看[Django](https://docs.djangoproject.com/en/1.10/ref/settings/#databases)官网对其他数据库的配置要求
  * STATIC_URL： 静态文件地址

### __init__.py 
* 声明模块的文件，内容可以为空

# 创建应用
* 进入 manage.py的同级目录
* `python manage.py startapp 应用名`
* 创建完成以后将应用名添加到`setting.py`的`INSTALLED_APPS`里
* 自己创建的应用是不能和系统名字相同的
* 应用下各模块介绍
![目录.png](http://upload-images.jianshu.io/upload_images/954728-01ac62a698055382.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * migrations:  数据移植模块，其目录下内容都是系统生成的
  * admin.py:  该应用下的后台管理系统配置
  * app.py:  该应用的一些配置，Django-1.9会自动已生成，之前的版本没有
  * models:  数据模块模块，存放数据表，但是DJango有ORM框架，一般会配合其使用
  * tests.py:  自动化测试模块，可以利用脚本进行自动化测试
  * views.py: 视图模块，执行相应的代码所以在的模块，代码逻辑处理的主要地点，项目`大部分`代码均在这里编写

# 创建响应【在blog.views 模块下】
* 引入头文件`from django.http import  HttpResponse`
* Django中每一个相应都要通过一个函数处理，参数为请求，返回值为相应
* 配置相应的url
  * 编辑urls.py
  * url 函数放在urlpattens列表中
  * url 函数参数： URL（一般用政策表达式），url对应的相应函数，url名称（可选）

# 详解url配置
* 方式1：
  * 在views.py 中创建相应函数
  * 在系统应用rls.py引入此函数,并在urlpattens中配置此url
* 方式2：
  * 在blog应用新建urls.py文件
  * 配置blog应用下urls.py
    * 导入头文件 `from django.conf.urls import url`
    *  导入相应views.py
    * 新建urlpattens,并按照方式1中进行url配置
  * 修改系统应用下urls.py的头文件 `from django.conf.urls import url`后面添加`include`,最终`from django.conf.urls import url,include`
  * 修改系统应用urls.py模块的urlpattens,`url(r'^index/',include("blog.urls")),`
* tip:
  * 配置url正则的时候，空串可以用"^$"
  * 非空串在正则匹配之后，记得要加上反斜杠"^index/$"

# 创建Templates【模板】
* Django中`templates` 就是指HTML文件
* Django 要使用模板语言`DTL（Django Templates Language）`
* 模板引擎很多，本例中使用的jinjia2,要修改模板引擎，可以在`settings.py`下`TEMPLATES`的`BACKEND`键值
* 具体步骤：
  * 在当前应用（不是系统应用）新建一个文件夹，名字是Templates
  * 在Templates文件夹下新建HTML文件，如果项目存在多个应用，那么在Tenplates下要新建一个与应用同名的文件夹，然后将HTML文件创建在此目录下
  * 在views.py中相应函数中，返回render渲染的HTML文件
    * render 在views.py创建的过程中就已经忍引入了 `from django.shortcuts import render`
    * render有很多参数，比较常用的是: request，模板名称.heml, 响应给前端的数据
  * render函数支持一个字典参数，key为传递给前台的数据的key值，value就是传递的数值

# 创建Models
* Django中一个model对应一张数据库表，models以类的形式存在，所以处理数据不会与SQL打交道，是对对象进行操作
* ORM ： 对象关系映射，实现了对象和数据库之间的映射，隐藏了数据访问细节，不编写SQL语句
* 具体创建models
  * 在应用的根目录下创建models.py,并引入models 模块【系统在创建应用的时候已经做了】
  * 创建类，继承models.Model,该类就是一张数据表
  * 类中创建数据表字段
      * 字段即类中的属性
      * 格式 `attr = models.数据类型()`,
         例如`title = models.CharField(max_length=32,default='title')`
         更多数据类型[请访问这里](https://docs.djangoproject.com/en/1.10/ref/models/fields/)
* 映射到数据表，即数据迁移
  * 命令行进入manage.py同一级目录
  * 执行`Python manage.py makemigrations` 应用名
`如果不传应用名，会将该项目下所有的应用制作数据迁移`
  * 执行`python mange.py migrate`
  * Django会自动在 `应用/migrations/`目录下生成移至文件
* sql语句查看 `python manage.py sqlmigrate 应用名 文件id`
* 获取数据库中数据
  *` views.py` 中引入` import models`
  * 获取数据 `article = models.Article.objects.get(参数)`
    参数可以是具体条件而定，本例用使用主键作为参数:
    `article = models.Article.objects.get(pk=1)`

# Admin 
* Django 自带的一个功能强大的`自动化数据管理界面`
* 被授权的用户可以直接在Admin中`管理数据库`
* Django 提供了很多针对Admin的`定制功能`
* 具体操作：
  * 创建超级管理员
  `python manage.py createsuperuser`
  * 通过`http://localhost:8000/admin/`访问后台界面
  * 修改界面为中文界面--修改`settings.py`中`LANGUAGE_CODE = 'zh_Hans'
* 配置应用下的admin.py
  * 引入自身models模块（或里面的模型类）
  * 编辑admin.py : admin.site.register(models.Article)
* 修改系统数据的默认显示方式
  * 在相应的类下面添加一个方法
  py3.x  :  `__str__ (self):`
  py2.7  : `__unicode__(self):`
返回值为想要在后台系统中展示的数据，本例中是用的self.title

# 博客主界面
* 主页面内容： 文章标题列表(含有主链接)，发表博客按钮(含有超链接)
* 文章列表编写思路：
  * 取出数据库中所有文章对象
    * 修改views.py `articles = models.Article.objects.all()`
  * 文章打包成列表，传递给前端
    * 将数据封装为对象返回给前台
 `return render(request,"blog/index.html", {"articles": articles})`
  * 前端页面获取到文章数据，以标题超链接的形式列出
    * 在前端页面遍历数据，格式为`{%for xx in xxs %}`

# 博客文章页面
  * 思路：
    * 标题
    * 文章内容
    * 修改文章按钮(超链接)

* 添加响应函数函数,为了获取具体的文章，要将代表文章的参数(本例中选择id)传入
```py
def article_page(request,article_id):
          article = models.Article.objects.get(pk=article_id)
          return render(request,"blog/article_page.html",{"article":article})
```
* 创建HTML模板,展示标题和内容
```
<body>
    <h1>{{article.title}}</h1>
    <br>
    <h3>{{article.content}}</h3>
    <br>
    <br>
    <a href="">修改文章</a>
</body>
```
* urls.py配置url:
  * 整体思路：在遗忘配置的url的链接后边追加文章的Id
  * 具体实现： `url(r'^article/(?P<article_id>[0-9]+)$',bv.article_page)` 
其中`(?P<article_id>[0-9]+)` 中article_id要和响应函数中的文字Id的参数名保持一致

# 博客主页面链接到文章页面
* 超链接目标地址，即a标签的href属性后边的链接地址，在Django中有固定的写法`{%url  "app_name : url_naeme" param %}`
  * app_name: 应用的命名空间
  * url_name：url链接名
  * param: 参数
  * {%url ....%} 是固定的写法
  * 注意字符串
*具体写法
  * 再言url的配置---url的第三个参数(在有inclue的情况下就是第二个参数)，写法有两种：
    * 写法1：在有include的情况下，include的第2个参数为定位`namespace="应用的命名空间"`
    * 写法2：在没有include的情况下，第3个参数为`name = "应用的命名空间"`

* 配置的这两个名字就是url_name的值
* app_name取的是系统应用下的url配置的命名空间
* 以上两个名字可以随便定义，没有固定的要求
# 博客撰写页面
* 思路
  * 页面：标题编辑栏，文章编辑区域，提交按钮
  * 提交数据，利用form表单
* 实现：
  * 编写前端界面
  ```
<body>
<form action="" method="post">
    <label> 文章标题：
    <input type="text" name="title">
    </label>
    <br>
    <label> 文章内容:
    <input type="text" name="content">
    </label>
    <br>
    <input type="submit" value="提交">
</form>
 ```
  * 添加页面的响应【配置url，写响应函数等等和前面一样，不赘述】
  * 写form表单提交的响应，存储新文章数据
    * 编辑相应函数：
      使用reques.POST["参数名"]获取表单数据；
     ` models.Article.objects.create(title= "", content="")`创建数据对象，并存储
  * post 提交保单的时候，要添加`{% csrf_token %}`，为了网络安全

# 修改文章
* 思路：新建文章和修改文章都是跳转文章撰写文章页面，不同的是修改文章页面需要向撰写文章页面传入文章id,为了不增加url，在这两个操作都传入Id,撰写页面传入0，其他页面根据数据库自己添加
* 具体实现：
  * 修改编辑页面的响应函数，增加文章id,根据Id进行判断，为0则直接返回编辑页面，否则根据Id取出文章对象，并将对象和页面一起返回
```
def edit_page(request,article_id):
    if str(article_id) == "0":
        return  render(request,"blog/edit_page.html")
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/edit_page.html",{"article":article })
```
  * 修改页面
     首页的新文章的链接的url总增加参数0
     文章页面的修改文章的链接url，传入文章Id

* 提交操作的处理
  * 思路：提交的响应函数也要增加文章id,此id不是参数，而是从前端页面传入，从request中获取
     如果为0的话，就创建文章；
     如果不为0，就取出对象，修改属性并保存。
```
def edit_action(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    article_id = request.POST.get("article_id")
    if str(article_id) == "0":
        models.Article.objects.create(title=title,content=content)
        articles = models.Article.objects.all()
        return render(request, "blog/index.html", {"articles": articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, "blog/article_page.html", {"article": article})
```
  * 在页面增加一个隐藏的input用于将文字Id转入到后台
```
<form action="{% url "blog:edit_action" %}" method="post">
    {% csrf_token %}
    {% if article %}
        <input type="hidden" name="article_id" value="{{ article.id }}">
        <label> 文章标题：
            <input type="text" name="title", value="{{ article.title }}">
        </label>
        <br>
        <label> 文章内容：
            <input type="text" name="content" value="{{ article.content }}">
        </label>
    {% else %}
        <input type="hidden" name="article_id" value="0">
        <label> 文章标题：
            <input type="text" name="title">
        </label>
        <br>
        <label> 文章内容：
            <input type="text" name="content">
        </label>
    {% endif %}
    <br>
    <input type="submit" value="提交">
</form>
```

# 番外篇：Django的一些使用技巧
### 过滤器
  * 写在模板中的，属于DJDe 模板语言
  * 可以修改模板的变量，从而显示不同页面
  * 格式 ： {{value| 过滤器}}
  * 叠加{{value | filter1 | filter2 ......}}
  * 例子： {{list_number| length}} 值为list_number的长度
  * 实战： 修改文章页面的if else

```
############### 修改前 #######################
<body>
<form action="{% url "blog:edit_action" %}" method="post">
    {% csrf_token %}
    {% if article %}
        <input type="hidden" name="article_id" value="{{ article.id }}">
        <label> 文章标题：
            <input type="text" name="title", value="{{ article.title }}">
        </label>
        <br>
        <label> 文章内容：
            <input type="text" name="content" value="{{ article.content }}">
        </label>
    {% else %}
        <input type="hidden" name="article_id" value="0">
        <label> 文章标题：
            <input type="text" name="title">
        </label>
        <br>
        <label> 文章内容：
            <input type="text" name="content">
        </label>
    {% endif %}
    <br>
    <input type="submit" value="提交">
</form>
</body>
###############修改后#######################
<body>
<form action="{% url "blog:edit_action" %}" method="post">
    {% csrf_token %}
    <input type="hidden" name="article_id" value="{{ article.id | default:"0" }}">
    <label> 文章标题：
        <input type="text" name="title", value="{{ article.title }}">
    </label>
    <br>
    <label> 文章内容：
        <input type="text" name="content" value="{{ article.content }}">
    </label>
    <br>
    <input type="submit" value="提交">
</form>
</body>
```

  * 解析 
     *  首先介绍DJ的一个模板特性，` <input type="text" name="title", value="{{ article.title }}">` 当模板中遇到一个没有定义的变量时，不会报错，会默认给一个空串，这样，即便不做if判断也可以兼容新文章页面和文章编辑页面
    * 但是，后台修改数据的时候，需要将文字id传入到后台，即我们写的隐藏的input便签，这时如果传空就会报错，此时我们用default 过滤器，即默认值 ` value="{{ article.id | default:"0"}} `，就可以兼容了

###  Django shell
  * 本质也是一个交互命令行，但是可以引入项目环境，与项目交互
  * 操作： `python manage.py shell` 就可以引入项目换将，然后就可以交互界面中实现项目代码
![djShell.png](http://upload-images.jianshu.io/upload_images/954728-2aa948d3a93bbcd0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* Admin
* 为了增加后台管理的功能，要修改应用下admin.py,改变注册方式
* 具体操作：
  * 创建admin 配置类`class ArticleAdmin(admin.ModelAdmin)`
  * 在注册代码中，绑定注册类 `admin.site.register(Article,ArticleAdmin)`
  * 修改配置类，增加功能
  * 代码
```
class ArticleAdmin(admin.ModelAdmin):
    # 增加显示列数，建议后面用元组，因为不可修改，且列名要与数据库字段名保持一致
    list_display = ("title","content")
admin.site.register(Article,ArticleAdmin)
```
  * 过滤功能（本例中以时间过滤为例子）
    * models.py增加一个时间字段
 `pub_time = models.DateTimeField(auto_now=True)` auto_nows属性为True的时候会自动赋值的当前日期，但在控制台中不能修改，若想修改则去掉此属性
  * 在admin.py中增加此字段的显示`list_display = ("title","content","pub_time")` 然后数据迁移
![admin.png](http://upload-images.jianshu.io/upload_images/954728-f553838be6490de1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * 修改admin.py给时间增加过滤器`list_filter = ("pub_time",)`

![filter.png](http://upload-images.jianshu.io/upload_images/954728-823a308b6ad83fa5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
 * 此时后台数据就可以进筛选
