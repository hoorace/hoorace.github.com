---
comments: true
date: 2013-09-02 19:16:09
layout: post
slug: use-sentry-to-feedback-your-system-problem
title: 用sentry来反馈您的系统问题
categories:
- python
tag:
- linux
- sentry
- python
- virtualenv

---
 
<p> &nbsp;&nbsp;&nbsp;&nbsp; 日志分析相关的操作，小公司没有实例去开发，当让程序员到线上不断关注日志又太依赖于人，很多问题不能很好的统计，不能反馈核心问题。没有错误日志的反馈，在关键路径的操作上，研发存在不少的盲点，遇到问题只有用户反馈的时候才去被动的修改，这不利于系统的演进。所以我们需要一个日志收集的系统。</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; Sentry 是一个实时的事件日志和聚合平台，基于 Django 构建。Sentry 可以帮助你将 Python 程序的所有 exception 自动记录下来，然后在一个好用的 UI 上呈现和搜索。处理 exception 是每个程序的必要部分，所以 Sentry 也几乎可以说是所有项目的必备组件。</p>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 1：安装sentry  
</strong></span></p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;安装sentry最开始没有在virtualenv下面，直接安装在自己的开发配置中，发现django是1.6和sentry6.1.2的版本是不兼容的，各种问题不断出现，“Internal Server Error” 的错误这样的情况下基本无解了，然后配置了N久的日志，打印不出来错误日志。各种纠结，折腾之后，还是不想卸载django1.6（因为有相关开发的内容是基于1.6的），只能在virtualenv环境安装sentry了。</p>

<p> &nbsp;&nbsp;&nbsp;&nbsp;1.1：安装virtualenv:</p>

<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
easy_install -UZ virtualenv
</div>
<p style="padding-top:6px;"> &nbsp;&nbsp;&nbsp;&nbsp;1.2：选择一个本地环境，执行virtualenv命令</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
virtualenv /opt/sentry/
</div>
<p style="padding-top:6px;"> &nbsp;&nbsp;&nbsp;&nbsp;1.3：激活你的virtualenv：</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
source /opt/sentry/bin/activate
</div>

<p style="padding-top:6px;"> &nbsp;&nbsp;&nbsp;&nbsp;1.4：安装sentry</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
easy_install -UZ sentry
</div>

<p style="padding-top:6px;"> &nbsp;&nbsp;&nbsp;&nbsp;<b style="background-color:#cc0000;color:#fff;">注意：</b>安装的过程中，遇到pytz这个包，安装流程会卡在这个地方。我是从pypi.python.org/pypi/pytz/2013b下周的文件，然后通过easy_install pytz_*.egg来安装这个包。在安装的过程中，网络一直timeout，需要不断的执行安装命令，后续会自动安装完毕。</p>

<p> &nbsp;&nbsp;&nbsp;&nbsp;1.5：安装sentry-mysql</p>

<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
easy_install -UZ sentry[mysql]
</div>

<p style="padding-top:6px;"> &nbsp;&nbsp;&nbsp;&nbsp;当然，其他数据库也可以根据配置选择安装，本人直接安装的MySQL-python就可以直接启动了，^_^</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;1.6：配置sentry.conf.py</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;--后面的路径配置过程中不是必须的，如果没有路径，将在用户的home的.sentry这个目录中生成sentry.conf.py</p>

<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
sentry init /etc/sentry.conf.py
</div>
<p style="padding-top:6px;"> &nbsp;&nbsp;&nbsp;&nbsp;生成完毕之后，注意到sentry.conf.py中去更改相关的DB配置，mysql的配置是：</p>

<div>
<pre><code>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sentry',
        #'NAME': os.path.join(CONF_ROOT, 'sentry.db'),
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
</code></pre>
</div>

<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 2：Sentry的相关操作 
</strong></span></p>

<p> &nbsp;&nbsp;&nbsp;&nbsp;2.1：启动服务</p>

<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
sentry --config=/etc/sentry.conf.py start
</div>

<p style="padding-top:6px;"> &nbsp;&nbsp;&nbsp;&nbsp;如果你用的是默认目录，则可以直接用sentry start来启动；</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;启动过程中如果报错，注意在sentry.conf.py中加入：</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
ALLOWED_HOSTS=['*'] 
</div>
<p style="padding-top:6px;"> &nbsp;&nbsp;&nbsp;&nbsp;一些其他配置的问题可以到文档中去搜一下，地址：
https://sentry.readthedocs.org/en/latest/quickstart/index.html</p>

