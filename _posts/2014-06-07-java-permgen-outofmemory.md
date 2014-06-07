---
comments: true
date: 2014-06-07 11:30:00
layout: post
slug: java-permgen-outofmemory
title: java permgen内存泄漏问题处理
categories:
- review
tag:
- java
- permgen
- ibatis
- jmap

---
<p>&nbsp;&nbsp;&nbsp;&nbsp;工作以来，第三次出现内存溢出，第一次是ThreadLocal没有remove造成的问题；第二次是ExecutorService没有正确的shutdown造成的问题；这一次的问题在我出手排查之前，已经知道了是permgen在不断的增长，在permgen中主要有Class和Meta信息，常量。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;在开始阶段：排除了ThreadLocal可能导致的问题；排除了Thread可能导致的问题；后面就需要从新的突破点找问题了。</p>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 1：基本设置的排查</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p>&nbsp;&nbsp;&nbsp;&nbsp;查找日志中访问量较大的请求的URL：<br \>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
awk '{print $6}' service-digest.* |awk -F"," '{print $1 ",""1"}'|awk -F","  '{a[$1]+=$2;b[$1]++}END{for(n in a)print a[n] " " n }'|sort -n 
</div>
<br \>&nbsp;&nbsp;&nbsp;&nbsp;查找日志中的调用很多的内容；依然没有发现问题；采用webbench一个个的调用请求来模拟操作，前十名的URL没有发现问题，后面的就没有查看了。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;通过线下操作，发现也不是开始怀疑的RMI远程调用的问题；</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;针对CMS-GC，网上建议开通 <strong>-XX:+CMSClassUnloadingEnabled -XX:+CMSPermGenSweepingEnabled</strong> ，好吧，我们一开始就是开通的。参考：<a href="http://stackoverflow.com/questions/5635255/permgen-out-of-memory-reasons" target="_blank">permgen-out-of-memory-reasons</a></p>
</div>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 2：内存使用情况</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p>&nbsp;&nbsp;&nbsp;&nbsp;2.1：查看内存使用情况</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
jmap -heap pid 
</div>
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;2.2：查看permsize的命令 </p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
jmap -heap `ps -ef  | grep java  | grep -v grep` | awk 'NR==44,NR==48'
</div> 
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;2.3：触发full gc :</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
 jmap -histo:live pid
</div>
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp; 2.4：不断的触发full GC 每10分钟观察一下内存的变化情况</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
PID=`ps -ef | grep java | grep uic | awk '{print $2}'` <br \>
for((i=1;i<10000;i++));do  <br \>
jmap -histo:live ${PID} > /tmp/fullgc.log <br \>
jmap -heap ${PID} | awk "NR==42,NR==48" >> heap.log <br \>
echo $i <br \>
sleep 600 <br \>
done  <br \>
</div>
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;2.5：观察一段时间后（5个小时），分析相关的permsize的内存增长情况</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
awk '{if(NR%7==0) print $0}' heap.log 
</div>
</div>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 3：查看perm中的情况</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
	jmap -permstat pid
</div>
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;查询的结果类似一下情况：</p>
<div style="border-top: 1px solid rgb(0, 0, 0); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(0, 0, 0); color:#fff;">
0x00000000ce58bb18      1       3200    0x00000000cc02c030      dead    sun/reflect/DelegatingClassLoader@0x00000000f4067700 <br \>0x00000000cec33d48      1       3088    0x00000000cc02c030      dead    sun/reflect/DelegatingClassLoader@0x00000000f4067700 <br \>0x00000000ce39c8b0      1       1944    0x00000000cc02c030      dead    sun/reflect/DelegatingClassLoader@0x00000000f4067700 <br \>0x00000000ce8ab270      1       3104      null          dead    sun/reflect/DelegatingClassLoader@0x00000000f4067700 <br \>0x00000000ceb1d108      1       3104    0x00000000cc02c030      dead    sun/reflect/DelegatingClassLoader@0x00000000f4067700 <br \><br \>total = 1600    11325   60491768            N/A         alive=1, dead=1599          N/A 
</div>  
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;不是反射的问题。（dead    sun/reflect/DelegatingClassLoader）</p>
</div>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 4：查看JDK的相关垃圾回收情况</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;我们使用了CMS GC，过程中发现的GC日志看不出任何问题。</p>
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;PS：未来我们找个时间专门讨论一下CMS GC的过程，方便我们在未来的垃圾处理过程中找到更加合理的方法去处理问题。</p>
</div>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 5：查看perm中的类加载情况</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;在启动的脚本中打开-verbose:class来查看运行的过程中到底多少个类被加载了。【verbose和verbose:class意义相同, 还有-verbose:gc, -verbose:jni】</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
JAVA_OPTS="${JAVA_OPTS}  -verbose:class"
</div>
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;启动脚本中把输出内容从<b> /dev/null 2>&1 &</b> 修改为 <b> >${PWD}/jvm.log </b> </p>


