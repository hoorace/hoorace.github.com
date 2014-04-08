---
comments: true
date: 2014-04-08 10:32:49
layout: post
slug: system-monitor-design
title: 系统监控的设计实践
categories:
- linux
tag:
- log
- nagios
- cacti
- sentry
- rsync
- django

---
<p>&nbsp;&nbsp;&nbsp;&nbsp;作坊式的开发的重点是围绕业务开展工作，系统开发出来之后，优化的工作一般都是针对用户端，出现问题一段时间后，有用户反馈才能够发现系统中的业务问题，而有些业务问题其实看看错误日志就可以解决。开发在没有日志反馈的开发环境中，发现问题是被动的。运维人员在这个过程中，也只能被开发驱动去被动解决问题，可能这个问题只是linux配置的问题。为何运维不能及时发现问题通知开发做出相关的调整呢？</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;为了更好的反馈问题，我们需要对现有的系统监控做好的同时，做好日志监控。界面化的发布系统目的是降低手动操作错误。</p>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 1：监控系统</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;监控分为系统监控(Nagios)，网络监控（Cacti）和业务监控（自主开发）。当系统磁盘满了，I/O的过于频繁，CPU使用率过高，我们通过Nagios的监控给运维人员发送短信提醒来迅速的定位并解决问题。Cacti很好的帮助我们查看系统之间的访问流量情况。业务是否可用，我们是在一个界面查看使用情况，由于我们的系统上有2个集群，把所有的服务列到一个界面，很直观的展示了线上服务的可用性，方便我们在某集群故障的时候做切换。</div>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 2：日志系统</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p><strong>2.1:系统错误日志的整理</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;错误日志的监控使用了sentry，当系统有错误日志的时候，写一份到sentry方便我们分析查看，把各模块的错误日志的解决落实到人，能够快速的定位线上系统的代码bug。错误日志的记录包括：Java系统错误日志，PHP系统错误日志，Nginx错误日志。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;这种错误日志的监控不是实时的，根据系统统计的结果，在2天之内能够解决问题即可。有时候会发现严重的问题，需要及时处理。</p>
<p><strong>2.2:代码执行的慢日志</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;代码执行效率低的查询问题，我们系统本来是记录相关的代码执行时间，借用的是taobao的profile，以前我们都是手动去查看哪些慢日志，为了更加的高效，我就找同事写了个脚本来分析一下这方面的代码执行率低的记录，然后通过界面集成到运维系统中去。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;一期项目执行配合的流程是这样的：研发提供相关的脚本→运维负责用django开发后端→前端人员负责美化界面→研发人员测试。在写的过程中没有什么难度，都是很顺畅的利用了现有的资源，把一个手动的需求整合到界面中去了而已。这样做的目的是提高团队的开发效率，更快的反馈性能问题。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;性能的优化是个长期的过程。</p>
<p><strong>2.3:DB的慢日志</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;DB的慢日志，通过脚本来读取相关的mysql的慢日志，由运维开发人员集成到运维平台上去。DB的慢日志可以找到我们数据库设计和代码联合查询的问题，对我们优化DB起到合理的反馈作用。</p>
<p><strong>2.4:Nginx的503错误预警</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;通过sentry来查看日志并不能及时的发现Nginx的503错误，在系统503错误出现的5秒内，我们需要有一个预警机制来处理后端系统宕机的情况，开始阶段通过脚本来处理，后续考虑使用Logstash来配合分析解决问题。</p>
</div>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 3：界面化的发布系统</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p>&nbsp;&nbsp;&nbsp;&nbsp;部署系统分为2个部分，一个是PHP的部署，以前手动的敲命令，部署时间比较长，出错的机率大，回滚起来不方便，为了解决这个问题，我们分析了整个部署流程，通过界面化的操作来执行发布，大大的提高了效率，降低了出错的情况。在整个开发的过程中，我们只是把手动的工作脚本化和界面化了而已。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;Java的部署采用的Jenkins来完成，又快捷又好用，点一点鼠标，很多事情都通过脚本来搞定了。脚本使用了rsync来Linux hosts之间文件传输。持续集成方面的探索对运维工作效率的提升大有好处，大家不妨去抽空好好的研究一下。</p>
</div>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 4：配置管理系统</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p>&nbsp;&nbsp;&nbsp;&nbsp;目前运维工作中，还缺少一个统一配置管理的工具，我们考虑用zookeeper来解决这个问题。只是配置方面现在已经很少变动了，整个系统还没有到达必须没有配置服务就经常出错的程度，所以还没有动力去做。目前还没有找到一个可以动手开始的配置项目，为了让系统足够的轻，我们暂时选择配置手动。</p>
</div>
<p>&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;</p>