<p> &nbsp;&nbsp;&nbsp;&nbsp;2.2：添加用户:</p>
![添加工程](http://longtask.com/images/sentry_account.png)
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
sentry --config=/etc/sentry.conf.py createsuperuser
</div>


<p style="padding-top:6px;"> &nbsp;&nbsp;&nbsp;&nbsp;2.3：添加teams</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;到右边菜单中，添加不同的团队的分组；</p>
![添加工程](http://longtask.com/images/sentry_team.png)

<p> &nbsp;&nbsp;&nbsp;&nbsp;2.4：添加工程</p>
![添加工程](http://longtask.com/images/sentry_project.png)
<p> &nbsp;&nbsp;&nbsp;&nbsp;每个团队下属的工程，各自添加，然后每个工程会有自己的API keys，拿着这个key配置不同模块的日志；</p>

<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 3：JAVA环境配置日志到sentry
</strong></span></p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;3.1：pom文件的修改</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;各项目根目录下面的 pom.xml文件的依赖:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&lt;!-- raven 依赖的maven服务器地址 --&gt;</p>
```
<repositories>
        <repository>
            <id>sonatype-nexus-snapshots</id>
            <name>Sonatype Nexus Snapshots</name>
            <url>https://oss.sonatype.org/content/repositories/snapshots</url>
            <releases>
                <enabled>false</enabled>
            </releases>
            <snapshots>
                <enabled>true</enabled>
            </snapshots>
        </repository>
</repositories>
```
<p> &nbsp;&nbsp;&nbsp;&nbsp;dependencyManagement中添加raven的依赖 </p>
```
<dependency>
	<groupId>net.kencochrane.raven</groupId>
	<artifactId>raven</artifactId>
	<version>4.0</version>
</dependency>
<dependency>
	<groupId>net.kencochrane.raven</groupId>
	<artifactId>raven-log4j</artifactId>
	<version>4.0</version>
</dependency>
```
<p> &nbsp;&nbsp;&nbsp;&nbsp;因为没有相关的应用，所以需要在跟pom.xml中添加dependencies来保证把raven的jar打到我们的发布包中；</p>

```
<dependencies>
            <dependency>
              <groupId>net.kencochrane.raven</groupId>
              <artifactId>raven</artifactId>
            </dependency>
            <dependency>
                <groupId>net.kencochrane.raven</groupId>
                <artifactId>raven-log4j</artifactId>
                <exclusions>
                    <exclusion>
                        <artifactId>log4j</artifactId>
                        <groupId>log4j</groupId>
                    </exclusion>
                </exclusions>
            </dependency>
</dependencies>
```
<p> &nbsp;&nbsp;&nbsp;&nbsp;3.2：log4j的配置添加</p>

<p> &nbsp;&nbsp;&nbsp;&nbsp;注意，dsn就是工程的API Keys，每个工程的都不一样。</p>

```
<appender name="SentryAppender" class="net.kencochrane.raven.log4j.SentryAppender">
        <param name="dsn" value="http://e61a0d19d87743bd9e0b7499b720c2a5:df28df39628e4dd5a4986eecf4923851@192.168.100.11:9000/1" />
        <layout class="org.apache.log4j.PatternLayout">
            <param name="ConversionPattern" value="%d [%X{realRemoteIp}/%X{memberId} - %X{servletPathInfoWithQueryString}] %-5p %c{2} - %m%n" />
        </layout>
</appender>
```
<p> &nbsp;&nbsp;&nbsp;&nbsp;在相关的error日志配置中添加：</p>
```
<appender-ref ref="SentryAppender" />
```

<p> &nbsp;&nbsp;&nbsp;&nbsp;例如：</p>
```
<logger name="com.okhqb.canvas" additivity="false">
        <level value="INFO" />
        <appender-ref ref="CANVAS-DEFAULT-APPENDER" />
        <appender-ref ref="ERROR-APPENDER" />
        <appender-ref ref="SentryAppender" />
</logger>
```
<p> &nbsp;&nbsp;&nbsp;&nbsp;如果系统有错误日志产生，就会在sentry中看到相关的错误日志的分析结果了。</p>

<p> &nbsp;&nbsp;&nbsp;&nbsp;错误日志的展示结果：
</p>
![错误日志展示](http://longtask.com/images/sentry_1.jpg)

<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 4：nginx的配置
</strong></span></p>

<p> &nbsp;&nbsp;&nbsp;&nbsp;使用sentrylogs来监控nginx的日志，到https://github.com/mdgart/sentrylogs 去了解一下源码，通过 easy_install sentrylog就可以安装，然后设置sentry的dsn 启动的时候注意几个参数的指定。
<ul>
<li>--sentrydsn SENTRYDSN, -s SENTRYDSN   指定dsn的路径</li>
<li>--daemonize, -d 静默启动</li>
<li>--nginxerrorpath NGINXERRORPATH, -n NGINXERRORPATH   Nginx错误日志的目录</li>
</ul>
 </p>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 5：其他系统的配置
</strong></span></p>

<p> &nbsp;&nbsp;&nbsp;&nbsp; 在project的setting中可以找到相关模块的不同语言的example，可以通过案例来配置不同的语言，其他语言后续会不断补充……</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; </p>