<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;我们通过jvm的日志发现如下奇怪的日志：</p>
<div style="border-top: 1px solid rgb(0, 0, 0); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(0, 0, 0); color:#fff;">
[Loaded com.hqb360.uic.dao.point.entity.BonusPointDetail$$BulkBeanByCGLIB$$5a972456_249 from file:/opt/jetty/work/jetty-0.0.0.0-8080-uic.war-_uic-any-/webapp/WEB-INF/lib/cglib-2.2.2.jar]<br \>
[Loaded com.hqb360.uic.dao.point.entity.BonusPointDetail$$BulkBeanByCGLIB$$5a972456_250 from file:/opt/jetty/work/jetty-0.0.0.0-8080-uic.war-_uic-any-/webapp/WEB-INF/lib/cglib-2.2.2.jar]<br \>
[Loaded com.hqb360.uic.dao.point.entity.BonusPointDetail$$BulkBeanByCGLIB$$5a972456_251 from file:/opt/jetty/work/jetty-0.0.0.0-8080-uic.war-_uic-any-/webapp/WEB-INF/lib/cglib-2.2.2.jar]<br \>
[Loaded com.hqb360.uic.dao.point.entity.BonusPointDetail$$BulkBeanByCGLIB$$5a972456_252 from file:/opt/jetty/work/jetty-0.0.0.0-8080-uic.war-_uic-any-/webapp/WEB-INF/lib/cglib-2.2.2.jar]<br \>
[Loaded com.hqb360.uic.dao.point.entity.BonusPointDetail$$BulkBeanByCGLIB$$5a972456_253 from file:/opt/jetty/work/jetty-0.0.0.0-8080-uic.war-_uic-any-/webapp/WEB-INF/lib/cglib-2.2.2.jar]<br \>
[Loaded com.hqb360.uic.dao.point.entity.BonusPointDetail$$BulkBeanByCGLIB$$5a972456_254 from file:/opt/jetty/work/jetty-0.0.0.0-8080-uic.war-_uic-any-/webapp/WEB-INF/lib/cglib-2.2.2.jar]<br \>
[Loaded com.hqb360.uic.dao.point.entity.BonusPointDetail$$BulkBeanByCGLIB$$5a972456_255 from file:/opt/jetty/work/jetty-0.0.0.0-8080-uic.war-_uic-any-/webapp/WEB-INF/lib/cglib-2.2.2.jar]<br \>
</div>
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;uic.dao.point.entity.BonusPointDetail的类一直在perm中增加，每次都在复制，没有重用，也没有被垃圾回收。问题基本就定位到这个地方。</p>

</div>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 6：找出问题的具体原因</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p style="padding-top:10px;color:#cc0000;">&nbsp;&nbsp;&nbsp;&nbsp;<b>6.1：去掉类中的反射，发现问题没有解决。空欢喜了一场！！！！</b></p>
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;6.2：反复的测试调用的页面，发现在插入操作的过程中，会出现步骤5中perm class日志的情况。针对</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
<pre  style = 'border:dashed 0px;'>
INSERT INTO bonus_point_detail (
                &lt;isNotEmpty property="id"&gt;
                id,
                &lt;/isNotEmpty&gt;
               ……
                gmt_created,
                gmt_modified
        )
    VALUES (
               &lt;isNotEmpty property="id"&gt;
               		#id#,
               &lt;/isNotEmpty&gt;
                    ……
                    now(),
                    now()
    )
    </pre>
</div>
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;这样的情况，我们修改为：</p>
<div style="border-top: 1px solid rgb(148, 218, 58); border-bottom: 1px solid rgb(148, 218, 58); padding: 9px 0pt 9px 16px; background-color: rgb(224, 255, 182);">
<pre  style = 'border:dashed 0px;'>
INSERT INTO bonus_point_detail (
                id,
               ……
                gmt_created,
                gmt_modified
        )
    VALUES (
                    #id#,
                    ……
                    now(),
                    now()
    )
    </pre>
</div>
<p style="padding-top:10px;">&nbsp;&nbsp;&nbsp;&nbsp;后续测试一下，发现问题解决，permgen不再持续增长；当某个内容写操作比较多的时候，直接导致permgen里面有大量的类消息，从而导致了内存溢出。</p>
</div>

<p style="padding-top:10px;color:#cc0000;font-size:16px;">&nbsp;&nbsp;&nbsp;&nbsp;待处理：我们将下次讨论为什么不能在insert的时候使用isNotEmpty的问题。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;</p>