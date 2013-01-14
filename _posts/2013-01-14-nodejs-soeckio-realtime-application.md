---
comments: true
date: 2013-01-14 09:52:19
layout: post
slug: nodejs-soeckio-realtime-application 
title: Node.JS Web长连接开发实践
categories:
- review
tag:
- node.js 
- socket.io
- websocket
- LXC
- Nginx-mem-module
---

2012年在架构设计上，个人觉得最有价值的表现在3个方面：<br />
1. **LXC**半虚拟化技术在线上环境的使用，解决了Java的端口的问题；<br />
2. **Nginx-mem-module**解决活动期间的并发问题；<br />
3. 使用**Node.js + Socket.io + Redis** 的架构设计开发出来了一个实时通讯的客服系统；<br />

由于这些架构设计对于我本来说都需要时间的考验，所以，都没有通过bolg写给大家看。简单的给大家说一下**架构选型的原因：**<br />
1. 使用**LXC**纯属KVM每次都需要启动虚拟机，LXC使用更加的简单，同时能够解决我们的问题，现在我甚至喜欢上了LXC在宿主机上启动进程的模式。<br />
2. **Nginx-mem-module**的使用是因为活动期间，我们系统挂掉了，在静态文件和nginx+memcached之间我们选择了Nginx-mem-module，后来发现开启keep-alive模式符合我们的预期。<br />
3. 作为java程序员，没有选择XMPP协议去开发一个实时通讯客服系统，是因为看到了trello.com的实时机制，我很喜欢这个团队实时协助的网站，就拉着人看看trello.com的架构，然后借鉴了去开发我们自己的系统。**node.js**入门比较简单，**socket.io**解决了大部分浏览器的问题，**redis**搞定并发。<br />

虽然沉淀了半年的时间，但是我依然觉得对问题的看法比较肤浅，所以**珠三角2013年活动沙龙聚会**我没有给大家讲具体的架构设计，而只是谈谈入门级别的内容，欢迎大家和我探讨。
PPT放到slideshare上了，看不到的猛击 **[这里](http://longtask.com/tools/node.js%E9%95%BF%E8%BF%9E%E6%8E%A5%E5%BC%80%E5%8F%91%E5%AE%9E%E8%B7%B5.pptx)** 下载

<iframe src="http://www.slideshare.net/slideshow/embed_code/15978875" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC;border-width:1px 1px 0;margin-bottom:5px" allowfullscreen webkitallowfullscreen mozallowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="http://www.slideshare.net/longhao/nodejs-15978875" title="Node.js长连接开发实践" target="_blank">Node.js长连接开发实践</a> </strong> from <strong><a href="http://www.slideshare.net/longhao" target="_blank">longhao</a></strong> </div>
